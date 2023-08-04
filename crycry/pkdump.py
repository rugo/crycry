from Crypto.PublicKey import ECC, RSA
import ecdsa

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


def test_ecc_ecdsa_formats(key_data):
    if key_data.startswith(b"---"):
        try:
            return ecdsa.SigningKey.from_pem(key_data)
        except Exception:
            pass
        try:
            return ecdsa.VerifyingKey.from_pem(key_data)
        except Exception:
            pass

    try:
        return ecdsa.SigningKey.from_der(key_data)
    except Exception:
        pass
    try:
        return ecdsa.VerifyingKey.from_der(key_data)
    except Exception:
        pass


def print_ecc_ecdsa(key_data):
    key = test_ecc_ecdsa_formats(key_data)

    if not key:
        raise ValueError("Invalid key.")

    if isinstance(key, ecdsa.VerifyingKey):
        x, y = key.pubkey.x(), key.pubkey.y()
    else:
        x, y = key.verifying_key.pubkey.point.x(), key.verifying_key.pubkey.point.y()

    print(f"Curve: {key.curve.name}")
    print(f"Public Point x values: Q.x={x}")
    print(f"Public Point y values: Q.y={y}")

    if isinstance(key, ecdsa.SigningKey):
        print(f"Private Scalar: d={key.privkey.secret_multiplier}")


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
        pass  # Not ECC common, try other encoding

    try:
        print_ecc_ecdsa(input_raw)
        exit(0)
    except ValueError:
        pass



    print("Unsupported key format.", file=sys.stderr)


if __name__ == '__main__':
    main()
