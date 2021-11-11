Lab 8


Problem
A professor needs a program that will choose a random student in class to call on when no one is raising their hand to offer an answer. Write a program that asks the user for a filename and then reads in the student names from the given file and stores them in a list. The program should then give the user a randomly-chosen name and give the option to continue or quit. If the user chooses to continue, the program should draw a new name (with the previous name having been removed from consideration).

The names of the students in the class are supplied as a plain-text file with one name per line. Use the file names.txt accompanying this handout, which contains names taken from randomlists.com, to test your program. However, your program should work with any valid plain-text file of names.

Instructions
Create a new Python file and place intro comments using the template below.
Use comments to write the algorithm your program will follow, including functions.
Write the Python code corresponding to each of your algorithm's steps.
Commit and push changes and check your repository on github.com to confirm your updates before leaving lab (even if not finished).

Note: This lab does not require a flowchart or test cases.

Intro comments template
# Programmers: [your names]
# Course: CS151, Dr. Rajeev  
# Date:
# Lab Number:
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]
Function decomposition
Your program should have a function for each of the following tasks. Practice iterative development: implement each item according to the instructions section below and then test that your code still works before proceeding onto the next item.

A function load_name_list that, given a filename (as a string), loads the names from the corresponding file and returns them in list of strings.
A function pop_random_name that, given a list of strings representing names, chooses a random name, removes it from the list, and returns it. Use the random.randrange function to implement this behavior.
A main function to drive the program.
Submission
One submission per team including all member names.

GitHub: Completed .py file (including intro and algorithm comments).
