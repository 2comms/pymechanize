import unittest

import pymechanize
from pymechanize.testcase import TestCase


class ImportTests(TestCase):

    def test_import_all(self):
        for name in pymechanize.__all__:
            exec("from pymechanize import %s" % name)


if __name__ == "__main__":
    unittest.main()
