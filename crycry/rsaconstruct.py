import sys
import argparse

from Crypto.PublicKey import RSA


arg_parser = argparse.ArgumentParser(
    description="Tool to create PEM encoded RSA private key files from prime factors."
)

arg_parser.add_argument(
    "-e",
    "--exponent",
    help="The public exponent to be used",
    default=0x10001,
    type=int
)

arg_parser.add_argument('prime1', type=int)
arg_parser.add_argument('prime2', type=int)

arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def construct_rsa(prime1, prime2, e):
    p = prime1
    q = prime2

    n = p * q
    phi = (p - 1) * (q - 1)

    d = pow(e, -1, phi)

    privkey = RSA.construct((n, e, d))

    return privkey.exportKey()


def main():
    args = arg_parser.parse_args()

    key = construct_rsa(args.prime1, args.prime2, args.exponent)

    args.outfile.write(key)


if __name__ == '__main__':
    main()
