#!/usr/bin/env python3

import unittest
from tf_idf_inverted_index import TfIdfInvertedIndex


def build_index():
    index = TfIdfInvertedIndex()
    index.add_document(1, 'coffee coffee'.split())
    index.add_document(2, 'tea cup jar jar tea'.split())
    index.add_document(3, 'cup coffee jar cup'.split())
    index.add_document(4, 'coffee cup coffee jar tea cup coffee jar cup jar'
                       .split())
    index.add_document(5, 'jar water water jar'.split())
    return index


class TestCalcDocumentLengths(unittest.TestCase):
    def test_lecture_corpus(self):
        index = build_index()
        index.calc_document_lengths()
        self.assertEqual(5, len(index.document_lengths))
        self.assertAlmostEqual(0.44, index.document_lengths[1], delta=0.01)
        self.assertAlmostEqual(0.85, index.document_lengths[2], delta=0.01)
        self.assertAlmostEqual(0.50, index.document_lengths[3], delta=0.01)
        self.assertAlmostEqual(1.06, index.document_lengths[4], delta=0.01)
        self.assertAlmostEqual(1.41, index.document_lengths[5], delta=0.01)

    def test_book_corpus(self):
        index = TfIdfInvertedIndex()
        index.add_document(1, ['car'] * 27 + ['auto'] * 3 +
                           ['insurance'] * 0 + ['best'] * 14)
        index.add_document(2, ['car'] * 4 + ['auto'] * 33 +
                           ['insurance'] * 33 + ['best'] * 0)
        index.add_document(3, ['car'] * 24 + ['auto'] * 0 +
                           ['insurance'] * 29 + ['best'] * 17)
        index.calc_document_lengths()
        self.assertEqual(3, len(index.document_lengths))
        self.assertAlmostEqual(2.52, index.document_lengths[1], delta=0.01)
        self.assertAlmostEqual(8.22, index.document_lengths[2], delta=0.01)
        self.assertAlmostEqual(5.92, index.document_lengths[3], delta=0.01)

    def test_empty_corpus(self):
        index = TfIdfInvertedIndex()
        index.calc_document_lengths()
        self.assertEqual(0, len(index.document_lengths))


class TestSearch(unittest.TestCase):
    def test_lecture_results(self):
        index = build_index()
        index.calc_document_lengths()
        results = index.search('cup jar'.split())
        self.assertEqual(4, len(results))
        self.assertEqual(3, results[0][0])  # doc id
        self.assertAlmostEqual(0.88, results[0][1], delta=0.01)  # doc relevance
        self.assertEqual(4, results[1][0])  # doc id
        self.assertAlmostEqual(0.68, results[1][1], delta=0.01)  # doc relevance
        self.assertEqual(2, results[2][0])  # doc id
        self.assertAlmostEqual(0.33, results[2][1], delta=0.01)  # doc relevance
        self.assertEqual(5, results[3][0])  # doc id
        self.assertAlmostEqual(0.05, results[3][1], delta=0.01)  # doc relevance

    def test_single_results(self):
        index = build_index()
        index.calc_document_lengths()
        results = index.search('water water'.split())
        self.assertEqual(1, len(results))
        self.assertEqual(5, results[0][0])  # doc id
        self.assertAlmostEqual(0.99, results[0][1], delta=0.01)  # doc relevance

    def test_empty_results(self):
        index = build_index()
        index.calc_document_lengths()
        results = index.search('cola'.split())
        self.assertEqual(0, len(results))


if __name__ == '__main__':
    unittest.main()
