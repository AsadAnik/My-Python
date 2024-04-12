# VARIABLES IN PYTHON
myNum = 12
myName = "Asad"

print("My name is : {} and the number is : {}".format(myName, myNum))


# TELLING THE VARIABLE WITH CASTING
myNameWithCast = str("Asad Anik")
myNumWithCast = str(myNum)  # String Number = '12'
myFoatData = float(12)  # Float Number = 12.0

print("My Number with string casting: {}".format(myNumWithCast))
print("My Float data number is : {}".format(myFoatData))


# NOW LET'S CHECKING THE TYPES
check_myNum_type = type(myNum)
check_myName_type = type(myName)

print("My Number Type checked with myNum : {} \n Type checked with myName : {}".format(check_myNum_type,
                                                                                       check_myName_type))

# ASSIGNING THE MULTIPLE VARIABLES WITH VALUES
''' Many Values to Multiple Variables
aa = 1
bb = 2
cc = 3
'''
aa, bb, cc = 1, 2, 3
print("aa = {} -- bb = {} -- cc = {}\n".format(aa, bb, cc))


# ONE VALUE TO MULTIPLE VARIABLES
''' One value will be assign to multiple variables
num1 = 12 
num2 = 12
'''
num1 = num2 = 12
print("num1 = {} -- num2 = {}".format(num1, num2))


# UNPACKING THE COLLECTION FROM LIST OR TUPLE
cars = ["Ford", "Mercedes", "BMW"]
one, two, three = cars
print("The Values for the Cars here - one = {} - two = {} - three = {}\n".format(one, two, three))


# GLOBAL AND LOCAL VARIABLES
# Global Variable
iAmGlobal = True


def checkScope():
    print("Global variable iAmGlobal - {}".format(iAmGlobal))


checkScope()


# Local Variable
def checkScope2():
    iAmLocal = True
    print("Local variable iAmLocal - {}".format(iAmLocal))


checkScope2()


# Local Scope but Global Variable with Scope
def checkScope3():
    global iAmLocalButGlobal
    iAmLocalButGlobal = True

    print("Local variable with Global Scope iAmGlobal - {} (Local Scope)".format(iAmGlobal))


checkScope3()
print("Local variable with Global Scope iAmGlobal - {} (Global Scope)".format(iAmGlobal))

# Checking the Scope with an Example
myScope = "I am Global with Global"


def myFunction():
    global myScope
    myScope = "I am Local but Global"
    print("From Local - {}".format(myScope))


myFunction()
print("From Global - {}".format(myScope))
