"""
Run script to test BK Tree implementation. 
NOTE: Uncomment last line to evaluate BK tree using Dynamic Programming implementation of Levenshtein distance
"""

import time
import pickle   
test_data = pickle.load(open('testdata2.p', 'rb'))
test_data = test_data['bkt']

from util_bktree import bkt_traversal

from levenshtein import lev, lev_dp
from bktree import BKTree


def test_bk(tree):
    timer = time.perf_counter()
    # Construct tree from 512 elements
    for key in test_data['in_key']: tree.insert(key)
    # Retrieve 512 elements
    r_output = [tree.get(k, d) for k,d in zip(test_data['get_key'],test_data['get_dist'])] 
    timer = time.perf_counter() - timer

    bkt_traversal(tree._root, c_output := [])
    print(tree.__class__.__name__, tree._distance_function.__name__, 
          "\tStructure:", c_output == test_data['structure'], 
          "  \tRetrieval:", r_output == test_data['get_out'],
          "  \tT:", round(timer, 6), "s")

if __name__ == "__main__":
    # test_bk(BKTree(lev))
    test_bk(BKTree(lev_dp))     # NOTE: Uncomment to evaluate BK tree with lev_dp
