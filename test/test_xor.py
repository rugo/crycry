import unittest
from crycry.xor import xor


class TestBase32(unittest.TestCase):

    def test_properties(self):
        a = b"\xaf\xaf"
        b = b"KA"
        self.assertEqual(xor(a, a), b"\x00\x00")
        self.assertEqual(xor(a, xor(a, b)), b)
        self.assertEqual(xor(a, b), xor(b, a))

    def test_keywrap(self):
        length = 20
        c = xor(b"A" * length, b"A")

        self.assertEqual(c, b"\x00" * length)

        c = xor(b"B" * length, b"AB")

        self.assertEqual(c, b"\x03\x00" * (length//2))
