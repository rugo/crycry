import argparse
import sys

arg_parser = argparse.ArgumentParser(
    description="Tool for XORing files with a key."
)

arg_parser.add_argument(
    "-k", "--key",
    help="Hex encoded key used for XOR. If key is shorter than input, it will be wrapped.",
    required=True
)

arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def xor(input_raw, key):
    result = bytearray()
    for i in range(len(input_raw)):
        result.append(input_raw[i] ^ key[i % len(key)])
    return bytes(result)


def main():
    args = arg_parser.parse_args()

    try:
        key_raw = bytes.fromhex(args.key)
    except ValueError:
        sys.stderr.write("Key is not valid hex!")
        sys.exit(1)

    input_raw = args.infile.read()

    output_raw = xor(input_raw, key_raw)
    args.outfile.write(output_raw)


if __name__ == '__main__':
    main()
