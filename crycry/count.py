import sys
import argparse

arg_parser = argparse.ArgumentParser(
    description="Tool for counting bytes."
)

arg_parser.add_argument(
    "-b",
    "--bits",
    help="Output number of bits instead of bytes",
    action="store_true"
)

arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)


def main():
    args = arg_parser.parse_args()

    input_raw = args.infile.read()

    input_len = len(input_raw)

    if args.bits:
        input_len *= 8

    print(input_len)


if __name__ == '__main__':
    main()
