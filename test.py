import unittest
from helper import get_long_url, get_url_usage,create_hash

class TestStringMethods(unittest.TestCase):

    def test_create_hash(self):
        self.assertIsNotNone(create_hash('test_url_1234567890','test_user'))

    def test_invalid_long_url(self):
        with self.assertRaises(KeyError):
            get_long_url('abc')
    
    def test_create_valid(self):
        test_short_url = create_hash('test_url_012345689','test_user')
        self.assertEqual(get_long_url(test_short_url),'test_url_012345689')

    
    def test_increments_count(self):
        test_count = get_url_usage(test_short_url)['used_count']
        get_long_url(test_short_url)
        self.assertEqual(get_url_usage(test_short_url)['used_count'],test_count+1)


if __name__ == '__main__':
    unittest.main()