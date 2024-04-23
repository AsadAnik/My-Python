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
# Using of the format() function
price = 12.01
formatedText = "The price is {}".format(price)
print("Formated Text : ", formatedText)

# Using of the F-Strings formatting way
formatedTextWithFString = f"The price is {price}"
print("Formated Text With FString : ", formatedTextWithFString)

# Display price in 2 decimals
newPrice = 24
textWithFString = f"This is new price {newPrice: .2f} dollar"
print("New Text With FString : ", textWithFString)
print("\n")


# ESCAPE CHARACTERS
# Example with \" this symbol
escapeText = "We are the so-called \"Vikings\" form the north."
print(escapeText)
print("\n")


# STRING METHODS
'''
1. capitalize()
2. casefold()
3. center()
4. count()
5. encode()
6. endswith()
7. expandtabs()
8. find()
9. format()
10. format_map()
11. index()
12. isalnum()
13. isalpha()
14. isascii()
15. isdecimal()
16. isdigit()
17. isidentifier()
18. islower()
19. isnumeric()
20. isprintable()
21. isspace()
22. istitle()
23. isupper()
24. join()
25. ijust()
26. lower()
27. istrip()
28. maketrans()
29. partition()
30. replace()
31. rfind()
32. rindex()
33. rjust()
34. rpartition()
35. rsplit()
36. rstrip()
37. split()
38. splitlines()
39. startswith()
40. strip()
41. swapcase()
42. title()
43. translate()
44. upper()
45. zfill()
'''

# capitalize()
txt = "hello, and welcome to my world."
txtCap = txt.capitalize()
print("capitalize() - ", txtCap)


# casefold()
txt2 = "Hello, And Welcome To My World."
txt2Case = txt2.casefold()
print("casefold() - ", txt2Case)


# center(gaps)
txt3 = "banana"
txt3Cen = txt3.center(20)
print("center(gaps) - ", txt3Cen)

# fill all gaps with "0"
txt3Cen2 = txt3.center(20, "0")
print("center(gaps, fills) - ", txt3Cen2)


# count()
txt4 = "I love Apples, Apple are my favorite fruit."
txt4Count = txt4.count("Apple")
print("count(value) - ", txt4Count)


# count(value, start, end)
txt4Count2 = txt4.count("Apple", 10, 24)
print("count(value, start, end) - ", txt4Count2)


# encode()
# By default it will encode with UTF-8 string,
txt5 = "My name is Asad"
txt5Encode = txt5.encode()
print("encode() - ", txt5Encode)


# encode(encoding="ascii", errors="backslashreplace")
# errors can be ("backslashreplace" / "ignore" / "namereplace" / "replace" / "xmlcharrefreplace")
txt5Encode2 = txt5.encode(encoding="ascii", errors="backslashreplace")
print("encode(encoding=\"ascii\", errors=\"backslashreplace\") - ", txt5Encode2)


# endswith(value)
txt6 = "Hello, welcome to my world."
txt6Endswith = txt6.endswith(".")
print("endswith(value) - ", txt6Endswith)


# endswith(value, start, end)
txt6Endswith2 = txt6.endswith("my world.", 5, 11)
print("endswith(value, start, end) - ", txt6Endswith2)


# expandtabs(value)
txt7 = "H\te\tl\tl\to"
txt7Exndtabs = txt7.expandtabs(4)
print("expandtabs(value) - ", txt7Exndtabs)


# find(value)
# find(value, start, end)
txt8 = "Hello, welcome to my world."
txt8Find = txt8.find("welcome")
print("find(value) - ", txt8Find)


# index(value)
# index(value, start, end)
txt10 = "Hello, welcome to my world."
txt10Index = txt10.index("welcome")
print("index(value) - ", txt10Index)


# isalnum()
txt11 = "Hello, welcome to my world."
txt11Isalnum = txt11.isalnum()
print("isalnum() - ", txt11Isalnum)


# isalpha()
txt12 = "world 77"
txt12Isalpha = txt12.isalpha()
print("isalpha() - ", txt12Isalpha)


# isascii()
txt13 = "Hello, welcome to my world."
txt13Isalnum = txt13.isalnum()
print("isalnum() - ", txt13Isalnum)


# isdecimal()
txt14 = "1211"
txt14Isalpha = txt14.isdecimal()
print("isdecimal() - ", txt14Isalpha)


# isdigit()
txt15 = "1233"
txt15Isdigit = txt15.isdigit()
print("isdigit() - ", txt15Isdigit)


# isidentifier()
txt16 = "Hello, welcome to my world."
txt16Isidentifier = txt16.isidentifier()
print("isidentifier() - ", txt16Isidentifier)


# islower()
txt17 = "Hello, welcome to my world."
txt17Islower = txt17.islower()
print("islower() - ", txt17Islower)


# isnumeric()
txt18 = "1234"
txt18Isnumeric = txt18.isnumeric()
print("isnumeric() - ", txt18Isnumeric)


# isprintable()
txt20 = "Hello! Are you #1?"
txt20Isprintable = txt20.isprintable()
print("isprintable() - ", txt20Isprintable)


# isspace()
txt21 = "    "
txt21Isspace = txt21.isspace()
print("isspace() - ", txt21Isspace)


# istitle()
txt22 = "Hello"
txt22Istitle = txt22.istitle()
print("istitle() - ", txt22Istitle)


# isupper()
txt23 = "HELLO ALL I AM HERE."
txt23Isupper = txt23.isupper()
print("isupper() - ", txt23Isupper)


# join()
# string.join(iterable)
txt24 = ("Asad", "Anik", "Musa")
txt24Join = "join-me-there".join(txt24)
print("join() - ", txt24Join)

txt25 = {
    "name": "Asad",
    "age": 25,
    "city": "San Francisco",
}

mySeparator = "TEST"
txt25Join = mySeparator.join(txt25)
print("join() - ", txt25Join)


# ljust(value)
# string.ljust(length, character)
txt26 = "banana"
txt26Ljust = txt26.ljust(20)
print("ljust() - ", txt26Ljust, "this was left side wide")


# lower()
# string.lower()
txt27 = "Hello My Friends"
txt27Lower = txt27.lower()
print("lower() - ", txt27Lower)


# maketrans(value1, value2, value3)
# str.maketrans(x, y, z)
txt28 = "Hello, Sam!"
txt28Maketrans = str.maketrans("S", "M")
txt28Translated = txt28.translate(txt28Maketrans)
print("maketrans() - ", txt28Translated)

# Using with the mapping table
txt29 = "Good night Sam!"
x = "mSa"
y = "eJo"
myTable1 = str.maketrans(x, y)
txt29Translated = txt29.translate(myTable1)
print("str.translate() - ", txt29Translated)

# Another mapping table
txt30 = "Good night Sam!"
x = "mSa"
y = "ejo"
z = "odnght"
myTable2 = str.maketrans(x, y, z)
txt30Translated = txt30.translate(myTable2)
print("str.translate() - ", txt30Translated)


# partition(value)
# string.partition(value)
txt31 = "Good early night Sam for you!"
txt31Partition = txt31.partition("night")
print("partition() - ", txt31Partition)


# replace(oldValue, newValue, count)
# string.replace(oldvalue, newvalue, count)
txt32 = "Good night Sam for you!"
txt32Replace = txt32.replace("Sam", "Anik")
print("replace() - ", txt32Replace)

# Replace the two first occurrence of the word "one":
txt33 = "Good night Sam for you!, Sam is my favorite developer. And Sam is good programmer too."
txt33Replace = txt33.replace("Sam", "Anik", 2)
print("replace() - ", txt33Replace)


# istrip()
# string.lstrip(characters)
txt34 = "    mango    "
txt34Lstrip = txt34.lstrip()
print("lstrip() - ", txt34Lstrip)


# rfind()
# string.rfind(value, start, end)
txt34 = "Made is Bangladesh!"
txt34Rfind = txt34.rfind("is")
print("rfind(value) - ", txt34Rfind)


# rindex()
# string.rindex(value, start, end)
txt35 = "Manufacturer in Bangladesh"
txt35Rindex = txt35.rindex("in")
print("rindex(value) - ", txt35Rindex)


# rjust()
# string.rjust(length, character)
txt36 = "Apple"
txt36Rjust = txt36.rjust(10)
print("rjust() - ", txt36Rjust)


# rpartition()
# string.rpartition(value)
txt37 = "I love to drink mineral water"
txt37Rpartition = txt37.partition("mineral")
print("partition() - ", txt37Rpartition)


# rsplit()
# string.rsplit(separator, maxsplit)
txt38 = "drink, water, cherry, banana, mango"
txt38Rsplit = txt38.rsplit(", ")
print("rsplit() - ", txt38Rsplit)


# rstrip()
# string.rstrip(characters)
txt39 = "    banana    "
txt39Rstrip = txt39.rstrip()
print("rstrip() - ", txt39Rstrip, "is my favorite fruit")


# split()
# string.split(separator, maxsplit)
txt40 = "welcome to Jumanji"
txt40Split = txt40.split()
print("split() - ", txt40Split)

# Split the string, using comma, followed by a space, as a separator:
txt41 = "Hello, welcome to, Jumanji"
txt41Split = txt41.split(", ")
print("split() - ", txt41Split)

# Split the string into a list with max 2 items:
txt42 = "apple#orange#mango#cherry#banana"
txt42Split = txt42.split("#")
print("split() - ", txt42Split)


# splitlines()
# string.splitlines(keeplinebreaks)
txt43 = "Thank you for the music\nWelcome to the jungle"
txt43Splitlines = txt43.splitlines()
print("splitlines() - ", txt43Splitlines)


# startswith()
# string.startswith(value, start, end)
txt44 = "Hello, welcome to my world."
txt44Startswith = txt44.startswith("Hello")
print("startswith() - ", txt44Startswith)


# strip()
# string.strip(characters)
txt45 = "    banana    "
txt45Strip = txt45.strip()
print("strip() - ", txt45Strip)

# Remove the leading and trailing characters:
txt46 = ",,,,,rrttgg.....banana....rrr"
txt46Strip = txt46.strip(",.grt")
print("strip() - ", txt46Strip)


# swapcase()
# string.swapcase()
txt47 = "Hello My Name Is PETER"
txt47Swapcase = txt47.swapcase()
print("swapcase() - ", txt47Swapcase)


# title()
# string.title()
txt48 = "Hello My Name Is PETER"
txt48Title = txt48.title()
print("title() - ", txt48Title)


# translate()
# string.translate(table)
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
txt49Dics = {84: 77}
txtOne = "Hello MacBook!"
txt49DicsTranslate = txtOne.translate(txt49Dics)
print("translate() - ", txt49DicsTranslate)

# Use a mapping table to replace
txt50 = "Hello My Name Is PETER"
myTable = str.maketrans("P", "R")
txt50Translated = txt50.translate(myTable)
print("str.translate() - ", txt50Translated)

# The same example as above, but using a dictionary instead of a mapping table:
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

# The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))


# upper()
# string.upper()
txtNormal = "I am the normal text here"
txtNormalToUpper = txtNormal.upper()
print("upper() - ", txtNormalToUpper)


# zfill()
# string.zfill(len)
txt = "50"
txtZfill = txt.zfill(10)
print("zfill() - ", txtZfill)

# adding with strings
b = "welcome to the jungle"
print(b.zfill(50))
