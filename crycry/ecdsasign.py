import sys
import argparse
import hashlib

import ecdsa
from ecdsa import curves


CURVES = {}
for c in curves.curves:
    CURVES[c.name] = c

arg_parser = argparse.ArgumentParser(
    description="Tool to generate private keys from ECDSA signatures with reused nonce."
)

arg_parser.add_argument(
    "--hash",
    help="Hash function used",
    default="sha1",
    choices=hashlib.algorithms_available
)

arg_parser.add_argument('privkey', type=argparse.FileType('rb'))


arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def main():
    args = arg_parser.parse_args()

    privkey = ecdsa.SigningKey.from_pem(args.privkey.read(), hashfunc=getattr(hashlib, args.hash))

    signature = privkey.sign(args.infile.read())

    args.outfile.write(signature)


if __name__ == '__main__':
    main()
