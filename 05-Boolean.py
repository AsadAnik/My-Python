# Boolean in Python
print("10 > 9 = ", 10 > 9)
print("10 < 9 = ", 10 < 9)
print("10 <= 9 = ", 10 <= 9)
print("10 >= 9 = ", 10 >= 9)
print("10 == 9 = ", 10 == 9)
print("10 != 9 = ", 10 != 9)
print("10 == 10 = ", 10 == 10)


# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
print("bool(""\"Hello\") = ", bool("Hello"))
print("bool(15) = ", bool(15))


# Evaluate two variables:
x = "Hello"
y = 15
print("x = ", bool(x))
print("y = ", bool(y))


# Most Values are True
'''
1. Almost any value is evaluated to True if it has some sort of content.
2. Any string is True, except empty strings.
3. Any number is True, except 0.
4. Any list, tuple, set, and dictionary are True, except empty ones.
'''
print("bool(""\"abc\") = ", bool("abc"))
print("bool(123) = ", bool(123))
print("bool(['apple', 'cherry', 'banana']) = ", bool(["apple", "cherry", "banana"]))


# Some Values are False
'''
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 
And of course the value False evaluates to False.
'''
print("bool(False) = ", bool(False))
print("bool(None) = ", bool(None))
print("bool(0) = ", bool(0))
print("bool('') = ", bool(''))
print("bool([]) = ", bool([]))
print("bool(()) = ", bool(()))
print("bool({}) = ", bool({}))


'''
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
'''
class MyClass:
    def __len__(self):
        return 0


myClass = MyClass()
print("bool(myClass) = ", bool(myClass))
