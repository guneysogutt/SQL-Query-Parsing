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

# Check whether true or not the given conditions by the operation type
def validate_operation(cond1:bool,operation_type:str,cond2:bool):
    if operation_type == "and":
        return cond1 and cond2
    else:
        return cond1 or cond2


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

# Delete student from table
def delete_from_table(input_elements:list,student_list:list):
    # Check the number of the condition(s)
    if len(input_elements) > 7:
        print("--MORE THAN ONE CONDITION--")########delete this
        index = 4
        constraint1 = input_elements[index]
        symbol1 = fix_operation_indentation(input_elements[index + 1])
        value1 = input_elements[index + 2]

        constraint2 = input_elements[index + 4]
        symbol2 = fix_operation_indentation(input_elements[index + 5])
        value2 = input_elements[index + 6]

        operation_type = input_elements[7].lower()

        for student in list_csv_file:
            if validate_operation(check_condition(symbol1, student, constraint1, value1), operation_type, check_condition(symbol2, student, constraint2, value2)):
                print(student)
                student_list.remove(student)


    else:
        print("--ONE CONDITION--")########delete this
        constraint = input_elements[4]
        symbol = input_elements[5]
        value = input_elements[6]
        # Iterate through the list
        for student in list_csv_file:
            # Check the condition in the query
            if check_condition(symbol, student, constraint, value):
                print(student)
                # DDelete the item if satisfies the condition
                student_list.remove(student)

    print(student_list.count('John')) # Check if any item left ########delete this
    return student_list
# end delete_from_table

# Select operation - query printing
def select_operation(input_elements:list,list_csv_file):
    # Sort the temporary student list
    sorted_student_list = sorted(list_csv_file, key=lambda k: int(k['id']), reverse=False)

    column_names = input_elements[1].split(',')

    index = 5
    operation_type = input_elements[8].lower()
    # If multiple conditions in the query
    if operation_type == "and" or operation_type == "or":
        print("---MORE THAN ONE STATEMENT---")
        constraint1 = input_elements[index]
        symbol1 = fix_operation_indentation(input_elements[index + 1])
        value1 = input_elements[index + 2]

        constraint2 = input_elements[index + 4]
        symbol2 = fix_operation_indentation(input_elements[index + 5])
        value2 = input_elements[index + 6]

        for student in sorted_student_list:
            if validate_operation(check_condition(symbol1, student, constraint1, value1), operation_type,
                                  check_condition(symbol2, student, constraint2, value2)):
                print_columns(column_names, student)


    # If one statement occurs for constraints
    else:
        print("---ONE STATEMENT---")########delete this
        constraint = input_elements[5]
        symbol = fix_operation_indentation(input_elements[6])
        value = input_elements[7]

        for student in sorted_student_list:
            if check_condition(symbol, student, constraint, value):
                print_columns(column_names, student)
# end select_operation


# opening the CSV file
with open('students.csv') as file:
    # reading the CSV file
    csv_file = csv.DictReader(file, delimiter=';')

    # Storing student data as list of dictionaries
    list_csv_file = list(csv_file)
# end reading csv file

# Get the user input
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


# Select operation
elif (query_type.lower() == "select"):
    select_operation(input_elements,list_csv_file)


# Creating json file and writing students
with open("students.json", "w") as json_file:
    for student in list_csv_file:
        json.dump(student, json_file, indent=3, ensure_ascii=False)
