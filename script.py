"""
Group: 2
Names: Tiemen De Raedt, Siebe Vandewalle, Wolf De Waele
"""

def main():
    import sys
    sys.setrecursionlimit(10000)
    from util_bktree import TextProcessor
    qp  = TextProcessor()
    s   = "This is some sample string"
    bow = qp.process(s)                             # NOTE: You can use the given method to process a sentence into a tokenized bag-of-words

    #from avltree import AVLTree 
    from avltree_x1 import AVLTreeX1 as AVLTree   # NOTE: Uncomment to use AVLTreeX1
    avltree = AVLTree()

    from bktree import BKTree
    #from levenshtein import lev
    from levenshtein import lev_dp as lev         # NOTE: Uncomment to use dynamic programming version of Levenshtein distance
    bktree = BKTree(lev)

    from util_bktree import Dataset
    dataset = Dataset("brooklyn_public_library_catalog_selected.csv", 10000)



    print("Indexing: Load in the data")

    # Easy iteration over dataset.
    for book in dataset:        
        book_id = book['ID']
        book_title = book['TITLE']
        
        tokenized_title = qp.process(book_title)   

        for word in tokenized_title:
            avltree.insert(word, book_id)                       # TODO: 1. Construct a binary search tree to map title words to book ID
            bktree.insert(word)                                 # TODO: 2. Construct a BK-tree to structure similar words.

    print("Indexing completed")


    print("Ranking: Demonstrate search engine")
    
    from ranker import Ranker
    ranker = Ranker(avltree, bktree)

    while True:
        query = input("Query: ")
        string_matching_threshold = int(input("String matching threshold: "))
     
        tokenized_query = qp.process(query)
        ranking = ranker.get_ranking(tokenized_query, string_matching_threshold=string_matching_threshold)
    
        # dataset.get_book(book_id)                 # TODO: 3. Retrieve the book information for the best ranking books.  
        if ranking:
            
            ranking = get_ranking(ranking, query, dataset, lev)  # Option to sort the ranking based on Levenshtein distance

            length = int(input("How many results do you want to see? "))
            if length > len(ranking):
                length = len(ranking)

            print("Search Results:", end="\n\n")

            for i, result in enumerate(ranking[:length]):
                book_info = dataset.get_book(result[0])  # Assuming result[0] contains book_id
                print(f"Match {i} -> Book ID: {book_info['ID']}, Title: {book_info['TITLE']}, Author: {book_info['AUTHOR']}")
                print(f"Score   -> Similarity: {result[1]}, Levenshtein Distance: {lev(book_info['TITLE'], query)}", end="\n\n")
        else:
            print("No matching results found.")

        # Ask for continuation or exit
        cont = input("Do you want to continue searching? (yes/no): ").lower()
        if cont != 'yes':
            break



def get_ranking(ranking, query, dataset, lev):
    """
    Orders the titles in ranking, based on their Levenshtein distance to the given query.

    Parameters:
    - ranking (list): A list of tuples representing books .
    - query (str): The query string to compare book titles against.
    - dataset (object): An object representing the dataset of books.
    - lev (function): Function that calculates the Levenshtein distance.

    Returns:
    - list: A sorted list of book titles based on their similarity to the query.
    """

    libr = {}
    for title in ranking:
        book_title = dataset.get_book(title[0])['TITLE']
        distance = lev(book_title, query)
        libr[title] = distance

    return sorted(libr.keys(), key=lambda x: libr[x])


            


if __name__ == "__main__":
    main()