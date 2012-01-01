#Percentages from http://www.exrx.net/Calculators/OneRepMax.html

BRZYCKI = {"1":  100,
           "2":   95,
           "3":   90,
           "4":   88,
           "5":   86,
           "6":   83,
           "7":   80,
           "8":   78,
           "9":   76,
           "10":  75,
           "11":  72,
           "12":  70}

BEACHLE = {"1":  100,
           "2":   95,
           "3":   93,
           "4":   90,
           "5":   87,
           "6":   85,
           "7":   83,
           "8":   80,
           "9":   77,
           "10":  75,
           "11":  75,
           "12":  67,
           "13":  65}

DOSREMEDIOS = {"1":  100,
               "2":   92,
               "3":   90,
               "4":   87,
               "5":   85,
               "6":   82,
               "7":   82,
               "8":   75,
               "9":   75,
               "10":  70,
               "11":  70,
               "12":  65,
               "13":  60}

maxComputeMethod = BRZYCKI
           
def compute1rm(set, old1rm=0):
    """Compute the 1rm for this exercise.

    set = iterator of the current set.  Needs to have reps and weight
          as available variables
    old1rm = the current 1rm

    Usage
    >>> set = _Set()
    >>> set.reps = 4
    >>> set.weight = 100
    >>> compute1rm(set)
    88.0

    >>> compute1rm(set, 4)
    88.0

    """
    newMax = old1rm
    reps = str(set.reps)

    if set.reps < 1:
        #0 reps - return old1rm
        return old1rm
    elif reps not in maxComputeMethod.keys():
        #Reps are not in the dictionary, return the larger of the
        #older max and whatever was done in this set
        return max((old1rm, set.weight))

    thisMax = .01 * set.weight * maxComputeMethod[reps]
        
    if thisMax > newMax:
        newMax = thisMax
            
    if newMax > 0:
        return newMax
    else:
        return set.weight

class _Set(object):
    reps = 0
    weight = 0

if "__main__" == __name__:
    import doctest
    doctest.testmod()
