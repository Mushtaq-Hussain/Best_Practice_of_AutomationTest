import unittest
from UnitTestPackage.Unit_Test1 import UnitTest1
from UnitTestPackage.Uint_Test2 import UnitTest2


tc1 = unittest.TestLoader().loadTestsFromTestCase(UnitTest1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(UnitTest2)

smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)