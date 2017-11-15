__author__ = 'kathan'

import os
import sys
import csv
from utils.db import execute_script
from entities import Sitter, User, Pet, Appointment

# rating - 0 ,
# sitter_image - 1,
# end_date - 2,
# text - 3,
# owner_image - 4,
# dogs - 5,
# sitter - 6,
# owner - 7,
# start_date - 8,
# sitter_phone_number - 9,
# sitter_email - 10,
# owner_phone_number - 11,
# owner_email - 12

dir_path = os.path.dirname(os.path.realpath(__file__))


def create_table(schema_file_path):
    if not schema_file_path:
        schema_file_path = "database_schema.txt"

    try:
        with open(dir_path + '/' + schema_file_path, "r") as table_file:
            create_tables_script = table_file.read()

        execute_script(create_tables_script)
    except IOError, e:
        raise e


def read_csv_and_load_data(data_file_path):
    if not data_file_path:
        data_file_path = "reviews.csv"

    try:
        with open(dir_path + '/' + data_file_path, "r") as data_file:

            file_data = csv.reader(data_file)

            # skipping header
            file_data.next()

            for row in file_data:
                row = [column_data.strip() for column_data in row]

                # if incorrect data, skip the row
                if len(row) != 13:
                    continue

                sitter_temp = row[1].split("user=")
                if len(sitter_temp) < 2:
                    continue

                sitter_id = sitter_temp[1]

                user_temp = row[4].split("user=")
                if len(user_temp) < 2:
                    continue

                user_id = user_temp[1]

                load_appointment_data(data=row, user_id=user_id, sitter_id=sitter_id)
                load_pet_data(data=row, user_id=user_id)
                load_sitter_data(data=row, sitter_id=sitter_id)
                load_user_data(data=row, user_id=user_id)
    except IOError, e:
        print e

def load_pet_data(data, user_id):
    if not all([data, user_id]):
        return

    pets = data[5].split('|')

    for pet in pets:
        pet = Pet(name=pet,
                  userId=user_id)
        pet.save()


def load_appointment_data(data, user_id, sitter_id):
    if not all([data, user_id, sitter_id]):
        return

    appointment = Appointment(userId=user_id,
                              sitterId=sitter_id,
                              rating=data[0],
                              startDate=data[8],
                              endDate=data[2],
                              review=data[3])
    appointment.save()


def load_user_data(data, user_id):
    if not all([data, user_id]):
        return

    user = User(id=user_id,
                name=data[7],
                photoUrl=data[4],
                phone=data[11],
                email=data[12])
    user.save()


def load_sitter_data(data, sitter_id):
    if not all([data, sitter_id]):
        return

    already_present_sitter = Sitter.get(sitter_id)

    if already_present_sitter:
        rating_score = Sitter.get_rating_score(new_rating=float(data[0]),
                                               previous_record=already_present_sitter)

        number_of_reviews = already_present_sitter.number_of_reviews + 1
    else:
        rating_score = data[0]
        number_of_reviews = 1

    sitter = Sitter(id=sitter_id,
                    name=data[6],
                    photoUrl=data[1],
                    phone=data[9],
                    email=data[10],
                    rating_score=rating_score,
                    number_of_reviews=number_of_reviews)
    sitter.save()


if len(sys.argv) == 1:
    raise Exception("Please provide schema and data file path")
try:
    create_table(sys.argv[1])
except IOError, e:
    print e
else:
    if len(sys.argv) > 2:
        read_csv_and_load_data(sys.argv[2])