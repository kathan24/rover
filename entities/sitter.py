__author__ = 'kathan'

from utils.db import execute_statement, fetch_one, fetch_all


class Sitter(object):

    def __init__(self, id, name, photoUrl, phone, email, rating_score, number_of_reviews):
        self.id = id
        self.name = name
        self.photoUrl = photoUrl
        self.phone = phone
        self.email = email
        self.rating_score = float(rating_score)
        self.number_of_reviews = number_of_reviews
        self.overall_rank = self.set_overall_rank()

    def save(self):
        query = """
            INSERT OR REPLACE INTO
              sitter("id", "name", "photoUrl", "phone", "email", "rating_score", "number_of_reviews", "overall_rank")
            VALUES(
              :id,
              :name,
              :photoUrl,
              :phone,
              :email,
              :rating_score,
              :number_of_reviews,
              :overall_rank
            )
        """

        query_values = dict(
            id=self.id,
            name=self.name,
            photoUrl=self.photoUrl,
            phone=self.phone,
            email=self.email,
            rating_score=self.rating_score,
            number_of_reviews=self.number_of_reviews,
            overall_rank=self.overall_rank
        )

        execute_statement(query, query_values)

    def set_overall_rank(self):
        if self.number_of_reviews == 0:
            return self.get_sitter_score()
        elif self.number_of_reviews >= 10:
            return self.rating_score
        else:
            sitter_score = self.get_sitter_score()

            weighted_average_sitter_score = sitter_score * (1 - (self.number_of_reviews / 10.0))
            weighted_average_rating_score = self.rating_score * (self.number_of_reviews / 10.0)

            total = weighted_average_sitter_score + weighted_average_rating_score

            return float("{0:.2f}".format(total))

    def get_sitter_score(self):
        characters_in_name = [char.lower() for char in self.name if char.isalpha()]
        unique_characters = len(set(characters_in_name))

        return 5 * (unique_characters / 26.0)

    @staticmethod
    def get(sitter_id):
        query = """
            SELECT
                *
            FROM
                sitter
            WHERE
                id=:id
        """

        query_values = dict(
            id=sitter_id
        )

        return fetch_one(query, query_values)

    @staticmethod
    def get_rating_score(new_rating, previous_record):
        total = (previous_record.rating_score * previous_record.number_of_reviews) + new_rating

        return total / float(previous_record.number_of_reviews + 1)


    @staticmethod
    def getSitters():
        query = """
            SELECT
                name,
                photoUrl,
                rating_score,
                overall_rank
            FROM
                sitter
            ORDER BY overall_rank DESC
        """

        return fetch_all(query)
