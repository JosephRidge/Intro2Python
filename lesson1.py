"""
COMMENTS: 
    - preceded the statement with a # 
    - user a multiline string """ """
    - Importance:
        - add extra information especially when collaboarating or maintain the project
"""

"""
VARIABLES: 
- define before use
- types:
    - global variable (accessed all throughout) 
    - local variables (constrained in a particular section)

"""
student_name = "JR" 
student_name = "JD"
output =""
output = student_name

#  standard input
# input()
# input("What is the color of the sky right now?")
# output = input("What is the color of your favorite car? ")

# print("Hello World")
# print(student_name)

# standard error
# print(age) # returns NameError: name 'age' is not defined


"""
DATA TYPES: 
    - String:
        - def: collection of characters
        - enclosed in between either single quotes '' or double quotes ""
        - class: str() => <class 'str'>
        - we can use the str() method to convert from different data types to strings
        - has in-built methods
        - slicing
        - immutable in nature 
    - Numbers:
        - Integers:
            - number that starts from 0 to -ve infinity and 0 to +ve infinity
            - int(): <class 'int'>
            - whole number
            - inbuilt methods

        - Floating
        - Complex:
            - <class 'complex'>
    - Lists:
        - Set
        - Array
        - Tuple
        - Dictionary

"""

output = "John Doe"
# output = 'John's Cows' # SyntaxError: unterminated string literal (detected at line 55)
output = 'John\'s Cows' # \ => an escape characte
output = "John's Cows" 
johns_cows = "John's-Cows are really plump and color white" 

#  extract characters/ words from the string 
output = johns_cows[2]
output = johns_cows[0]
output = johns_cows[6]

# slicing - statr and stop  => parts start:stop
output = johns_cows[0 :7 ]

# slicing with a step (skipping) => parts: start:stop:step
output = johns_cows[0:7:1]
output = johns_cows[0:7:2] # => Jh'-

knowledge_base = "encyclopedia britannica"
output = knowledge_base[0: :2]

output = len(knowledge_base) # len() => returns the size of  a list 
output = type(knowledge_base) # type() =>  gives us the data type as output
# knowledge_base[0] = 'a' # TypeError: 'str' object does not support item assignment => immmutability of string elements
knowledge_base = knowledge_base + " year" + str(2026) + " Voila!!" # string concatenation => you are combining more than one string into one
output = knowledge_base

output = f"{knowledge_base} 2026 is an awesome year to learn and do as much as possible, arent those {johns_cows}"
# for letter in knowledge_base:
#     print(letter)

# to parse or convert a data type to a string we use the str() class and pass in the varibale as a paramater
numberOne = 10 
output = type(numberOne)
output = f"Junior turns {numberOne} tomorrow"
output = "Junior turns "+ str(numberOne) + " tomorrow" # conctenation and string conversion 

#  methods => help reduce the lines an dcomplexities of your codebases
output = knowledge_base.lower() # transforms it to lowercase 
output = knowledge_base.upper() # transforms it to lowercase  

knowledge_base = "EnCyClOpEdIa BrItAnNiCa"
output = knowledge_base.swapcase()
output = knowledge_base.lower()
output = knowledge_base.find('I')





#integers
current_year = 2026
yob = 2000

age = current_year - yob 
output = age
output = type(age)
user_age = "23" # input("Enter your age: ")
output = user_age
output = type(user_age)
output = len(user_age)
user_age = int(user_age)
output = type(user_age) 
# output = len(user_age) # TypeError: object of type 'int' has no len() => you cannot get the length of an integer

# Floating number => a number that has a decimal 
weight = 20.2
height = 60.5
output = height
output = type(height)

#  complex numbers 
value = 2j
output = value
output = type(value)


# standard output
print("======================================")
print(output)
print("======================================")
