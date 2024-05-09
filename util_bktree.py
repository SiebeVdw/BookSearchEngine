import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

from binarytree import BinaryTreeNode
from bktree import BKTreeNode

class TextProcessor():
    def __init__(self):
        """
        Set up text processing.
        """
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('words', quiet=True)
        
        self._character_pattern = re.compile('[\\W_]+')
        self._stop_words = set(stopwords.words('english'))

    def process(self, string: str) -> list:
        """
        Process a string into a tokenized bag-of-words.

        :param str string: Input string to process.
        :return list: Bag-of-words.
        """
        # remove capital letters
        string = string.casefold()
        
        # split sentence into tokens
        string = word_tokenize(string)
        
        # remove non-alphanumeric characters
        string = [self._character_pattern.sub('', token) for token in string]
        
        # filter empty tokens
        string = list(filter(None, string))
        
        # remove stop words
        string = [token for token in string if token not in self._stop_words]
                
        # return processed input as List of unique tokens
        return list(set(string))


class Dataset():
    def __init__(self, csv_file: str, number_of_titles_to_load: int = -1):
        """
        Utility class to easily load the data.
        """
        import csv
        self._books = []
        with open(csv_file) as file:
            contents = csv.DictReader(file, delimiter=',', quotechar='"')
            for i, entry in enumerate(contents): 
                if number_of_titles_to_load > -1 and i > number_of_titles_to_load: break
                entry['ID'] = i
                self._books.append(entry)

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        for e in self._books:
            yield e

    def get_book(self, book_id: int) -> dict:
        """
        Retrieve the book entry for a given ID.

        :param int book_id: The book ID.
        :return dict: Inforamation on the book.
        """
        return self._books[book_id]


def bst_traversal(node: BinaryTreeNode, result_out: list):
    """
    Utility function to check structure of Binary Search Tree in tests.
    """
    if node is None: return
    else:
        result_out.append((node.key, (sorted(node.values))))
        bst_traversal(node.left, result_out)
        bst_traversal(node.right, result_out)
    

def bkt_traversal(node: BKTreeNode, result_out: list):
    """
    Utility function to check structure of BK Tree during tests.
    """
    if node is None: return
    else:
        result_out.append(node.value)
        for d in node.get_distances_of_children():
            result_out.append(str(d))
            bkt_traversal(node.get_child(d), result_out)


def main():
    tp = TextProcessor()
    print(tp.process("The wolves are returning to nature"))

if __name__ == "__main__":
    main()