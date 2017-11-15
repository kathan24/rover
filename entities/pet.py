__author__ = 'kathan'

from enum import Enum
from utils.db import execute_statement


class Pet(object):

    def __init__(self, name, userId):
        self.name = name
        self.userId = userId
        self.breed = None
        self.size = PetSize.MEDIUM

    def save(self):
        query = """
            INSERT OR REPLACE INTO
              pet("name", "userId", "breed", "size")
            VALUES(
              :name,
              :userId,
              :breed,
              :size
            )
        """

        query_values = dict(
            name=self.name,
            userId=self.userId,
            breed=self.breed,
            size=self.size.value
        )

        execute_statement(query, query_values)


class PetSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2