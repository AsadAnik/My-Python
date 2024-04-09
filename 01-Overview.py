# SEE THE FIRST THING AS VARIABLES
myName = input("Enter your name: ")
print("Hello " + myName + "!")

# CALCULATING THE AGE BY USERS PROMPT
myBirthDate = int(input("Enter your birth date: "))

myAge = 0
currentYearRunning = 2024

if myBirthDate >= currentYearRunning:
    myAge = myBirthDate - currentYearRunning
else:
    myAge = currentYearRunning - myBirthDate

print("Your Age is", str(myAge))

# LET'S SEE THE FUNCTIONS ON PYTHON HERE
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


def compareBigger(number1, number2):
    if number1 == number2:
        return False

    if number1 > number2:
        return number1
    else:
        return number2


comparedBigger = compareBigger(num1, num2)

if comparedBigger:
    print("{} is bigger number".format(comparedBigger))
else:
    print("Compare not possible here")

# LET'S SEE NOW THE LOOPING WITH PYTHON
carList = ['Ferrari', 'Volkswagen', 'BMW', 'Mercedes', 'Range-Rover']

for car in carList:
    print(car)

print('\n')

# Break statement
for car in carList:
    if car == 'BMW':
        break
    print("After Breaking - ", car)

print('\n')

# Continue statement
for car in carList:
    if car == 'Mercedes':
        continue
    print("Continue with - ", car)

# INLINE CONDITIONS
iAmAdult = "YES, I'm an Adult" if myAge >= 18 else "NO, I'm not an Adult"
print("Checking my Adult-ness = {}".format(iAmAdult))


# OOP OVERVIEW HERE
class Overview:
    # Constructor/Initializer method
    def __init__(self, myName, myBirthDate):
        self.myName = myName
        self.myBirthDate = myBirthDate

    # Getter method..
    def displayName(self):
        print("My name is {}".format(self.myName))

    # Setter method..
    def setName(self, myName):
        self.myName = myName
        print("My name is {}".format(self.myName))

    def setBirthDate(self, myBirthDate):
        self.myBirthDate = myBirthDate
        print("My birth date is {}".format(self.myBirthDate))

    def displayAge(self):
        myAge = self.myBirthDate - currentYearRunning if self.myBirthDate > currentYearRunning \
            else currentYearRunning - self.myBirthDate
        print("My age is {}".format(myAge))


myOverview = Overview(myName, myBirthDate)
myOverview.displayName()
myOverview.displayAge()

myOverview.setName("Anika")
myOverview.setBirthDate(2003)
myOverview.displayAge()


