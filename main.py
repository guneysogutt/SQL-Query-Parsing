# Ege-Kemal-Germen_2019510150, Güney-Söğüt_2020510066

import csv
import json
from operator import itemgetter


# Check the input id if exists or not
def search_id(student_list: list, searched_id: str):
    for student in student_list:
        if (student['id'] == searched_id):
            return True
    return False


def fix_operation_indentation(input:str):
    if(input == "!<"):
        input = ">="
    elif(input == "!>"):
        input = "<="
    return input

# Print the demanded columns
def print_columns(column_names: list, student:str):
    for name in column_names:
        print(student[name], end=" ")
    print()
# end print_columns

# Check the condition then print the appropriate student info
def check_condition(symbol:str, student:str, constraint:str, value:str):
    if(constraint.lower() == "id" or constraint.lower() == "grade"):
        if (symbol == "<"):
            if(int(student[constraint]) < int(value)):
                return True
        elif (symbol == "<="):
            if(int(student[constraint]) <= int(value)):
                return True
        elif (symbol == ">"):
            if(int(student[constraint]) > int(value)):
                return True
        elif (symbol == ">="):
            if(int(student[constraint]) >= int(value)):
                return True
        elif (symbol == "="):
            if(int(student[constraint]) == int(value)):
                return True
        elif (symbol == "!="):
            if(int(student[constraint]) != int(value)):
                return True
    else:
        value = value[1:len(value) - 1]
        if (symbol == "="):
            if(student[constraint] == value):
                return True
        elif (symbol == "!="):
            if(student[constraint] != value):
                return True
# end print_statement

# Insert the given student values into the table if valid
def insert_to_table(input_elements:list,student_list:list):
    # Split the student attributes from the user input
    last_item = input_elements[len(input_elements) - 1]
    # Get the expression inside the brackets
    last_item = last_item[last_item.index('(') + 1:last_item.index(')')]

    student_attributes = last_item.split(',') # Store input student values
    input_id = student_attributes[0] # Store the input id

    # Check for id whether exists or not
    if not (search_id(list_csv_file, input_id)):
        # Assign the attributes
        input_name = student_attributes[1]
        input_lastname = student_attributes[2]
        input_email = student_attributes[3]
        input_grade = student_attributes[4]
        # end assigning attributes

        # Insert them into the main table
        student_list.append({'id': input_id, 'name': input_name, 'lastname': input_lastname, 'email': input_email,
                            'grade': input_grade})
    # If already exists print an error message
    else:
        print("The given id is already exists!!!")

    # Return the given list. If the process is succeeded the main list will be updated.
    # If not it returns the list without any changes
    return student_list
# end insert_to_table


def delete_from_table(input_elements:list,student_list:list):
    # Check the number of the condition(s)
    if(len(input_elements) > 7):
        print("--MORE THAN ONE CONDITION--")
        index = 4
        constraint1 = input_elements[index]
        symbol1 = fix_operation_indentation(input_elements[index + 1])
        value1 = input_elements[index + 2]

        constraint2 = input_elements[index + 4]
        symbol2 = fix_operation_indentation(input_elements[index + 5])
        value2 = input_elements[index + 6]

        operation_type = input_elements[7].lower()

        for student in list_csv_file:
            if (operation_type == "and"):
                if (check_condition(symbol1, student, constraint1, value1) and check_condition(symbol2, student, constraint2, value2)):
                    print(student)
                    student_list.remove(
                        {'id': student['id'], 'name': student['name'], 'lastname': student['lastname'],
                         'email': student['email'], 'grade': student['grade']})
            else:
                if (check_condition(symbol1, student, constraint1, value1) or check_condition(symbol2, student, constraint2, value2)):
                    print(student)
                    student_list.remove(
                        {'id': student['id'], 'name': student['name'], 'lastname': student['lastname'],
                         'email': student['email'], 'grade': student['grade']})


    else:
        print("--ONE CONDITION--")
        constraint = input_elements[4]
        symbol = input_elements[5]
        value = input_elements[6]

        for student in list_csv_file:
            if (check_condition(symbol,student,constraint,value)):
                print(student)
                student_list.remove(
                    {'id': student['id'], 'name': student['name'], 'lastname': student['lastname'], 'email': student['email'],'grade': student['grade']})

    print(student_list.count('John'))
    return student_list
# end delete_from_table



# Boolean to check whether the query is true or not
is_the_query_true = False


# opening the CSV file
with open('students.csv') as file:
    # reading the CSV file
    csv_file = csv.DictReader(file, delimiter=';')

    # Storing student data as list of dictionaries
    list_csv_file = list(csv_file)
# end reading csv file


# User Inputs, will be taken from user query
input_id = "id"
input_name = "name"
input_lastname = "lastname"
input_email = "email"
input_grade = "grade"

# INSERT INTO STUDENT VALUES(15000,Ali,Veli,ali.veli@spacex.com,20)
# SELECT name FROM STUDENTS WHERE grade > 40 AND name = ‘John’ ORDER BY DSC
# SELECT name,lastname FROM STUDENTS WHERE grade !< 40 ORDER BY ASC
# DELETE FROM STUDENT WHERE name = ‘John’ and grade <= 20

user_input = input("Please enter your query:\n")

input_elements = user_input.split(" ") # Split the user input by space
query_type = input_elements[0] # Store the query type (select, insert or delete)

# Check the operation (insertion, remove or an item query)
if (query_type.lower() == "insert"):
    # Insert the given values in the query to the main table
   list_csv_file = insert_to_table(input_elements,list_csv_file)



# Delete operation
elif (query_type.lower() == "delete"):
    list_csv_file = delete_from_table(input_elements,list_csv_file)


# SELECT name FROM STUDENTS WHERE grade > 40 AND name = ‘John’ ORDER BY DSC
# SELECT name,lastname FROM STUDENTS WHERE grade !< 40 ORDER BY ASC

# Select operation
elif (query_type.lower() == "select"):
    # Sort the temporary student list
    sorted_student_list = sorted(list_csv_file, key=lambda k: int(k['id']), reverse=False)

    column_names = input_elements[1].split(',')

    index = 5
    operation_type = input_elements[8].lower()
    # If multiple conditions in the query
    if(operation_type == "and" or operation_type == "or"):
        print("---MORE THAN ONE STATEMENT---")
        constraint1 = input_elements[index]
        symbol1 = fix_operation_indentation(input_elements[index+1])
        value1 = input_elements[index+2]

        constraint2 = input_elements[index+4]
        symbol2 = fix_operation_indentation(input_elements[index+5])
        value2 = input_elements[index+6]


        for student in sorted_student_list:
            if (operation_type == "and"):
                if (check_condition(symbol1, student, constraint1, value1) and check_condition(symbol2, student, constraint2, value2)):
                    print_columns(column_names, student)
            else:
                if (check_condition(symbol1, student, constraint1, value1) or check_condition(symbol2, student, constraint2, value2)):
                    print_columns(column_names, student)




    # If one statement occurs for constraints
    else:
        print("---ONE STATEMENT---")
        constraint = input_elements[5]
        symbol = fix_operation_indentation(input_elements[6])
        value = input_elements[7]

        for student in sorted_student_list:
            if (check_condition(symbol, student, constraint, value)):
                print_columns(column_names, student)

        """
        if (constraint.lower() == "id" or constraint.lower() == "grade"):
            print("--ID OR GRADE(INT)--")
            for student in sorted_student_list:
                if(print_statement(symbol,student,constraint,value)):
                    print_columns(column_names,student)



        else:
            print("--OTHER(STR)--")
            if (symbol == "<" or symbol == "<=" or symbol == ">" or symbol == ">="):
                print("-error!!!!!!!!!!!!!!!!!!!!!!!!-")
                is_the_query_true = False
            else:

                for student in sorted_student_list:
                    if (print_statement(symbol, student, constraint, value)):
                        print_columns(column_names, student)

                
                if(symbol == "="):
                    print("-EQUAL-")

                    for student in sorted_student_list:
                        # Printing student data
                        if (student[constraint] == value):
                           print_columns(column_names,student)

                elif(symbol == "!="):
                    print("-NOT EQUAL-")

                    for student in sorted_student_list:
                        # Printing student data
                        if (student[constraint] != value):
                           print_columns(column_names,student)
                
        """




# Creating json file and writing students
with open("students.json", "w") as json_file:
    for student in list_csv_file:
        json.dump(student, json_file, indent=3, ensure_ascii=False)
