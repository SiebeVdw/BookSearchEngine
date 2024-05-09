"""
Run script to test Levenshtein distance implementation. 
NOTE: Uncomment last line to evaluate Dynamic Programming implementation of Levenshtein distance
"""

import time
import pickle   
test_data = pickle.load(open('testdata2.p', 'rb'))
test_data = test_data['lev']

from levenshtein import lev, lev_dp

def test_levenshtein(lev_fn):
    test_passed = True

    # Matching 4096 strings
    dtimer = time.perf_counter()
    for i,x in enumerate(test_data["in_mat"]):
        for j,y in enumerate(test_data["in_mat"]):
            test_passed = (lev_fn(x, y) == test_data["out_mat"][i][j])
            if not test_passed: break
    dtimer = time.perf_counter() - dtimer

    print(lev_fn.__name__, 
          "    \tDistances:", test_passed,
          "    \tT Calculation:", round(dtimer, 6), "s")

if __name__ == "__main__":
    # test_levenshtein(lev)
    test_levenshtein(lev_dp)    # NOTE: Uncomment to evaluate lev_dp