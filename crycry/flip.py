import sys
import argparse

arg_parser = argparse.ArgumentParser(
    description="Tool for flipping bits in given information."
)

arg_parser.add_argument(
    "--hex",
    help="Specify hex string as input instead of reading it from stdin.",
)

arg_parser.add_argument(
    "--byte",
    type=int,
    help="Byte number in which to flip a bit. First byte is indexed with 0 (zero).",
    required=True
)

arg_parser.add_argument(
    "--bit",
    help="Bit number within target byte to a bit. First, **most significant** bit is indexed with 0 (zero).",
    required=True,
    type=int,
    choices=range(0, 8)
)


arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def flip(input_raw, byte, bit):
    result = bytearray(input_raw)

    result[byte] ^= 1 << (7 - bit)

    return bytes(result)


def main():
    args = arg_parser.parse_args()

    if args.hex:
        try:
            input_raw = bytes.fromhex(args.hex)
        except ValueError:
            sys.stderr.write("Supplied Input is not valid hex!")
            sys.exit(1)
    else:
        input_raw = args.infile.read()

    output_raw = flip(input_raw, args.byte, args.bit)
    args.outfile.write(output_raw)


if __name__ == '__main__':
    main()
