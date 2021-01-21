import unittest


class UnitTest1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("I will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("I will run once before each test")

    def test_methodA(self):
        print("Running Method A")

    def test_methodB(self):
        print("Running Method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)