import sys
import argparse
import hashlib

hashlib.algorithms_available

arg_parser = argparse.ArgumentParser(
    description="Tool for hasing using cryptographic hash functions."
)

arg_parser.add_argument(
    "-H",
    "--hash",
    help="Hash function name.",
    default="sha1",
    choices=hashlib.algorithms_available
)

arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def main():
    args = arg_parser.parse_args()

    input_raw = args.infile.read()

    output_raw = hashlib.new(args.hash, input_raw).digest()

    args.outfile.write(output_raw)


if __name__ == '__main__':
    main()
