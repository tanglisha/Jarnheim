import unittest
from formulas import *

class Set(object):
    reps = 0
    weight = 100

class TestCalculateSetPoints(unittest.TestCase):

    def setup(self):
        self.set = Set()
        self.set.reps = 0
        self.set.weight = 100

    def test0reps(self):
        """0 reps should earn 0 points"""
        self.set.reps = 0
        points = calculateSetPoints(set, 45)
        self.assert(points, 0, "0 points should have been earned")

    def test1reps(self):
        """1 rep should earn the full amount"""
        self.set.reps = 1
        points = calculateSetPoints(set, 10)
        self.assert(points, 10, "10 points should have been earned")

    def test10reps(self):
        """10 reps should earn 10xpoints points"""
        self.set.reps = 10
        points = calculateSetPoints(set, 10)
        self.assert(points, 100, "100 points should have been earned")

    def test20reps(self):
        """20 reps should earn 10xpoints + 10xpoints/2 points"""
        self.set.reps = 20
        points = calculateSetPoints(set, 10)
        self.assert(points, 150, "150 points should have been earned")

    def test30reps(self):
        """30 reps should earn 20 reps points + 10xpoints/2/2
        points"""
        self.set.reps = 30
        points = calculateSetPoints(set, 10)
        self.assert(points, 170, "170 points should have been earned")

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
