"""
Create a variable named carname and assign the value Volvo to it.
"""

def answer2(z):
    if user_input == 'carname = "Volvo"':
        print("Your answer is correct!")
    elif user_input[0] == " ":
        print("Try to remove the space at the start of your input") 
    elif user_input == 'carname="Volvo"':
        print("Your answer is correct!")
        print("Next time try to insert a space between the variable name and the equal sign")  
        print("Next time try to insert a space between the the equal sign and the value of the variable")  
    elif user_input == 'carname= "Volvo"':
        print("Your answer is correct!") 
        print("Next time try to insert a space between the the equal sign and the value of the variable ") 
    elif user_input == 'carname ="Volvo"':
        print("Your answer is correct!")
        print("Next time try to insert a space between the variable name and the equal sign")             
    else:
        print("Unknown input.")
        print("Try to respect the readability rules")
print("In the input, write with the right syntax how to declare a variable named carname and to assign it the value Volvo")
user_input = input("Input here your answer: \n")
answer2(user_input)
