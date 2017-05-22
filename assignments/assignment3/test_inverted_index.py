#!/usr/bin/env python3

import unittest
from inverted_index import InvertedIndex


def build_index():
    index = InvertedIndex()
    index.add_document(1, 'coffee coffee'.split())
    index.add_document(2, 'tea cup jar jar tea'.split())
    index.add_document(3, 'cup coffee jar cup'.split())
    index.add_document(4, 'coffee cup coffee jar tea cup coffee jar cup jar'
                       .split())
    index.add_document(5, 'jar water water jar'.split())
    return index


class InvertedIndexTest(unittest.TestCase):
    def test_find_with_word(self):
        index = build_index()
        self.assertEqual({1, 3, 4}, index.find_documents_with_word('coffee'))
        self.assertEqual({2, 3, 4}, index.find_documents_with_word('cup'))
        self.assertEqual({2, 3, 4, 5}, index.find_documents_with_word('jar'))
        self.assertEqual({2, 4}, index.find_documents_with_word('tea'))
        self.assertEqual({5}, index.find_documents_with_word('water'))
        self.assertEqual(set(), index.find_documents_with_word('unkown_word'))

    def test_find_with_unkown_phrase(self):
        index = build_index()
        self.assertEqual(set(), index.find_documents_with_phrase(
            'jar coffee'.split()))
        self.assertEqual(set(), index.find_documents_with_phrase(
            'unkown_word'.split()))
        self.assertEqual(set(), index.find_documents_with_phrase(
            'jar unkown_word'.split()))
        self.assertEqual(set(), index.find_documents_with_phrase(
            'unkown_word coffee'.split()))

    def test_find_with_phrase_length_one(self):
        index = build_index()
        self.assertEqual({1, 3, 4},
                         index.find_documents_with_phrase('coffee'.split()))
        self.assertEqual({2, 3, 4},
                         index.find_documents_with_phrase('cup'.split()))
        self.assertEqual({2, 3, 4, 5},
                         index.find_documents_with_phrase('jar'.split()))
        self.assertEqual({2, 4},
                         index.find_documents_with_phrase('tea'.split()))
        self.assertEqual({5}, index.find_documents_with_phrase('water'.split()))

    def test_find_with_phrase_length_two(self):
        index = build_index()
        self.assertEqual({2, 4},
                         index.find_documents_with_phrase('tea cup'.split()))
        self.assertEqual({3, 4},
                         index.find_documents_with_phrase('coffee jar'.split()))
        self.assertEqual({5},
                         index.find_documents_with_phrase('water jar'.split()))

    def test_find_with_phrase_length_three(self):
        index = build_index()
        self.assertEqual({3, 4}, index.find_documents_with_phrase(
            'cup coffee jar'.split()))
        self.assertEqual({3, 4}, index.find_documents_with_phrase(
            'coffee jar cup'.split()))
        self.assertEqual({2}, index.find_documents_with_phrase(
            'tea cup jar'.split()))

    def test_find_with_phrase_length_four(self):
        index = build_index()
        self.assertEqual({3, 4}, index.find_documents_with_phrase(
            'cup coffee jar cup'.split()))
        self.assertEqual({4}, index.find_documents_with_phrase(
            'cup coffee jar tea'.split()))
        self.assertEqual({5}, index.find_documents_with_phrase(
            'jar water water jar'.split()))

    def test_find_with_phrase_identical_words(self):
        index = build_index()
        self.assertEqual({1}, index.find_documents_with_phrase(
            'coffee coffee'.split()))
        self.assertEqual({2}, index.find_documents_with_phrase(
            'jar jar'.split()))
        self.assertEqual({5}, index.find_documents_with_phrase(
            'water water'.split()))

    def test_empty_index(self):
        index = InvertedIndex()
        self.assertEqual(set(), index.find_documents_with_word('jar'))
        self.assertEqual(set(), index.find_documents_with_phrase('jar'.split()))


if __name__ == '__main__':
    unittest.main()
