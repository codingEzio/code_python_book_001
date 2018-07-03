from mypackage.mymathlib import *


# Since this test case was not mean to "fail"
#   except for the "nosetests FILENAME -v"
#   ya still need the param "-s"  (to show any printed stdout output)

math_obj = 0


def setUpModule():
    """called once, before anything else in this module"""
    print("In setUpModule()...")
    global math_obj
    math_obj = mymathlib()


def tearDownModule():
    """called once, after everything else in this module"""
    print("In tearDownModule()...")
    global math_obj
    del math_obj


class TestClass:

    @classmethod
    def setUpClass(cls):
        """called once, before any test in the class"""
        print("In setUpClass()...")

    def setUp(self):
        """called before every test method"""
        print("\nIn setUp()...")

    def test_case01(self):
        print("In test_case01()...")
        assert math_obj.add(2, 5) == 7

    def test_case02(self):
        print("In test_case02()...")

    def tearDown(self):
        """called after every test method"""
        print("\nIn tearDown()...")

    @classmethod
    def tearDownClass(cls):
        """called once, after all tests, if setUpClass() successful"""
        print("\nIn tearDownClass()...")
