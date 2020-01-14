#!/usr/bin/python3
import os
import sys
import unittest
import tempfile
# put '../..' in the lib search path so it can find this library
sys.path.insert(0, '..' + os.sep + '..')
from dataserve import DataContainer


# Dummpy class for holding some test data
class TestClass(object):
    CLASS_DATA_A = 'CLASS DATA NOT SAVED'
    def __init__(self):
        self.a  = 'saved data 1'
        delf._x = 'private data not saved by default'
    def method1(self):
        return 'method not saved'


class LemmatizerRulesTests(unittest.TestCase):

    def dc_load_save_test(self, fn):
        # Create some junk data to test load/save
        tc = TestClass()
        tc.b = ['saved data 2']
        # Create the data container and add some data to it
        dc1 = DataContainer()
        dc1.add_object_data(tc)
        dc1.c = {'x':'saved data 3'}
        # Save the data and reload it
        dc1.save(fn)
        dc2 = DataContainer(fn)
        # Test that everything was reloaded correctly
        self.assertEqual(len(vars(dc2)), 3)
        self.assertEqual('a' in vars(dc2), True)
        self.assertEqual('b' in vars(dc2), True)
        self.assertEqual('c' in vars(dc2), True)
        # remove the temporary file
        os.remove(fn)

    def getTestSaveLoad(self):
        # Test a basic pkl file
        fn = tempfile.mkstemp(suffix='.pkl')[1]
        self.dc_load_save_test(fn)
        # Test a gzipped file
        fn = tempfile.mkstemp(suffix='.pkl.gz')[1]
        self.dc_load_save_test(fn)


if __name__ == '__main__':
    # run all methods that start with 'test'
    unittest.main()
