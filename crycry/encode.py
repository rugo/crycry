import sys
import base64
import argparse
from enum import Enum
from string import whitespace
from urllib.parse import unquote_to_bytes, quote_from_bytes
import codecs

codecs.escape_decode

arg_parser = argparse.ArgumentParser(
    description="Tool for encoding and decoding files on the command line."
)


class Mode(Enum):
    Base16 = "base16"
    Base32 = "base32"
    Base64 = "base64"
    Base2 = "base2"
    URL = "url"
    ESCAPE = "escape"


arg_parser.add_argument("-d", help="Decode instead of encode.", action="store_true")
arg_parser.add_argument("--base64", help="Use base64 instead of base16.", dest="mode", action="store_const", const=Mode.Base64)
arg_parser.add_argument("--base32", help="Use base32 instead of base16.", dest="mode", action="store_const", const=Mode.Base32)
arg_parser.add_argument("--base16", help="Use base16 (hex). This is the default.", dest="mode", action="store_const", const=Mode.Base16)
arg_parser.add_argument("--base2", help="Use base2 (binary).", dest="mode", action="store_const", const=Mode.Base2)
arg_parser.add_argument("--url", help="Use url encoding.", dest="mode", action="store_const", const=Mode.URL)
arg_parser.add_argument("--escape", help="Use backslash escape encoding.", dest="mode", action="store_const", const=Mode.ESCAPE)

arg_parser.add_argument('infile', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer)
arg_parser.add_argument('outfile', nargs='?', type=argparse.FileType('wb'), default=sys.stdout.buffer)


def remove_whitespace(data):

    for char in whitespace:
        data = data.replace(char.encode(), b"")

    return data


def bytes_to_binstr(data):
    result = ""

    for byte in data:
        result += bin(byte)[2:].zfill(8)

    return result.encode()


def binstr_to_bytes(binstr):
    binstr = remove_whitespace(binstr)

    if len(binstr) % 8:
        raise ValueError("BinStr data is invalid, its length is not a multiple of 8.")

    result = b""

    for pos in range(0, len(binstr), 8):
        byte_val = int(binstr[pos:pos+8], 2)
        result += bytes([byte_val])

    return result


def encode(input_raw, mode):
    if mode == Mode.Base64:
        output_raw = base64.b64encode(input_raw)
    elif mode == Mode.Base32:
        output_raw = base64.b32encode(input_raw)
    elif mode == Mode.Base16:
        output_raw = input_raw.hex().encode()
    elif mode == Mode.Base2:
        output_raw = bytes_to_binstr(input_raw)
    elif mode == Mode.URL:
        output_raw = quote_from_bytes(input_raw).encode()
    elif mode == Mode.ESCAPE:
        output_raw = codecs.escape_encode(input_raw)[0]
    else:
        raise ValueError("Invalid mode chosen.")

    return output_raw


def decode(input_raw, mode):
    if mode == Mode.Base64:
        output_raw = base64.b64decode(input_raw)
    elif mode == Mode.Base32:
        output_raw = base64.b32decode(input_raw)
    elif mode == Mode.Base16:
        output_raw = bytes.fromhex(input_raw.decode())
    elif mode == Mode.Base2:
        output_raw = binstr_to_bytes(input_raw)
    elif mode == Mode.URL:
        output_raw = unquote_to_bytes(input_raw)
    elif mode == Mode.ESCAPE:
        output_raw = codecs.escape_decode(input_raw)[0]
    else:
        raise ValueError("Invalid mode chosen.")

    return output_raw


def main():
    args = arg_parser.parse_args()
    input_raw = args.infile.read()

    mode = args.mode or Mode.Base16

    if args.d or "decode" in sys.argv[0]:
        output_raw = decode(input_raw, mode)
    else:
        output_raw = encode(input_raw, mode)

    args.outfile.write(output_raw)


if __name__ == '__main__':
    main()
