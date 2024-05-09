"""
Run script to test AVL Tree implementation. 
NOTE: Uncomment last line to evaluate avltree_x1.py
"""

import time
import pickle   
test_data = pickle.load(open('testdata1.p', 'rb'))
test_data = test_data['bst']

from util_binavltree import bst_traversal

from binarytree import BinaryTree
from avltree import AVLTree
from avltree_x1 import AVLTreeX1


def test_avl(tree):
    # Construct tree from 10.000 elements
    ctimer = time.perf_counter()
    for key, id in zip(test_data['in_key'], test_data['in_value']): tree.insert(key, id)
    ctimer = time.perf_counter() - ctimer
    bst_traversal(tree._root, c_output := [])
    
    # Retrieve 40.000 elements
    rtimer = time.perf_counter()
    for key in test_data['get_key']: tree.get(key) 
    rtimer = time.perf_counter() -  rtimer

    print(tree.__class__.__name__, 
          "\tAVL Structure:", c_output == test_data['structure_avl'], 
          "  \tT Construct:", round(ctimer, 6), "s", 
          "  \tT Retrieve:", round(rtimer, 6), "s")

if __name__ == "__main__":
    test_avl(BinaryTree())
    test_avl(AVLTree())
    test_avl(AVLTreeX1())     # NOTE: Uncomment to evaluate avltree_x1.py
