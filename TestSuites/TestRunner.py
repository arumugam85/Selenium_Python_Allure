from unittest import TestSuite, TextTestRunner
from unittest.loader import TestLoader

from testCases.test_addCustomer import Test_002_AddCustomer
from testCases.test_login import Test_001_Login
from testCases.test_login_ddt import Test_002_DDT_Login
from utilities.readProperties import ReadConfig

if __name__ == "__main__":
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Test_001_Login),
        loader.loadTestsFromTestCase(Test_002_DDT_Login),
        loader.loadTestsFromTestCase(Test_002_AddCustomer)

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
