"""
Group: 2
Names: Tiemen De Raedt, Siebe Vandewalle, Wolf De Waele

Template for AVL Binary Search Tree with persistent height information implementation. 
NOTE: The class AVLTreeX1 inherrits from AVLTree.
NOTE: A new node class is defined, which inherits from BinaryTreeNode. 
"""

from avltree import AVLTree, BinaryTreeNode

class AVLTreeNode(BinaryTreeNode):
    height: int

    def __init__(self, key: str, id: int) -> None:
        super().__init__(key, id)
        self.height = 1


class AVLTreeX1(AVLTree):

    def __init__(self) -> None:
        super().__init__()
        self.NodeType = AVLTreeNode

    def _calc_node_height(self, node: AVLTreeNode) -> int:
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        elif node.left is None:
            return 1 + node.right.height
        elif node.right is None:
            return 1 + node.left.height
        else:
            return 1 + max(node.left.height,node.right.height)
        """
        Calculates the height of a node. Overridden method.

        :param AVLTreeNodeX1 node: The node to calculate the height of.
        :return int: The height of the node.
        """

    def _find_balance(self, node: AVLTreeNode) -> int:
        if node.left is None and node.right is None:
            return 0
        if node.left is None:
            return -1*(node.right.height)

        if node.right is None:
            return node.left.height
        
        else: return node.left.height - node.right.height
        """
        Calculates the balance of a node. Overridden method.

        :param AVLTreeNodeX1 node: Node to calculate the balance of.
        :return int: The balance of the node.
        """

    def _insert(self, node: AVLTreeNode, key: str, value) -> AVLTreeNode:
        node = super()._insert(node, key, value)

        if not isinstance(node, AVLTreeNode):
            avl_node = AVLTreeNode(node.key, node.values[0])
            avl_node.left = node.left
            avl_node.right = node.right
            node = avl_node

        node.height = self._calc_node_height(node)
        return node

        """
        Overridden recursive insertion method.

        :param AVLTreeNodeX1 node: Current node to evaluate.
        :param str key: Key in tree.
        :param int value: Value to add.
        :return AVLTreeNodeX1: Current node.
        """        
    def _right_rotate(self, old_root: AVLTreeNode) -> AVLTreeNode:
        new_root = super()._right_rotate(old_root)

        old_root.height -= 1
        new_root.height += 1
        return new_root
        """
        Perform a right rotate for the subtree. Overridden method.

        :param AVLTreeNodeX1 old_root: The current root for the subtree.
        :return AVLTreeNodeX1: The root of the subtree after rotation.
        """  

    def _left_rotate(self, old_root: AVLTreeNode) -> AVLTreeNode:
        new_root = super()._left_rotate(old_root)

        old_root.height -= 1
        new_root.height += 1
        return new_root
        """
        Perform a left rotate for the subtree. Overridden method.

        :param AVLTreeNodeX1 old_root: The current root for the subtree.
        :return AVLTreeNodeX1: The root of the subtree after rotation.
        """