# Ege-Kemal-Germen_2019510150, Güney-Söğüt_2020510066

import csv
import json
from operator import itemgetter

# opening the CSV file
with open('students.csv') as file:
    # reading the CSV file
    csv_file = csv.DictReader(file, delimiter=';')

    # Storing student data as list of dictionaries
    list_csv_file = list(csv_file)

    # User Inputs, will be taken from user query
    input_id = "id"
    input_name = "name"
    input_lastname = "lastname"
    input_email = "email"
    input_grade = "grade"

    # For user deletion
    # list_csv_file.remove({'id': input_id, 'name': input_name, 'lastname': input_lastname, 'email': input_email, 'grade': input_grade})

    # For student inserting
    # list_csv_file.append({'id': input_id, 'name': input_name, 'lastname': input_lastname, 'email': input_email, 'grade': input_grade})

    # For sorting students, second parameter(key) is taken from user query. Make reverse True if you want descending sort
    sorted_student_list = sorted(list_csv_file, key=itemgetter('id'), reverse=False)

    # Example of printing students which grades are below 50 (it prints 5 after 49?)
    for line in sorted_student_list:
       # if int(line['grade']) < 50:

            # Printing all student data
       if(int(line['id']) <= 100):
            print(line)

            # Printing grade-sorted array with only name and lastname. Column names will be taken from user query
           # print(line["id"], line["name"], line["lastname"], line["email"], line["grade"])


    # Creating json file and writing students
    with open("students.json", "w") as json_file:
        for student in list_csv_file:
            json.dump(student, json_file, indent=3, ensure_ascii=False)
