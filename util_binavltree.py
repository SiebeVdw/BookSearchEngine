from binarytree import BinaryTreeNode

def bst_traversal(node: BinaryTreeNode, result_out: list):
    """
    Utility function to check structure of Binary Search Tree in tests.
    """
    if node is None: return
    else:
        result_out.append((node.key, (sorted(node.values))))
        bst_traversal(node.left, result_out)
        bst_traversal(node.right, result_out)

