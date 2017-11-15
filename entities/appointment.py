__author__ = 'kathan'

from utils.db import execute_statement


class Appointment(object):

    def __init__(self, userId, sitterId, rating, startDate, endDate, review):
        self.userId = userId
        self.sitterId = sitterId
        self.rating = rating
        self.startDate = startDate
        self.endDate = endDate
        self.review = review

    def save(self):
        query = """
            INSERT INTO
              appointment("userId", "sitterId", "rating", "startDate", "endDate", "review")
            VALUES(
              :userId,
              :sitterId,
              :rating,
              :startDate,
              :endDate,
              :review
            )
        """

        query_values = dict(
            userId=self.userId,
            sitterId=self.sitterId,
            rating=self.rating,
            startDate=self.startDate,
            endDate=self.endDate,
            review=self.review
        )

        execute_statement(query, query_values)
