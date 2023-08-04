from Crypto.PublicKey import ECC, RSA

import sys
import argparse

arg_parser = argparse.ArgumentParser(
    description="Tool for dumping numbers from encoded RSA and ECC keys."
)

arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)


def print_rsa(key_data):
    key = RSA.import_key(key_data)
    print(f"Modulus: N={key.n}")
    print(f"Public Exponent: e={key.e}")

    if key.has_private():
        print(f"Private Exponent: d={key.d}")
        print(f"Prime1: p={key.p}")
        print(f"Prime2: q={key.q}")


def print_ecc(key_data):
    key = ECC.import_key(key_data)
    print(f"Curve: {key.curve}")
    print(f"Public Point x values: Q.x={key.pointQ.x}")
    print(f"Public Point y values: Q.y={key.pointQ.y}")

    if key.has_private():
        print(f"Private Scalar: d={key.d}")


def main():
    args = arg_parser.parse_args()

    input_raw = args.infile.read()

    try:
        print_rsa(input_raw)
        exit(0)
    except ValueError:
        pass  # Not an RSA key, try ECC

    try:
        print_ecc(input_raw)
        exit(0)
    except ValueError:
        pass  # Not an RSA key, try ECC

    print("Unsupported key format.", file=sys.stderr)


if __name__ == '__main__':
    main()
