# Emily Catanzariti, Angel Scott, Tim Hunt
# CS151, Dr. Rajeev
# 11/11/2021
# Lab: 8
# Program Inputs: name of file, choice of whether to pick a name
# Program Outputs: the name that was chosen

# random module
import random


# function load name list
def load_name_list(filename):
    name_list = []
    try:
        file = open(filename, "r")
        for line in file:
            name_list.append(line)
            random.shuffle(name_list)
        file.close()
    except "FileNotFoundError":
        print("file does not exist")
    return name_list


# function pop random name
# random.randrange
def pop_random_name(listnames):
    picked_index = random.randint(0, len(listnames))
    picked_name = listnames.pop(picked_index)
    listnames.remove(picked_index)
    return picked_name, listnames


# main function
def main():
    file_name = input("what is the name of your file?")
    file_name = str(file_name)
    file_name = file_name.lower().strip()
    list_of_names = load_name_list(file_name)
    while len(list_of_names) > 0:
        choice = input("would you like to choose a random name?")
        choice = choice.strip().lower()
        if choice == "yes":
            the_chosen_one, list_of_names = pop_random_name(list_of_names)
            print("the name picked was:", the_chosen_one)
        elif choice == "no":
            print("thank you for using this program")
        else:
            print("sorry input was invalid")
    if len(list_of_names) == 0:
        print("there are not more names to be picked. thank you for using this program")



main()
