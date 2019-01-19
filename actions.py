# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person
from sys import exit

my_name = "Rashed"
my_age = 38
my_bio = "Something wicked this way comes."
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("\n\nHello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    options_list = {
    "1" : "create a new club.",
    "2" : "Browse and join clubs.",
    "3" : "View existing clubs.",
    "4" : "Display members of a club",
    "-1" : "Close application."}

    print("----------------------------")
    print("What would you like to do?(pick a number):")
    
    for key in options_list:
        if key == "-1":
            print("%s) %s\n" % (key, options_list[key]))
        else:
            print("%s) %s\nor:" % (key, options_list[key]))

def create_club():
    # your code goes here!
    print("\n-----------------------------------")
    name = input("Name thy club: ")
    description = input("what's it all about? ")
    new_club = Club(name, description)
    print("Enter the numbers of the people you would like to recruit to your own club (-1 to stop): ")
    print("\n-----------------------------------\n")
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    key = 1

    for member in population:
        print("[%d] %s" % (key, member.name))
        key += 1

    while True:
        user_in = input("> ")
        
        if user_in == "-1":
            break
        elif user_in.isalpha() or int(user_in) > len(population) or int(user_in) < 1:
            print("Please enter a valid number: ")
        else:
            new_club.recruit_member(population[int(user_in) - 1])
    print("\n-----------------------------------")
    print("Here's your club:")
    print(new_club.name)
    print(new_club.description)
    new_club.print_member_list()
    clubs.append(new_club)

def view_clubs():
    # your code goes here!
    for club in clubs:
        print(club)

def view_club_members():
    # your code goes here!
    view_clubs()
    flag = False
    user_in = input("Enter the name of a club to see it's members (-1 to go back): ")
    while user_in != "-1":
        for club in clubs:

            if club.name.lower() == user_in.lower():
                print("\n-----------------------------------")
                club.print_member_list()
                view_clubs()
                print("Enter the name of a club to see it's members (-1 to go back): ")
                flag = True
        
        if flag == False:
            user_in = input("Please enter a valid club name: ")
        user_in = input("> ")

def join_clubs():
    # your code goes here!
    view_clubs()
    flag = False

    print("Enter the name of a club to see it's members(-1 to go back):")
    user_in = ""
    while user_in != "-1":
        user_in = input("> ")
        for club in clubs:

            if club.name.lower() == user_in.lower():

                if myself in club.members:
                    print("You're already in %s" % (club.name))
                    break

                club.recruit_member(myself)
                print("%s just joind %s!" %(myself.name, club.name))
                flag = True
        
        if flag == False:
            print("Please enter a valid club name: ")    

def application():
    # your code goes here!

    introduction()
    while True:
        options()
        choice = str(input("> "))

        if choice == "-1":
            exit("Goodbye!")

        elif choice == "1":
            create_club()

        elif choice == "2":
            join_clubs()

        elif choice == "3":
            view_clubs()

        elif choice == "4":
            view_club_members()

        else:
            print("That's not a valid option.\nPlease choose an option: ")

