#!/usr/bin/env python3

import unittest
from evaluation import precision, recall, f1_score, precision_at_k, \
    r_precision, mean_average_precision


class EvaluationTest(unittest.TestCase):
    def test_precision(self):
        self.assertAlmostEqual(0.40, precision('pacman'), delta=0.01)
        self.assertAlmostEqual(0.60, precision('zerg rush'), delta=0.01)
        self.assertAlmostEqual(0.50, precision('google in 1998'), delta=0.01)
        self.assertAlmostEqual(0.50, precision('askew'), delta=0.01)

    def test_recall(self):
        self.assertAlmostEqual(1.00, recall('pacman'), delta=0.01)
        self.assertAlmostEqual(1.00, recall('zerg rush'), delta=0.01)
        self.assertAlmostEqual(1.00, recall('google in 1998'), delta=0.01)
        self.assertAlmostEqual(1.00, recall('askew'), delta=0.01)

    def test_f1_score(self):
        self.assertAlmostEqual(0.57, f1_score('pacman'), delta=0.01)
        self.assertAlmostEqual(0.75, f1_score('zerg rush'), delta=0.01)
        self.assertAlmostEqual(0.66, f1_score('google in 1998'), delta=0.01)
        self.assertAlmostEqual(0.66, f1_score('askew'), delta=0.01)

    def test_precision_at_k(self):
        self.assertAlmostEqual(1.00, precision_at_k('pacman', 1), delta=0.01)
        self.assertAlmostEqual(0.40, precision_at_k('pacman', 5), delta=0.01)
        self.assertAlmostEqual(0.00, precision_at_k('zerg rush', 1), delta=0.01)
        self.assertAlmostEqual(0.40, precision_at_k('zerg rush', 5), delta=0.01)
        self.assertAlmostEqual(1.00, precision_at_k('google in 1998', 1),
                               delta=0.01)
        self.assertAlmostEqual(0.40, precision_at_k('google in 1998', 5),
                               delta=0.01)
        self.assertAlmostEqual(0.00, precision_at_k('askew', 1), delta=0.01)
        self.assertAlmostEqual(0.40, precision_at_k('askew', 5), delta=0.01)

    def test_r_precision(self):
        self.assertAlmostEqual(0.50, r_precision('pacman'), delta=0.01)
        self.assertAlmostEqual(0.50, r_precision('zerg rush'), delta=0.01)
        self.assertAlmostEqual(0.40, r_precision('google in 1998'), delta=0.01)
        self.assertAlmostEqual(0.53, r_precision('askew'), delta=0.01)

    def test_mean_average_precision(self):
        self.assertAlmostEqual(0.56, mean_average_precision(
            {'pacman', 'zerg rush', 'google in 1998'}), delta=0.01)
        self.assertAlmostEqual(0.51, mean_average_precision({'askew'}),
                               delta=0.01)
        self.assertAlmostEqual(0.65, mean_average_precision(
            {'answer to life the universe and everything',
             'once in a blue moon', 'anagram', 'recursion'}), delta=0.01)
        self.assertAlmostEqual(0.00, mean_average_precision(set()), delta=0.01)

    def test_empty_results(self):
        self.assertAlmostEqual(0.00, precision('_emptyresults'), delta=0.01)
        self.assertAlmostEqual(0.00, recall('_emptyresults'), delta=0.01)
        self.assertAlmostEqual(0.00, f1_score('_emptyresults'), delta=0.01)
        self.assertAlmostEqual(0.00, precision_at_k('_emptyresults', 1),
                               delta=0.01)
        self.assertAlmostEqual(0.00, precision_at_k('_emptyresults', 5),
                               delta=0.01)
        self.assertAlmostEqual(0.00, r_precision('_emptyresults'), delta=0.01)
        self.assertAlmostEqual(0.00, mean_average_precision({'_emptyresults'}),
                               delta=0.01)

    def test_empty_goldstandard(self):
        self.assertAlmostEqual(0.00, precision('_emptygoldstandard'),
                               delta=0.01)
        self.assertAlmostEqual(1.00, recall('_emptygoldstandard'), delta=0.01)
        self.assertAlmostEqual(0.00, f1_score('_emptygoldstandard'), delta=0.01)
        self.assertAlmostEqual(0.00, precision_at_k('_emptygoldstandard', 1),
                               delta=0.01)
        self.assertAlmostEqual(0.00, precision_at_k('_emptygoldstandard', 5),
                               delta=0.01)
        self.assertAlmostEqual(1.00, r_precision('_emptygoldstandard'),
                               delta=0.01)
        self.assertAlmostEqual(1.00,
                               mean_average_precision({'_emptygoldstandard'}),
                               delta=0.01)

    def test_empty_both(self):
        self.assertAlmostEqual(1.00, precision('_emptyboth'), delta=0.01)
        self.assertAlmostEqual(1.00, recall('_emptyboth'), delta=0.01)
        self.assertAlmostEqual(1.00, f1_score('_emptyboth'), delta=0.01)
        self.assertAlmostEqual(1.00, precision_at_k('_emptyboth', 1),
                               delta=0.01)
        self.assertAlmostEqual(1.00, precision_at_k('_emptyboth', 5),
                               delta=0.01)
        self.assertAlmostEqual(1.00, r_precision('_emptyboth'), delta=0.01)
        self.assertAlmostEqual(1.00, mean_average_precision({'_emptyboth'}),
                               delta=0.01)


if __name__ == '__main__':
    unittest.main()
