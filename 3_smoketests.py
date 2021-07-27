# Archivo donde estar el Test Suite

from unittest import TestLoader, TestCase
from unittest.suite import TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchtest import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output":"smoke-report"
}
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
