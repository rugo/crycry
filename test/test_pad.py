import unittest
from crycry.pad import pad


class TestPad(unittest.TestCase):

    def run_cases(self, testcases, bs):
        for testcase in testcases:
            self.assertEqual(
                pad(testcase[0], bs),
                testcase[1]
            )

    def test_aes(self):
        testcases = ((b'', b'\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'),
                     (b'A', b'A\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'),
                     (b'AA', b'AA\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'),
                     (b'AAA', b'AAA\r\r\r\r\r\r\r\r\r\r\r\r\r'),
                     (b'AAAA', b'AAAA\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'),
                     (b'AAAAA', b'AAAAA\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'),
                     (b'AAAAAA', b'AAAAAA\n\n\n\n\n\n\n\n\n\n'),
                     (b'AAAAAAA', b'AAAAAAA\t\t\t\t\t\t\t\t\t'),
                     (b'AAAAAAAA', b'AAAAAAAA\x08\x08\x08\x08\x08\x08\x08\x08'),
                     (b'AAAAAAAAA', b'AAAAAAAAA\x07\x07\x07\x07\x07\x07\x07'),
                     (b'AAAAAAAAAA', b'AAAAAAAAAA\x06\x06\x06\x06\x06\x06'),
                     (b'AAAAAAAAAAA', b'AAAAAAAAAAA\x05\x05\x05\x05\x05'),
                     (b'AAAAAAAAAAAA', b'AAAAAAAAAAAA\x04\x04\x04\x04'),
                     (b'AAAAAAAAAAAAA', b'AAAAAAAAAAAAA\x03\x03\x03'),
                     (b'AAAAAAAAAAAAAA', b'AAAAAAAAAAAAAA\x02\x02'),
                     (b'AAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAA\x01'),
                     (b'AAAAAAAAAAAAAAAA',
                      b'AAAAAAAAAAAAAAAA\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'),
                     (b'AAAAAAAAAAAAAAAAA',
                      b'AAAAAAAAAAAAAAAAA\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'),
                     (b'AAAAAAAAAAAAAAAAAA',
                      b'AAAAAAAAAAAAAAAAAA\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'),
                     (b'AAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAA\r\r\r\r\r\r\r\r\r\r\r\r\r'),
                     (b'AAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAA\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'),
                     (b'AAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAA\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'),
                     (b'AAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAA\n\n\n\n\n\n\n\n\n\n'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAA\t\t\t\t\t\t\t\t\t'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAA\x08\x08\x08\x08\x08\x08\x08\x08'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAA\x07\x07\x07\x07\x07\x07\x07'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAAA\x06\x06\x06\x06\x06\x06'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAAAA\x05\x05\x05\x05\x05'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAAAAA\x04\x04\x04\x04'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x03\x03\x03'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x02\x02'),
                     (b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x01'),)

        self.run_cases(testcases, 16)

    def test_shortblock(self):
        testcases = ((b'', b'\x05\x05\x05\x05\x05'),
                     (b'A', b'A\x04\x04\x04\x04'),
                     (b'AA', b'AA\x03\x03\x03'),
                     (b'AAA', b'AAA\x02\x02'),
                     (b'AAAA', b'AAAA\x01'),
                     (b'AAAAA', b'AAAAA\x05\x05\x05\x05\x05'),
                     (b'AAAAAA', b'AAAAAA\x04\x04\x04\x04'),
                     (b'AAAAAAA', b'AAAAAAA\x03\x03\x03'),
                     (b'AAAAAAAA', b'AAAAAAAA\x02\x02'),
                     (b'AAAAAAAAA', b'AAAAAAAAA\x01'))

        self.run_cases(testcases, 5)

    def test_singlebyte(self):
        testcases = ((b'', b'\x01'),
                     (b'A', b'A\x01'),
                     (b'AA', b'AA\x01'),
                     (b'AAA', b'AAA\x01'),
                     (b'AAAA', b'AAAA\x01'),
                     (b'AAAAA', b'AAAAA\x01'),
                     (b'AAAAAA', b'AAAAAA\x01'),
                     (b'AAAAAAA', b'AAAAAAA\x01'),
                     (b'AAAAAAAA', b'AAAAAAAA\x01'),
                     (b'AAAAAAAAA', b'AAAAAAAAA\x01'))

        self.run_cases(testcases, 1)
