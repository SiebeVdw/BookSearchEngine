"""
Group: 2
Names: Tiemen De Raedt, Siebe Vandewalle, Wolf De Waele

Template for AVL Binary Search Tree implementation. 
NOTE: The class AVLTree inherrits from BinaryTree.
"""

from binarytree import BinaryTree, BinaryTreeNode

class AVLTree(BinaryTree):

    def __init__(self) -> None:
        super().__init__()

    def _insert(self, node: BinaryTreeNode, key: str, value: int) -> BinaryTreeNode:
        """
        Overridden recursive insertion method.
        Calls `_rebalance` on the way up.

        :param BinaryTreeNode node: Current node to evaluate.
        :param str key: Key in tree.
        :param int value: Value to add.
        :return BinaryTreeNode: Current node.
        """
        node = super()._insert(node, key, value)
        node = self._rebalance(node, key)
        return node

    def _calc_node_height(self, node: BinaryTreeNode) -> int:
        if node is None:
            return 0
        else:
            return 1+max(self._calc_node_height(node.left),self._calc_node_height(node.right))

        """
        Recursive calculation of the height of a node.

        :param BinaryTreeNode node: Node to calculate height of.
        :return int: The height of the node.
        """

    def _find_balance(self, node: BinaryTreeNode) -> int:
        return self._calc_node_height(node.left)-self._calc_node_height(node.right)
        """
        Calculates the balance of a node.

        :param BinaryTreeNode node: Node to calculate the balance of.
        :return int: The balance of the node.
        """

    def _rebalance(self, node: BinaryTreeNode, key: str) -> BinaryTreeNode:
        balance = self._find_balance(node)
        # balance < -1 : right subtree > left subtree
        if balance <-1:
            # when inserting as a right child of the right subtree, perform a left rotation
            # then we skip the if statement. 
            if key < node.right.key:
                node.right = self._right_rotate(node.right)
            node = self._left_rotate(node)
        # balance > 1 : left subtree > right subtree
        elif balance > 1:
            if key > node.left.key:
                node.left = self._left_rotate(node.left)
            node = self._right_rotate(node)
        return node
        """
        Rebalance the subtree when necessary.

        :param BinaryTreeNode node: The current node, the root of the subtree. In example slides (37) : node with key 5
        :param str key: The key of the last-inserted node. In example slides (37) : node with key 8
        :return BinaryTreeNode: The (new) root of the subtree.
        """

    def _right_rotate(self, old_root: BinaryTreeNode) -> BinaryTreeNode:
        new_root = old_root.left
        old_root.left = new_root.right
        new_root.right = old_root
        return new_root
        """
        Perform a right rotate for the subtree.

        :param BinaryTreeNode old_root: The current root for the subtree.
        :return BinaryTreeNode: The root of the subtree after rotation.
        """

    def _left_rotate(self, old_root: BinaryTreeNode) -> BinaryTreeNode:
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left = old_root
        return new_root
        """
        Perform a left rotate for the subtree.

        :param BinaryTreeNode old_root: The current root for the subtree.
        :return BinaryTreeNode: The root of the subtree after rotation.
        """