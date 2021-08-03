import os
import sys
import pstats
import cProfile
from functools import reduce

sys.path.append(os.path.abspath("."))

from fold_tools import fold



def f8(x):
    """
    A simple monkeypath for the pstats module to be able to see sub-millisecond timings
    Source: https://gist.github.com/romuald/0346c76cfbbbceb3e4d1
    """
    ret = "%8.3f" % x
    if ret != '   0.000':
        return ret
    return "%6dµs" % (x * 10000000)

pstats.f8 = f8

print(cProfile.run("fold(max, [1,2,3],0)"))
print(cProfile.run("reduce(max, [1,2,3],0)"))
