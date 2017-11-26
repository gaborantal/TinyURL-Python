import tinyurl
import unittest


class ShortenLive(unittest.TestCase):
    def testUrl(self):
        result = tinyurl.shorten("http://google.com", "really_tiny_url_google")
        self.assertEqual("http://tinyurl.com/really-tiny-url-google", result)

    def testAlreadyAssignedTinyUrl(self):
        result = tinyurl.shorten("NOTgoogle.com", "really_tiny_url_google")
        self.assertEqual("Alias you have selected is already used by someone else.", result)

if __name__ == '__main__':
    unittest.main()
