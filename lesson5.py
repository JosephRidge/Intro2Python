"""
Functions:
    - collection of statements/ instructoins that achieve a particur goal eg welcomeMessage
    - types of functions:
        - parameterized function
            - key words: def
        - non-parameterized function
            - key words: def
        - lambda function/ anonymous function
            - key words: lambda

"""
# dependencies
import datetime as dt

output = "" # global variable 

# non-paramterized function
#  defined a function
def welcomeMessage():
    print("Welcome to DSA 2026!")

def welcomeMessageTwo():
    class_name = "DSA 2026" # regarded as a local variable
    print(f"Welcome to the awesome {class_name}!")

# call the function => eexecuting the function
# welcomeMessage()
# welcomeMessageTwo()
# print(class_name) # NameError: name 'class_name' is not defined => we are accessng local varibale globally
 
# parameterized functions, the take in parameters this is good/ advantageous since it allows customization
def welcomeClient(name):
    print(f"Welcome home {name}!")

welcomeClient("John Doe")

""""
BANK OF DSA: 
    - users
    - conduct transactions
        - date and time
        - amount 
        - person that triggred the transaction
    - withdraw (reducing your current amount)
    - deposit (adding an amount)
"""
def userDetails(name, current_amount, top_up_amount, widthdraw_cash):
    current_amount += top_up_amount # always increment
    current_amount -= widthdraw_cash
    user = {
        "name":name,
        "amount": current_amount,
        "top_up":top_up_amount,
        "transaction_date":dt.datetime.now()
    }

    return user

### Repeating code
#  user one
user_one_name = "John Doe"
user_one_amount = 100
date_time_transaction = dt.datetime.now()
user_one_top_up_amout = 20 
user_one_remove_amout = 5 
user_one_amount += user_one_top_up_amout 
user_one_amount -= user_one_remove_amout 

user_two_name = "Johanna Does"
user_two_amount = 100
date_time_transaction = dt.datetime.now()
user_two_top_up_amout = 20 
user_two_top_up_amout += user_two_top_up_amout 
user_one_amount -= user_one_remove_amout 

user_three_name = "Johanness Joes"
user_three_amount = 100
date_time_transaction = dt.datetime.now()
user_three_top_up_amout = 20 
user_three_top_up_amout += user_three_top_up_amout 
user_one_amount -= user_one_remove_amout 

#  using functions
user_one = userDetails("JOhn Doe", 100, 20,5)
user_two = userDetails("Johanna Does", 90, 50,6)
user_three = userDetails("Johanness Joes", 90, 50,7)


# lambda function => anonymous functoin
def nameOfFunciton():
    pass

amount = lambda x: x + 20

fruits = ["apples","mangoes","bananas"]

def formatText(text): 
    text = f"{text[0:2].upper()} {text[2:].lower()}" 
    return text

format_text = lambda text: formatText(text)

for fruit in fruits:
    print(format_text(fruit))

# print(amount(5))