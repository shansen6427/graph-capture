import os
import sys
import unittest

class ERROR_CODES:
    OK = 0
    TESTS_FAILED = 1

def main():
    sys.path.append(os.path.abspath('game'))
    suite = unittest.TestLoader().discover("tests", pattern = "test_*.py")
    runner = unittest.TextTestRunner(verbosity = 2, buffer = True)
    result = runner.run(suite) 
    if result.wasSuccessful():
        return ERROR_CODES.OK
    return ERROR_CODES.TESTS_FAILED

if __name__=='__main__':
    main()
