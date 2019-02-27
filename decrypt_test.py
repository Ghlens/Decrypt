import unittest
from textDecrypt import decrypt

class TestDecrypt(unittest.TestCase):
    """
    Basic test for decrypt application
    """

    def test_decrypt(self):
        res = decrypt("Everything is fine")
        self.assertEqual(''.join(res), "Everything is fine")

if __name__ == '__main__':
    unittest.main()
