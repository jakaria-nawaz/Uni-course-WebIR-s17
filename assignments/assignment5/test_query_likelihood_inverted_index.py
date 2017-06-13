#!/usr/bin/env python3

import unittest
from query_likelihood_inverted_index import QueryLikelihoodInvertedIndex


def build_index():
    index = QueryLikelihoodInvertedIndex()
    index.add_document(1, 'coffee coffee'.split())
    index.add_document(2, 'tea cup jar jar tea'.split())
    index.add_document(3, 'cup coffee jar cup'.split())
    index.add_document(4, 'coffee cup coffee jar tea cup coffee jar cup jar'
                       .split())
    index.add_document(5, 'jar water water jar'.split())
    return index


class TestQueryLikelihoodInvertedIndex(unittest.TestCase):
    def test_build_index(self):
        build_index()  # test if no exception is thrown here.

    def test_single_water(self):
        index = build_index()
        results = index.search('water'.split())
        self.assertEqual(1, len(results))
        self.assertEqual(5, results[0][0])
        self.assertAlmostEqual(0.290, results[0][1], delta=0.001)

    def test_double_water(self):
        index = build_index()
        results = index.search('water water'.split())
        self.assertEqual(1, len(results))
        self.assertEqual(5, results[0][0])
        self.assertAlmostEqual(0.084, results[0][1], delta=0.001)

    def test_search_cup_jar(self):
        index = build_index()
        results = index.search('cup jar'.split())
        self.assertEqual(4, len(results))
        self.assertEqual(3, results[0][0])
        self.assertAlmostEqual(0.105, results[0][1], delta=0.001)
        self.assertEqual(4, results[1][0])
        self.assertAlmostEqual(0.084, results[1][1], delta=0.001)
        self.assertEqual(2, results[2][0])
        self.assertAlmostEqual(0.079, results[2][1], delta=0.001)
        self.assertEqual(5, results[3][0])
        self.assertAlmostEqual(0.049, results[3][1], delta=0.001)

    def test_search_jar_cup(self):
        index = build_index()
        results = index.search('jar cup'.split())
        self.assertEqual(4, len(results))
        self.assertEqual(3, results[0][0])
        self.assertAlmostEqual(0.105, results[0][1], delta=0.001)
        self.assertEqual(4, results[1][0])
        self.assertAlmostEqual(0.084, results[1][1], delta=0.001)
        self.assertEqual(2, results[2][0])
        self.assertAlmostEqual(0.079, results[2][1], delta=0.001)
        self.assertEqual(5, results[3][0])
        self.assertAlmostEqual(0.049, results[3][1], delta=0.001)

    def test_empty_results(self):
        index = build_index()
        results = index.search('cola'.split())
        self.assertEqual(0, len(results))


if __name__ == '__main__':
    unittest.main()
