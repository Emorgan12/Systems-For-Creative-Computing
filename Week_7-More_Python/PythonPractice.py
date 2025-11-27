import datetime

mydict = {
    'carl' : 34,
    'alan': 25,
    'bob': 6,
    'danny': 3
}

#print in alphabetical order
for key in sorted(mydict.keys()):
    print("%s:%s" % (key, mydict[key]))

def word_count(string):
    my_string=string.lower().split()
    my_dict={}
    for item in my_string:
        my_dict[item] = my_dict.get(item, 0) + 1
    print(my_dict)

word_count(input("Enter a string: "))

def moveTower( height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower( height-1, fromPole, withPole, toPole)
        moveDisk( fromPole, toPole)
        moveTower( height-1, withPole, toPole, fromPole)

def moveDisk(frompole, topole):
    print("moving disk from", frompole, "to", topole)

moveTower( 3, "A", "B", "C")
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def birthday(self):
        year = input("Enter birth year (e.g., 1990): ")
        month = input("Enter birth month (1-12): ")
        day = input("Enter birth day (1-31): ")
        birthdate = datetime.date(int(year), int(month), int(day))
        return birthdate

    def calculate_age(self):
        birthdate = self.birthday()
        today = datetime.date.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age

Person1 = Person("John", 0)
Person1.age = Person1.calculate_age()
print("Today is:", datetime.date.today())
print(f"{Person1.name} is {Person1.age} years old.")

