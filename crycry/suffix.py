import sys
import argparse


arg_parser = argparse.ArgumentParser(
    description="Tool for outputting N least significant bytes from input."
)


arg_parser.add_argument(
    "-b",
    "--bytes",
    type=int,
    help="Number of bytes to write into outfile",
    required=True
)


arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def main():
    args = arg_parser.parse_args()

    byte_len = args.bytes

    input_raw = args.infile.read()

    args.outfile.write(input_raw[-byte_len:])


if __name__ == '__main__':
    main()
