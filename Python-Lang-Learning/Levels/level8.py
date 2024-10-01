# # Commit 1: Added string methods examples
# # Description: Demonstrating various string methods in Python

# # String Upper, Lower, Title, and Strip methods
# name = "   nitesh kushwaha   "
# print(name.upper())  # Converts string to uppercase
# print(name.lower())  # Converts string to lowercase
# print(name.title())  # Converts string to title case
# print(name.strip())  # Removes leading and trailing whitespaces

# # String Count and Replace methods
# print(name.count("h"))  # Counts the occurrences of 'h' in the string
# print(name.replace("kushwaha", "kushwah"))  # Replaces 'kushwaha' with 'kushwah'

# # String Isalpha, Isdigit, and Isspace methods
# print(name.isalpha())  # Checks if string contains only alphabets
# print(name.isdigit())  # Checks if string contains only digits
# print(name.isspace())  # Checks if string contains only whitespaces

# # Commit 2: Added split and join examples
# # Description: Demonstrating split and join methods in Python

# # String Split method
# name = "Nitesh Hello"
# res = name.split(' ')
# print(res)  # Splits the string into a list of words

# # String Join method
# name = ("nitesh", "kushwaha")
# x = " ".join(name)  # Joins the tuple into a single string
# print(x)

# # Commit 3: Added strip, lstrip, and rstrip examples
# # Description: Demonstrating strip, lstrip, and rstrip methods in Python

# # String Strip method
# name = "Chrisy"
# print(name.strip())  # Removes leading and trailing whitespaces
# print(name.strip("y"))  # Removes 'y' from the string

# # Commit 4: Added find and index examples
# # Description: Demonstrating find and index methods in Python

# # String Find method
# name = "akshay"
# print(name.find("z"))  # Returns the index of 'z' in the string
# print(name.find("h", 2, 5))  # Returns the index of 'h' in the specified range

# # String Index method
# print(name.index("a"))  # Returns the index of 'a' in the string

# # Commit 5: Added replace and count examples
# # Description: Demonstrating replace and count methods in Python

# # String Replace method
# name = "akshay"
# print(name.replace("akshay", "nitesh"))  # Replaces 'akshay' with 'nitesh'

# # String Count method
# name = "nitteshhttkk"
# print(name.count("t"))  # Counts the occurrences of 't' in the string
# print(name.count("t", 3, 5))  # Counts the occurrences of 't' in the specified range

# # Commit 6: Added startswith and endswith examples
# # Description: Demonstrating startswith and endswith methods in Python

# # String Startswith method
# name = "nitesh"
# print(name.startswith("n"))  # Checks if the string starts with 'n'

# # String Endswith method
# print(name.endswith("sh"))  # Checks if the string ends with 'sh'


# ! questions 

# name1 = "Princess Leia"
# print(name1.split())

# name2  = "Baby Yoda"
# print(name2.lstrip("Baby"))

# name3 = "Baby Yoda"
# print(name3.replace("Baby"  ,"Master"))

# ! lambda function 

example_List = [1, 9, 10]

# sqr = lambda x :x**2
# newls = []
# def printSqr():
#     for i in example_List:
#         newls.append(sqr(i))
#     print(newls)
# printSqr()


# print(list(map(lambda x :x**2 , example_List))) # in one line 
# print(list(map(lambda x:x**2 , example_List)))

#  ! recursion 

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


