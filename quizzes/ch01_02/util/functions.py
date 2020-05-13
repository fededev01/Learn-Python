def names(x):
    if x == 1:
        print("Your answer is wrong, come back to study!")
    elif x == 2:
        print("Your answer is wrong, come back to study!")    
    elif x == 3:
        print("Your answer is correct! Congratulations!") 
    else:
        print("Unknown input")
        

def variables1(z):
    if z == "a":
      print("Your answer is wrong, come back to study!")
    elif z == "b":
      x = 5
      y = 7
      print("Your answer is correct!")
      print("Let's see how does the code works:")
      print("5+7:") 
      print(x+y)
    elif z == "c":
        print("Your answer is wrong, come back to study!")
    else:
        print("Unknown input.") 


        
def variables2(z):
    if z == 'carname = "Volvo"':
        print("Your answer is correct!")
    elif z[0] == " ":
        print("Try to remove the space at the start of your input") 
    elif z == 'carname="Volvo"':
        print("Your answer is correct!")
        print("Next time try to insert a space between the variable name and the equal sign")  
        print("Next time try to insert a space between the the equal sign and the value of the variable")  
    elif z == 'carname= "Volvo"':
        print("Your answer is correct!") 
        print("Next time try to insert a space between the the equal sign and the value of the variable ") 
    elif z == 'carname ="Volvo"':
        print("Your answer is correct!")
        print("Next time try to insert a space between the variable name and the equal sign")             
    else:
        print("Unknown input.")
        print("Try to respect the readability rules")        