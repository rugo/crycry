import unittest

from crycry import encoder


class EncoderTest:
    def encode_func(self, inp):
        return encoder.encode(inp, self.mode)

    def decode_func(self, inp):
        return encoder.decode(inp, self.mode)

    def test_encode(self):
        for plain, enc in self.testcases:
            self.assertEqual(self.encode_func(plain), enc)

    def test_decode(self):
        for plain, enc in self.testcases:
            self.assertEqual(self.decode_func(enc), plain)

    def test_encode_decode(self):
        for plain, enc in self.testcases:
            self.assertEqual(self.decode_func(self.encode_func(plain)), plain)


class TestBase16(EncoderTest, unittest.TestCase):
    def setUp(self):
        self.mode = encoder.Mode.Base16
        self.testcases = [
            (b"\xaf\xfe" * 10, b"affe" * 10),
            (b"\x00" * 17, b"00" * 17)
        ]


class TestBase32(EncoderTest, unittest.TestCase):
    def setUp(self):
        self.mode = encoder.Mode.Base32
        self.testcases = [
            (b"yolo123", b"PFXWY3ZRGIZQ===="),
            (b"yolo12", b"PFXWY3ZRGI======")
        ]


class TestBase64(EncoderTest, unittest.TestCase):
    def setUp(self):
        self.mode = encoder.Mode.Base64
        self.testcases = [
            (b"You make me feel good", b"WW91IG1ha2UgbWUgZmVlbCBnb29k"),
            (b"You make me feel goo", b"WW91IG1ha2UgbWUgZmVlbCBnb28="),
            (b"You make me feel go", b"WW91IG1ha2UgbWUgZmVlbCBnbw==")
        ]


class TestBase2(EncoderTest, unittest.TestCase):
    def setUp(self):
        self.mode = encoder.Mode.Base2
        self.testcases = [
            (b"Hallo was geht bei dir?", b"010010000110000101101100011011000110111100100000011101110110000101110011001"
                                         b"000000110011101100101011010000111010000100000011000100110010101101001001000"
                                         b"0001100100011010010111001000111111"),
            (b"AA", b"0100000101000001"),
        ]

    def test_whitespace(self):
        a = b"Hallo was geht bei dir?"
        b = b"01001000 01100001 01101100 01101100 01101111 00100000 01110111 01100001" \
            b"01110011 00100000 01100111 01100101 01101000 01110100 00100000 01100010" \
            b"01100101 01101001 00100000 01100100 01101001 01110010 00111111"

        self.assertEqual(
            encoder.binstr_to_bytes(b),
            a
        )

    def test_bad_len(self):
        with self.assertRaises(ValueError):
            encoder.binstr_to_bytes(b"1" * 7)


if __name__ == "__main__":
    unittest.main()
