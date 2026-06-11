"""
When handling operations we have two key players:
    - Operand
    - Operator

    Operators: 
        - Arithmetic Operators:
            - helping perfom matha operations (+, -, /, //, %, *, **)
        - Assignment Operators (+=, =, -=, /=,**=, *=,//=)
        - Comparison operators (>, <, <=, >=, ==, !=)
        - Boolean Operators ( and, or, not)
        - BitWise operators (|, && etc) => https://wiki.python.org/moin/BitwiseOperators
    
"""

output = "" #global variable
# Arithmetic Operators:
x = 10 
y = 12 

output = x + y # addition
output = x - y # subtraction
output = x * y # multiplication
output = x / y # division => always retursn a floating point number
output = x // y # floor division = > truncated value
output = x ** y # power 
output = x % y # returns to use the remainder => divisibility tests

# Assignment Operators (+=, =, -=, /=,**=, *=,//=) => assign what is on the rught to what is on the left
output = 90 # simple assignment
x  = 90
x += 10 # similar to x = x + 10  # addition and assignment
x -= 10 # similar to x = x - 10  # subtraction and assignment
x *= 10 # similar to x = x * 10  # multiplication and assignment
x **= 10 # similar to x = x ** 10  # power and assignment
x = 100 # reassignment
x /= 10 # similar to x = x / 10  # division and assignment
x = 100 # reassignment
x /= 6 # similar to x = x / 10  # division and assignment => iff we parse it to an inte we get  a truncated whole number
# x //= 6 # similar to x = x // 10  # floor division and assignment

output = int(x) # converting the value of the division outcome to an integer

x = 10
x %= 5 # simple divisblity test of 5
x =10
x %= 4 # simple divisblity test of 4
x =15
x //= 4 # floor division test of 4

output = x

# Comparison operators (>, <, <=, >=, ==, !=)

tank_a = 100 
tank_b = 200

output = tank_a > tank_b  # greater than 
output = tank_a < tank_b  # less than 
output = tank_a >=  tank_b  # greater than  or equal to 
tank_a = 200 
output = tank_a >=  tank_b  # greater than  or equal to 
output = tank_a <=  tank_b  # less than  or equal to 
output = tank_a == tank_b # checking equality
tank_a = 150
output = tank_a == tank_b # checking equality
output = tank_a != tank_b # checking equality

# Boolean Operators ( and, or, not)
tank_a = 100
tank_b = 200
tank_c = 400

output = (tank_a > tank_b and tank_b < tank_c ) 
output = (tank_a < tank_b and tank_b < tank_c ) # and requires ythat both/ all condirionts are satisifed
output = (tank_a > tank_b or tank_b < tank_c )  # or requires at least one true outcome
output = not (tank_a > tank_b or tank_b < tank_c )  # note negates the final outocme
print("=============================================")
print(output)
print("=============================================")