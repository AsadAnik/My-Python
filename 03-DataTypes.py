# DATA TYPES IN PYTHON
""" BUILT-IN DATA TYPES AND SPECIFIC TYPES
1. Number
2. Text
3. Sequence
4. Mapping
5. Set
6. Boolean
7. Binary
8. None
"""
# Number Types
# Int
num = 12
print(type(num))

# FLoat
myFloat = 1.2
print(type(myFloat))


# Text / String Type
string = "Hello World"
print(type(string))


# Sequence Types (List, Tuple, Range)
# List
myList = [1, 2, 3]
print(type(myList))

# Tuple
myTuple = (1, 2, 3)
print(type(myTuple))

# Range
myRange = range(1, 11)
print(type(myRange))


# Mapping Type (Dictionary)
myDics = {"name": "Ken Thomson", "age": 90}
print(type(myDics))


# Set Types (Set, Frozenset)
# Set
mySet = {"Apple", "Orange", "Banana"}
print(type(mySet))

# Frozen Set
myFrozenSet = frozenset({"Apple", "Orange", "Banana"})
print(type(myFrozenSet))


# Boolean Type
myBool = True
print(type(myBool))


# Binary Types (Bytes, ByteArray, MemoryView)
# Bytes
myBytes = b"Hello World"
print(type(myBytes))

# ByteArray
myByteArray = bytearray(5)
print(type(myByteArray))

# MemoryView
myMemoryView = memoryview(bytes(6))
print(type(myMemoryView))


# None Type
myNone = None
print(type(myNone))


print("\n")


# SPECIFIC DATA TYPES as,
"""
1. Int
2. Float
4. Complex
"""
# Int Number
numWithInt = int(6)
print(type(numWithInt))

# Float Number
numWithFloat = float(7)
print(type(numWithFloat))

# Complex Data
myComplexData = complex(1j)
print(type(myComplexData))

