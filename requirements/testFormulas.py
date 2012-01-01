import unittest
from formulas import *

class Set(object):
    reps = 0
    weight = 100

class TestCompute1rm(unittest.TestCase):

    def setUp(self):
        self.set = Set()
        self.set.reps = 1
        self.set.weight = 100

    def test0reps(self):
        self.set.reps = 0
        new1rm = compute1rm(self.set)
        self.assertEqual(new1rm, 0, "1rm should be 0 - set was not completed")
        newer1rm = compute1rm(self.set, 100)
        self.assertEqual(newer1rm, 100, "1rm should remain 100")

    def test1rep(self):
        self.set.reps = 1
        new1rm = compute1rm(self.set, 100)
        self.assertEqual(new1rm, 100, "1rm should remain 100")
        newer1rm = compute1rm(self.set, 99)
        self.assertEqual(newer1rm, 100, "1rm should now be 100")
        
    def testSeveralReps(self):
        maxComputedMethod = BRZYCKI
        self.set.reps = 2
        twoRepsMax = compute1rm(self.set)
        self.assertEqual(twoRepsMax, 95, "1rm should now be 95")

if "__main__" == __name__:
    unittest.main()
