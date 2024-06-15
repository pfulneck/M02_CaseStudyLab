# Author: Patrick Fulnecky
# Program Name: Student GPA Classifier
# This program accepts student's names and GPA's as input,
# then tests if the student qualifies for either Dean's List or Honor Roll

QUIT = str('ZZZ')
studentLastName = input("Please enter the student's last name or 'ZZZ' to quit: ")

while studentLastName != QUIT:
    studentFirstName = input("Please enter the student's first name: ")
    studentGPA = float(input("Please enter the Student's GPA: "))
    if studentGPA >= 3.5:
        print(studentFirstName, studentLastName + " has made the Dean's List and Honor Roll!")
    elif studentGPA >= 3.25:
        print(studentFirstName, studentLastName + " has made the Honor Roll!")
    else:
        print(studentFirstName, studentLastName + " Needs to improve their GPA to qualify for the Dean's List and/or Honor Roll. ")
    studentLastName = input("Please enter the student's last name or 'ZZZ' to quit: ")
