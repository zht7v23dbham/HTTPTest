import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    for i in  range(10):

        print i

if __name__ == '__main__':
    unittest.main()
