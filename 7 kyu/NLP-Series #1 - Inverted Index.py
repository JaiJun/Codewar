"""
    You are given an array of documents (strings), a term (string), and two booleans finetuning your indexing operation. Return an array containing the document IDs (1-based indices of documents in the array), where the term occurs, sorted in ascending order.

    Booleans:

    CaseSensitive: test matches test, but not Test
    Not CaseSensitive: test matches both test and Test

    Exact Match: test matches test and .test!, but not attest or test42
    Not Exact Match: test matches both test and attest
"""
import re

def build_inverted_index(collection, term, case_sensitive, exact_match):
    pass
if __name__ == '__main__':
    input = ['Rumpel Dumpel','Holger', 'Quadrumpel']
    compare = 'UmPeL'
    CaseSensitive = False
    ExactMatch = False
    build_inverted_index(input, compare, CaseSensitive, ExactMatch)