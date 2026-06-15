"""
Control Flows: 
    - conditional statements:
        - if...else
        - if...elif...else
        - ternary operator
        - match...case

    - loops:
        - for...loop
        - while
"""

output = "" # globa variable 

light_status = "OFF"

# - if...else
if light_status == "ON": # condition
    output = "Turning lights ON" 
else: # focuses on the default incase the condition outcome is False 
    output = "Turning lights OFF!"   

# if...elif...else
water_tap = "RUNNING"
if light_status != "ON" and water_tap != "CLOSED":
    output = "lights are on but it wont flood the house"
elif light_status =="OFF" and water_tap == "RUNNING":
    output = "It will flood!" 
else: 
    output = "go home!"

# ternary operator => this simplifies a conditoin inot one line 
output = "Turning lights ON" if light_status == "OFF" else  "Turning lights OFF!"

#  match case => swicth scenario
color ="BLUE"

match (color): 
    case "BLUE":
        output = "blue is the color"
    case "RED":
        output = "red is the colors"
    case _: # depicts default
        output = "I dot know" 

#  for .. loop
fruits = ["mangoes","bananas", "pineapples", "kiwi", "watermelon", "oranges", "beetroots"]

for fruit in fruits:
    print(f"=>>> {fruit.upper()}") 

basket_size = len(fruits)

while basket_size > 0:
    if basket_size == 0:
        pass 
    else: 
        print("you still have fruits!")
        fruits.pop()
        basket_size = len(fruits)

fruits = ["mangoes","bananas", "pineapples", "kiwi", "watermelon", "oranges", "beetroots"]
basket_size = len(fruits)

# ============ Order of exeution implication example ============
# while basket_size > 0:
#     print("you still have fruits!")
#     if basket_size == 0:
#         pass 
#     else: 
#         fruits.pop()
#         basket_size = len(fruits)

# order of execution difference        
# x = 0 
# while x <=10: 
#     print(x)
#     x+=1 # increment by 1
# print("------------------")
# x=0
# while x <=10:
#     x+=1 # increment by 1
#     print(x) 
# ============ Order of exeution implication example ============


#  if using numbers as the ranges
# range(10): moves from 0 to 9
# range(1, 10): moves from 1 to 9
# range (2, 18, 2): moves from 2 to 17 with a step of 2
for i in range(2, 18, 2):
    print(i)

print("=============================================")
print(output)
print("=============================================")