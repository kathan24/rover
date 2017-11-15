__author__ = 'kathan'

from utils.db import execute_statement

class User(object):

    def __init__(self, id, name, photoUrl, phone, email):
        self.id = id
        self.name = name
        self.photoUrl = photoUrl
        self.phone = phone
        self.email = email

    def save(self):
        query = """
            INSERT OR REPLACE INTO
              user("id", "name", "photoUrl", "phone", "email")
            VALUES(
              :id,
              :name,
              :photoUrl,
              :phone,
              :email
            )
        """

        query_values = dict(
            id=self.id,
            name=self.name,
            photoUrl=self.photoUrl,
            phone=self.phone,
            email=self.email
        )

        execute_statement(query, query_values)