import sys
import argparse

arg_parser = argparse.ArgumentParser(
    description="Tool for PKCS7 padding of bytes."
)

arg_parser.add_argument(
    "-b",
    "--block",
    help="Block size in bytes.",
    default=16,
    type=int
)

arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def pad(data, block_size):
    last_block_spill = len(data) % block_size
    num_pad_bytes = block_size - last_block_spill

    data += bytes([num_pad_bytes] * num_pad_bytes)

    return data


def main():
    args = arg_parser.parse_args()

    input_raw = args.infile.read()

    output_raw = pad(input_raw, args.block)

    args.outfile.write(output_raw)


if __name__ == '__main__':
    main()
