"""
Group: 2
Names: Tiemen De Raedt, Siebe Vandewalle, Wolf De Waele

Template for BK-Tree implementation. 
NOTE: The function for the distance can be given upon initialization of the BK-Tree. 
      For the project, this will be `lev(a, b)` or `lev_dp(a, b)`.
"""

class BKTreeNode():

    value: str
    _children: dict

    def __init__(self, value: str) -> None:
        self.value = value
        self._children = {}

    def get_distances_of_children(self) -> list:
        """
        Return the distances for which this node has children.

        :return list: Sorted list of distances.
        """
        return sorted(list(self._children.keys()))

    def get_child(self, distance: int) -> "BKTreeNode":
        """
        Return the child for a certain distance

        :param int distance: Distance to the child to retrieve.
        :return BKTreeNode: The child.
        """
        return self._children.get(distance, None)

    def set_child(self, distance: int, child: "BKTreeNode") -> None:
        """
        Add a child to the node.

        :param int distance: The distance to the child.
        :param BKTreeNode child: The child.
        """
        self._children[distance] = child


class BKTree():

    _root: BKTreeNode
    _distance_function = None

    def __init__(self, distance_function: callable) -> None:
        """
        :param callable distance_function: The function to calculate the distance between two strings. 
        """
        self._root = None
        self._distance_function = distance_function

    def get(self, query_word:str, thresh: int = 1) -> list:
        """
        Method to retrieve matches for a query word.
        Call recursive method `_get`.
        
        :param str query_word: The query word.
        :param int thresh: The threshold to respect, defaults to 1
        :return list: List of tuples (v, d) for values matching the query, 
                      where v is the value matching the query q, and d is the distance from k to q.
        """
        retval = self._get(self._root, query_word, thresh)
        return sorted(sorted(retval), key=lambda t: t[1])

    def _get(self, node: BKTreeNode, query: str, thresh: int) -> list:
        if not thresh:
            return [(query,thresh)]
        lijst = []
        distance = self._distance_function(node.value,query)
        if distance <= thresh:
            lijst.append((node.value,distance))
        for distance_kind in list(node._children):
            if (distance_kind  <= distance + thresh and distance_kind >= distance - thresh):
                lijst += self._get(node.get_child(distance_kind),query,thresh)
        return lijst

        """
        Recursive get method.

        :param BKTreeNode node: The current node to evaluate.
        :param str query: The query word.
        :param int thresh: The threshold to respect.
        :return list: List of tuples (v, d) for values matching the query, 
                      where v is the value matching the query q, and d is the distance from k to q.
        """
        raise NotImplementedError # TODO: Complete recursive get.

    def insert(self, value: str) -> None:
        """
        Method to insert a new value into the tree.

        :param str value: Value to insert.
        """
        if self._root is None: self._root = BKTreeNode(value)
        else: self._root = self._insert(self._root, value)

    def _insert(self, node: BKTreeNode, value: str) -> BKTreeNode:
        distance = self._distance_function(node.value,value)
        if not distance:
            return node
        child = node.get_child(distance)
        if child:
            self._insert(child,value)
        else:
            node.set_child(distance,BKTreeNode(value))
        return node

        """
        Recursive insertion method.

        :param BKTreeNode node: Current node to evaluate.
        :param str value: Value to insert.
        :return BKTreeNode: Current node.
        """