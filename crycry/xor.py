import argparse
import sys

arg_parser = argparse.ArgumentParser(
    description="Tool for XORing files with a key."
)

arg_parser.add_argument(
    "-k", "--key",
    help="Hex encoded key used for XOR. If key is shorter than input, it will be wrapped.",
    nargs=1,
    action="append"
)

arg_parser.add_argument(
    "-a", "--ascii-key",
    help="ASCII encoded key, used as is, for XOR. If key is shorter than input, it will be wrapped.",
    nargs=1,
    action="append"
)

arg_parser.add_argument("-n", help="Don't use an input file.", action="store_true")

arg_parser.add_argument('infile', nargs='*', type=argparse.FileType('rb'), default=[sys.stdin.buffer])
arg_parser.add_argument('--output', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def xor(input_a, input_b):
    result = bytearray()
    max_len = max(len(input_a), len(input_b))

    if len(input_a) == 0:
        return input_b
    elif len(input_b) == 0:
        return input_a

    for i in range(max_len):
        result.append(input_a[i % len(input_a)] ^ input_b[i % len(input_b)])

    return bytes(result)


def main():
    args = arg_parser.parse_args()

    if args.n:
        output_raw = b""
    else:
        output_raw = args.infile[0].read()

        for input_file in args.infile[1:]:
            input_raw = input_file.read()
            output_raw = xor(input_raw, output_raw)

    if args.key:
        for key_hex in args.key:
            key_hex = key_hex[0]
            try:
                key_raw = bytes.fromhex(key_hex)
            except ValueError:
                sys.stderr.write(f"Key is not valid hex: {key_hex}")
                sys.exit(1)

            output_raw = xor(output_raw, key_raw)

    if args.ascii_key:
        for key_ascii in args.ascii_key:
            key = key_ascii[0]
            try:
                key_raw = key.encode("ascii")
            except UnicodeEncodeError:
                sys.stderr.write(f"Key is not valid ascii: {key}")
                sys.exit(1)

            output_raw = xor(output_raw, key_raw)

    args.output.write(output_raw)


if __name__ == '__main__':
    main()
