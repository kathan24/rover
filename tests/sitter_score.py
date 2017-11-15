__author__ = 'kathan'

import unittest
from entities import Sitter


class TestCase(unittest.TestCase):

    def test_sitter_score(self):
        sitter = Sitter(id=1, name='Abcdefghijklm Abcdefghijklm.', photoUrl='http://placekitten.com/g/500/500?user=24', phone='1234567890', email='rover@rover.com', rating_score=5, number_of_reviews=1)

        self.assertEquals(sitter.get_sitter_score(), 2.5)
