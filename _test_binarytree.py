"""
Run script to test Binary Tree implementation. 
"""

import pickle   
test_data = pickle.load(open('testdata1.p', 'rb'))
test_data = test_data['bst']

from util_binavltree import bst_traversal

from binarytree import BinaryTree

def test_binary_search(tree):
    # Construct tree from 10.000 elements
    for key, id in zip(test_data['in_key'], test_data['in_value']): tree.insert(key, id)
    bst_traversal(tree._root, c_output := [])
    
    # Retrieve 40.000 elements
    r_output = [tree.get(key) for key in test_data['get_key']]

    print(tree.__class__.__name__, 
          "\tBST Structure:", c_output == test_data['structure_bst'], 
          "\tBST Retrieval:", r_output == test_data['get_out'])

if __name__ == "__main__":
    test_binary_search(BinaryTree())
