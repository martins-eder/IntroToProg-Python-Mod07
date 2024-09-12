# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,Updated Script with constants, classes, and functions
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ""  # Hold the choice made by the user


# Data Classes --------------------------------------- #
class Person:
    """ Represents a person """

    def __init__(self, first_name: str = "", last_name: str = ""):  # parameters default to empty
        self.__first_name = first_name  # set the attribute using the property to provide validation
        self.__last_name = last_name  # set the attribute using the property to provide validation

    @property  # decorator for getter or accessor
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter  # (setter or mutator)
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # allow characters or the default empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers or special characters.")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # allow characters or the default empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers or special characters.")

    def __str__(self):
        return self.__first_name + " " + self.__last_name


class Student(Person):
    """ A class that represents student data, inherits from Person """

    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name, last_name)
        self.__course_name = course_name

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        self.__course_name = value

    def __str__(self):
        return super().__str__() + " is enrolled in " + self.__course_name


# Processing --------------------------------------- #
class FileProcessor:
    """ A collection of processing layer functions that work with Json files
        ChangeLog: (Who, When, What)
        Eder Martins,9/11/2024,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

            ChangeLog: (Who, When, What)
            Eder Martins,9/11/2024,Created function

            :param file_name: string data with name of file to read from
            :param student_data: list of dictionary rows to be filled with file data

            :return: list
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

            ChangeLog: (Who, When, What)
            Eder Martins,9/11/2024,Created function

            :param file_name: string data with name of file to write to
            :param student_data: list of dictionary rows to be writen to the file

            :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            # After successfully writing to the file, print confirmation and the data
            print("\nData has been successfully saved to the file. The following data was stored:")
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
        A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        Eder Martins,9/11/2024,Created Class
        Eder Martins,9/11/2024,Added menu output and input functions
        Eder Martins,9/11/2024,Added a function to display the data
        Eder Martins,9/11/2024,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

            ChangeLog: (Who, When, What)
            Eder Martins,9/11/2024,Created function

            :param message: string with message data to display
            :param error: Exception object with technical message to display

            :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

            ChangeLog: (Who, When, What)
            Eder Martins,9/11/2024,Created function


            :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

            ChangeLog: (Who, When, What)
            Eder Martins,9/11/2024,Created function

            :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__()) # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

            ChangeLog: (Who, When, What)
            Eder Martins,9/11/2024,Created function

            :param student_data: list of dictionary rows to be displayed

            :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Eder Martins,9/11/2024,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or spaces.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers or spaces.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

