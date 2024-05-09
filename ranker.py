"""
Group: 2
Names: Tiemen De Raedt, Siebe Vandewalle, Wolf De Waele

Template for ranker. 
"""

from binarytree import BinaryTree
from bktree import BKTree

class Ranker():

    avltree: BinaryTree
    bktree: BKTree

    def __init__(self, avltree: BinaryTree, bktree: BKTree) -> None:
        """
        :param BinaryTree binary_search_tree: Initialized binary search tree, mapping title words to book IDs.
        :param BKTree bk_tree: Initialized BK tree.
        """
        self.avltree = avltree
        self.bktree = bktree


    def get_ranking(self, tokenized_query: list, string_matching_threshold: int) -> dict:
        """
        Get a ranking of matching books IDs based on a query.

        :param list tokenized_query: Tokenized query = list of book titles
        :param int string_matching_threshold: Threshold to respect when matching words.
        :return: Collected results.
        """

        avltree = self.avltree
        bktree  = self.bktree

        results = []
        for title in tokenized_query:
            matching_values_distances = bktree.get(title, string_matching_threshold)
            for value_distance in matching_values_distances:
                ids = avltree.get(value_distance[0])
                for id in ids:
                    if id not in [value[0] for value in results]:
                        results.append((id,value_distance[1]))
        return sorted(results, key = lambda t: t[1])


"""
        results = {}
        for title in tokenized_query:
            matching_values_distances = bktree.get(title, string_matching_threshold)
            dict = {}
            for value_distance in matching_values_distances:
                if value_distance[0] not in [value[0] for value in dict.values()]:
                    dict[value_distance[0]] = (avltree.get(value_distance[0]),value_distance[1])
            results[title] = dict

        return results


# test
from avltree import AVLTree
from levenshtein import lev
from bktree import BKTree

avltree = BinaryTree()
bktree = BKTree(lev)

# add some values to the avltree
avltree.insert("hello", 1)
avltree.insert("world", 2)
avltree.insert("python", 3)
avltree.insert("java", 4)
avltree.insert("c++", 5)
avltree.insert("c#", 6)
avltree.insert("javascript", 7)
avltree.insert("html", 8)
avltree.insert("css", 9)
avltree.insert("php", 10)

# add some values to the bktree
bktree.insert("hello")
bktree.insert("world")
bktree.insert("python")
bktree.insert("java")
bktree.insert("c++")
bktree.insert("c#")
bktree.insert("javascript")
bktree.insert("html")
bktree.insert("css")
bktree.insert("php")

ranker = Ranker(avltree, bktree)

result = ranker.get_ranking(["hello", "world", "python"], 4)
for title in result:
    print(title)
    for value in result[title]:
        print(value, result[title][value])
    print()

"""