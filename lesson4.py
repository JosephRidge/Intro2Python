"""
Control Flows: 
    - conditional statements:
        - if...else
        - if...elif...else
        - ternary operarot
        - match scenario

    - loops
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



print("=============================================")
print(output)
print("=============================================")