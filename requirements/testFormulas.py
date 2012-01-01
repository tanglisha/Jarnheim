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
        """Sanity check:
        0 reps should return whatever the old rep max was.
        The set is considered incomplete.
        """
        self.set.reps = 0
        new1rm = compute1rm(self.set)
        self.assertEqual(new1rm, 0, "1rm should be 0 - set was not completed")
        newer1rm = compute1rm(self.set, 100)
        self.assertEqual(newer1rm, 100, "1rm should remain 100")

    def test1rep(self):
        """Sanity check:
        1 rep will always change the max to that weight if it's
        more than the old 1rm.  If it's not, the 1rm remains
        unchanged.
        """
        self.set.reps = 1
        new1rm = compute1rm(self.set, 100)
        self.assertEqual(new1rm, 100, "1rm should remain 100")
        newer1rm = compute1rm(self.set, 99)
        self.assertEqual(newer1rm, 100, "1rm should now be 100")
        
    def testSeveralReps(self):
        """Formula check"""
        maxComputedMethod = BRZYCKI
        self.set.reps = 2
        twoRepsMax = compute1rm(self.set)
        self.assertEqual(twoRepsMax, 95, "1rm should now be 95")

    def testWayTooManyReps(self):
        """Sanity check:
        Lots of reps means the calculators become fairly useless.
        We can go ahead and change the max to whatever was done,
        but there's no real value in trying to figure out what the
        max would be.
        """
        self.set.reps = 200
        twohundredRepsMax = compute1rm(self.set)
        self.assertEqual(twohundredRepsMax, 100, "1rm should now be 100")

if "__main__" == __name__:
    unittest.main()
