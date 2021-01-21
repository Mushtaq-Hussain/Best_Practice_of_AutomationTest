import unittest


class AssertTest(unittest.TestCase):

    def test_assertTrueFalse(self):

        a = True
        self.assertTrue(a, "a is not false")
        b = False
        self.assertFalse(b, "b is not true")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, "a & b are Equal")


if __name__ == '__main__':
    unittest.main(verbosity=2)