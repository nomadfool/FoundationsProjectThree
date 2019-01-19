# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.president = None
        self.members = []

    def __str__(self):
        return ("\tName: %s\n\tDescription: %s\n\tMembers: %d\n" % (self.name, self.description, len(self.members)))


    def assign_president(self, person):
        # your code goes here!
        self.president = person

    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)

    def print_member_list(self):
        # your code goes here!
        total_age = 0

        print("Members: \n")
        for member in self.members:
            if member == self.president:
                print("- %s (%d years old, President) - %s.\n\n" % (member.name, member.age, member.bio))
                total_age += member.age
            else:
                print("- %s (%d years old) - %s.\n\n" % (member.name, member.age, member.bio))
                total_age += member.age

        avrage_age = total_age / len(self.members)
        print("Avrage age of the club: %.2f" % (avrage_age))
        print("---------------------------------")
