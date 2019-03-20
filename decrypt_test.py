import unittest
import time
from textDecrypt import decrypt

class TestDecrypt(unittest.TestCase):
    """
    Basic test for decrypt application
    """

    def test_decrypt(self):
        start = time.clock()
        res = decrypt("Everything is fine")
        self.assertEqual(''.join(res), "Everything is fine")
        print(time.clock() - start)

if __name__ == '__main__':
    unittest.main()
