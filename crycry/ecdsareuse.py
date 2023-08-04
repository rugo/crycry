import sys
import argparse
import hashlib

from ecdsa import SigningKey, numbertheory, SECP256k1, curves
from ecdsa.util import sigdecode_string, string_to_number


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

arg_parser.add_argument(
    "-c",
    "--curve",
    help="Curve to be used",
    default="NIST256p",
    choices=list(CURVES.keys())
)

arg_parser.add_argument('message1')
arg_parser.add_argument('signature1')
arg_parser.add_argument('message2')
arg_parser.add_argument('signature2')


arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def decode_sig(sig, curve):
    r, s = sigdecode_string(sig, curve.generator.order())
    return r, s


def compute_secret(curve, hashfunc, msg1, sig1, msg2, sig2):
    r1, s1 = decode_sig(
        bytes.fromhex(sig1), curve
    )
    z1 = string_to_number(hashlib.new(hashfunc, msg1.encode()).digest())

    r2, s2 = decode_sig(
        bytes.fromhex(sig2), curve
    )
    z2 = string_to_number(hashlib.sha1(msg2.encode()).digest())

    if r1 != r2:
        print("Signatures do not suffer from nonce reuse.", file=sys.stderr)
        return

    k = ((z1 - z2) * numbertheory.inverse_mod(s1 - s2, curve.generator.order())) % curve.generator.order()
    secret_key = (s1 * k - z1) * numbertheory.inverse_mod(r1, SECP256k1.generator.order())
    secret_key %= curve.generator.order()

    sk = SigningKey.from_secret_exponent(secret_key, curve)
    return sk.to_pem()

def main():
    args = arg_parser.parse_args()

    curve = CURVES.get(args.curve)

    if not curve:
        print("Invalid curve specified.")

    key = compute_secret(curve, args.hash, args.message1, args.signature1, args.message2, args.signature2)

    if not key:
        print("Failed.", file=sys.stderr)

    args.outfile.write(key)


if __name__ == '__main__':
    main()
