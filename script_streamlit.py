import streamlit as st
import sys
from util_bktree import TextProcessor
from avltree_x1 import AVLTreeX1 as AVLTree
from bktree import BKTree
from levenshtein import lev_dp as lev
from util_bktree import Dataset
from ranker import Ranker

def get_ranking(ranking, query, dataset, lev):
    """
    Orders the titles in ranking, based on their Levenshtein distance to the given query.

    Parameters:
    - ranking (list): A list of tuples representing books.
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

def main():
    st.title("Book Search Engine")
    st.sidebar.header("Settings")
    string_matching_threshold = st.sidebar.slider("String Matching Threshold", min_value=0, max_value=10, value=5, key="string_matching_threshold")

    sys.setrecursionlimit(10000)
    qp = TextProcessor()
    s = "This is some sample string"
    bow = qp.process(s)  # NOTE: You can use the given method to process a sentence into a tokenized bag-of-words

    avltree = AVLTree()
    bktree = BKTree(lev)
    dataset = Dataset("brooklyn_public_library_catalog_selected.csv", 1000)

    st.write("Indexing: Load in the data")

    # Easy iteration over dataset.
    for book in dataset:
        book_id = book['ID']
        book_title = book['TITLE']

        tokenized_title = qp.process(book_title)

        for word in tokenized_title:
            avltree.insert(word, book_id)  # TODO: 1. Construct a binary search tree to map title words to book ID
            bktree.insert(word)  # TODO: 2. Construct a BK-tree to structure similar words.

    st.write("Indexing completed")

    st.write("Ranking: Demonstrate search engine")

    ranker = Ranker(avltree, bktree)
    i = 0
    while True:
        i+=1
        query = st.text_input("Query", key=f"query_{i}")
        if not query:
            st.warning("Please enter a query.")
            return

        ranking = ranker.get_ranking(qp.process(query), string_matching_threshold=string_matching_threshold)

        if ranking:
            ranking = get_ranking(ranking, query, dataset, lev)  # Option to sort the ranking based on Levenshtein distance

            length = st.slider("How many results do you want to see?", min_value=1, max_value=min(len(ranking), 10), value=5, key=f"length_{i}")
            st.write("Search Results:")

            for j, result in enumerate(ranking[:length]):
                book_info = dataset.get_book(result[0])  # Assuming result[0] contains book_id
                st.write(f"Match {j+1} -> Book ID: {book_info['ID']}, Title: {book_info['TITLE']}, Author: {book_info['AUTHOR']}")
                st.write(f"Score   -> Similarity: {result[1]}, Levenshtein Distance: {lev(book_info['TITLE'], query)}")
                st.write("\n")
        else:
            st.warning("No matching results found.")

        # Ask for continuation or exit
        cont = st.radio("Do you want to continue searching?", options=["Yes", "No"], key=f"cont_{i}")
        if cont == 'No':
            break

if __name__ == "__main__":
    main()
