__author__ = 'kathan'

import unittest
from entities import Sitter


class TestCase(unittest.TestCase):

    def test_overall_ranking_algorithm_mora_than_10_5_star_reviews(self):
        expected_initial_score = 2.75
        for i in range(1,12):
            sitter = Sitter(id=1, name='Abcdefghijklm Abcdefghijklm.', photoUrl='http://placekitten.com/g/500/500?user=24', phone='1234567890', email='rover@rover.com', rating_score=5, number_of_reviews=i)
            self.assertEquals(sitter.overall_rank, expected_initial_score)

            if i < 10:
                expected_initial_score += 0.25

    def test_overall_ranking_algorithm_5_5_star_reviews(self):
        sitter = None
        for i in range(1, 6):
            sitter = Sitter(id=1, name='Abcdefghijklm Abcdefghijklm.', photoUrl='http://placekitten.com/g/500/500?user=24', phone='1234567890', email='rover@rover.com', rating_score=5, number_of_reviews=i)

        self.assertEquals(sitter.overall_rank, 3.75)

    def test_sitter_score(self):
        sitter = Sitter(id=1, name='Abcdefghijklm Abcdefghijklm.', photoUrl='http://placekitten.com/g/500/500?user=24', phone='1234567890', email='rover@rover.com', rating_score=5, number_of_reviews=1)

        self.assertEquals(sitter.get_sitter_score(), 2.5)