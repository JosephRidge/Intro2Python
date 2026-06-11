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

"""
LISTS:
     - collection of items
     - some collections can be compose dof different data types

- Array List:
    - collection of items
    - class list: <class 'list'>
    - composed of more than one data type
    - encloded inside a [] - sqaure brackets
    - mutable in nature ( you can alter the values)
    - accessed by indexes
    - it has its own methods 
    - can convert to list using the list()

    refrences:
    - https://docs.python.org/3/tutorial/datastructures.html
    - https://www.w3schools.com/python/python_ref_list.asp

"""

output = "" # global variable
fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples"] # list
output = fruits
output = type(fruits)
output = fruits[-1] #accesing items within the list using and index
fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples"] # list
output = fruits [3:9] # slicing
#  methods: 
output = fruits.append("watermelon")
output = fruits

fruits.clear() # deleting elements wihtin the list
fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples"] # list
output = fruits.count("kiwi") # count of elments within the list
output = fruits.index("kiwi") # return tthe index of the first occurence of the element
fruits.sort() #sots elements in ascending order
output = fruits
output = len(fruits)
output = fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples", 1, 2, 3,100, 234, 23.4, 3j] # list with mixed data types
# fruits.sort() #fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples"] # list => sort only works with uniqform data
fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples"] # list
output = fruits
fruits[0] = "Pineapples" # mutable nature of  list
output =fruits

"""
Tuple: 
    - elements are enclosed within ()
    - the immutable in nature 
    - class tuple: <class 'tuple'>
    - can host different data tpes
    - contains its unique class methods
    - access them using indexes
    - can convert to tuple using the tuple()

    References:
    - https://www.w3schools.com/python/python_ref_tuple.asp
"""

colors = ("Red", "Green", "Blue")  
colors = ("Red", "Green", "Blue",12,34.5) # can capture mutliple  data types
output = colors
output = colors[1]
output = colors
# colors[1] = "Yellow" # TypeError: 'tuple' object does not support item assignment => returns error since tuples ar eimmutable in nature 
output = type(colors)
output = len(colors)

#  methods: 
output = colors.count("Red")
output = colors.index("Blue")


"""
Set: 
    - captures the unique elements in  list 
    - it is enclosed within {}
    - class set
    - items are accessed via indexes
    - it composed of it respective methods
    - can convert to set using the set()

    References:
    - https://www.w3schools.com/python/python_sets_methods.asp

"""
fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples"] # list
output = type(fruits)
fruits = { "bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples"}
output = type(fruits)
fruits = [ "bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples","bananas", "mangoes", "oranges", "kiwi","apples"] # list

output = set(fruits) # convert to set 
output = type(output)
output = list(fruits) # convert to list 
output = type(output)

team_one = {"M","E", "B","N","W"}
team_two = {"M","E","A","B", "C", "D", "E"}

output = team_one
output = team_two
output = team_one.difference(team_two) # returns to use the elemnts that are no present in both sets
output = team_one.intersection(team_two) # returns to us the common elmeent sin both tset one and two
output = team_one.symmetric_difference(team_two)

"""
Dictionary: 
    - key-value pair
    - class name dict: <class 'dict'>
    - it composed of methods
    - enclosed in {}

    References
    - https://www.w3schools.com/python/python_dictionaries_methods.asp
"""
student = {
    "name":"John Doe",
    "age":100, 
    "index":10234567
}

output = student
output = type(student)
output = student['name'] # accesing the values of the respective keys 

output = type(student)
output = list(student.values()) # returns a list composed of the values within the dictionary
output = list(student) # returns a list composed of the keys within the dictionary
output = set(student) # returns a list composed of the keys within the dictionary

print("=============================================")
print(output)
print("=============================================")