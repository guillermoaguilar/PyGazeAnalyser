# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:45:32 2015

@author: guille
"""

import unittest
import sys
sys.path.append('../')
from edfreader import read_edf



class TestEDFReader(unittest.TestCase):

    def test_read_starttime(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK')
        self.assertEqual(d[0]['trackertime'][0], 261291)


    def test_read_xy_starttime_lefteye(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK')

        self.assertEqual(d[0]['x'][0], -423.1)
        self.assertEqual(d[0]['y'][0], 772.7)
        self.assertNotEqual(d[0]['x'][0], 0.0)
        self.assertNotEqual(d[0]['y'][0], 0.0)


    def test_read_xy_starttime_righteye(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='R')

        self.assertEqual(d[0]['x'][0], -537.5)
        self.assertEqual(d[0]['y'][0], 597.9)
        self.assertNotEqual(d[0]['x'][0], 0.0)
        self.assertNotEqual(d[0]['y'][0], 0.0)


    def test_first_fixation(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK')
        self.assertEqual(d[0]['events']['Sfix'][0], 261298)


    def test_end_last_fixation(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='L')
        self.assertEqual(d[0]['events']['Efix'][-1][0], 265850)

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='R')
        self.assertEqual(d[0]['events']['Efix'][-1][0], 265833)


    def test_first_blink(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='L')
        self.assertEqual(d[0]['events']['Sblk'][0], 261423)

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='R')
        self.assertEqual(d[0]['events']['Sblk'][0], 261447)


    def test_end_last_saccade(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='L')
        self.assertEqual(d[0]['events']['Esac'][-1][0], 265599)

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='R')
        self.assertEqual(d[0]['events']['Esac'][-1][0], 265613)


    def test_numberoffixations(self):

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='L')
        self.assertEqual(len(d[0]['events']['Efix']), 16)

        d = read_edf('test.asc', start='TRIALID', stop='TRIAL OK', eye='R')
        self.assertEqual(len(d[0]['events']['Efix']), 17)

if __name__ == '__main__':
    unittest.main()
