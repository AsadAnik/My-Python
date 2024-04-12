# STRING IN PYTHON
# Assign Value in String Variable
name = "Asad Anik"
print(name)
print("\n")


# Multiline String
multi_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
ut labore et dolore magna aliqua."""
print("Multi-line double quote string - ", multi_string)
print("\n")

# Also we can do with single quote
multi_single_q_string = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,'''
print("Multi-line single quote string - ", multi_single_q_string)

# Lets making figure out the very first element from the list
firstElementOfMyName = name[0]
lastElementOfMyName = name[-1]
print("First and Last name of my Element of name : ", firstElementOfMyName, lastElementOfMyName)

# Looping throw a String
for el in name:
    print(el)

# Check the length of a String
lengthOfName = len(name)
print("Name length here - ", lengthOfName)

# Searching / Checking a string from a value
searchedText = "Anik" in name
print("Searched the word from name : ", searchedText)

# Check the text is not present on strings-set
notFoundText = "Asad" not in name
print("Not found word from name : ", notFoundText)

# SLICING THE STRING
# letting it end at 3 index only
myText = "I am using MacBook for coding."
sliceText = myText[:3]
print("Slice Text : ", sliceText)

# letting start 3 and end 6 index
sliceText2 = myText[3:6]
print("Slice Text 2 : ", sliceText2)

# letting the text starts from 10 index only
sliceText3 = myText[10:]
print("Slice Text 3 : ", sliceText3)
print("\n")


# MODIFY THE STRING
# Uppercase String
uppercasedText = myText.upper()
print("Uppercased Text : ", uppercasedText)

# Lowercase String
lowercasedText = myText.lower()
print("Lowercased Text : ", lowercasedText)

# Removing Whitespaces / Trim the Text
removedWhiteSpaces = myText.strip()
print("Removed White Spaces : ", removedWhiteSpaces)

# Replacing the Text
worldText = "Hello, World"
replacedText = worldText.replace("Hello", "Hi")
print("Replaced Text : ", replacedText)

# Splitting the Text
splitText = replacedText.split(",")
print("Split Text : ", splitText)
print("\n")


# CONCATENATE THE STRING
text1 = "Hello"
text2 = "World"
concatenatedTexts = text1 + text2
concatenatedTextsWithSpace = text1 + " " + text2
print("Concatenated Text : ", concatenatedTexts)
print("Concatenated Text With Space : ", concatenatedTextsWithSpace)
print("\n")


# FORMAT THE STRING


