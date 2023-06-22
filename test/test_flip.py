import unittest
from crycry import flip


class TestBase32(unittest.TestCase):

    def test_bits(self):
        a = [(2**i).to_bytes(1) for i in range(7, -1, -1)]
        b = b"\x00"

        for i in range(7, -1, -1):
            res = flip.flip(b, 0, i)
            self.assertEqual(res, a[i])

    def test_vectors(self):
        a = b"\xff\xfe\xaf\xfe"
        a_msb_flipped = b"\x7f\xfe\xaf\xfe"
        a_lsb_flipped = b"\xff\xfe\xaf\xff"
        a_middle_flipped = b"\xff\xee\xaf\xfe"

        self.assertEqual(
            flip.flip(a, 0, 0), a_msb_flipped
        )

        self.assertEqual(
            flip.flip(a, len(a) - 1, 7), a_lsb_flipped
        )

        self.assertEqual(
            flip.flip(a, 1, 3), a_middle_flipped
        )

