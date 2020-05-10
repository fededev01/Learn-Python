
def answer1(z):
    if z == "a":
      print("Your answer is wrong, come back to study!")
    elif z == "b":
      x = 5
      y = 7
      print("Your answer is correct!")
      print("Let's see how does the code works:") 
      print(x+y)
    elif z == "c":
        print("Your answer is wrong, come back to study!")
    else:
        print("Unknown input.")    
                  
print("What is the value assigned to y?")
print("x = 5")
print("y = ...")
print("print(x + y)")
print("output is: 12")
print("Input 'a' if the code must be: y='7' ")
print("Input 'b' if the code must be: y=7 ")
print("Input 'c' if the code must be: y=='7' ")
print("Input the correct answer to make the code work correctly.")
user_choice = input("What value is assigned to y?\n")
answer1(user_choice)