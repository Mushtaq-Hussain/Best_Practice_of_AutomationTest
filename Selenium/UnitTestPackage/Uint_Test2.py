import unittest


class UnitTest2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("Class 1 --> Class level SetUp")
        print("*#" * 30)

    def setUp(self):
        print("Class 1 -->SetUp")

    def test_methodA(self):
        print("Class 1 --> Running Method A")

    def test_methodB(self):
        print("Class 1 --> Running Method B")

    def tearDown(self):
        print("Class 1 --> tearDown")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("Class 1 --> Class level tearDown")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
