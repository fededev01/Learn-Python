def print1(z):
    if z == "print":
        print("Your answer is correct!")
    else:
        print("Your answer is wrong, come back to study!")  


def first_answ(m):
    if m == "print":
        print("Your answer is correct!")
    else:
        print("Your answer is wrong, come back to study!") 
        print("If you want a hint, input 'hint'")
        print("If you don't want a hint, input 'quit' ")
        print("Obviously, if you'll print 'quit', you have to restart the program")
        hint = input("Insert here your choice\n")
        if hint == "hint":
            print("The first correct answer is 'print' ")
        elif hint == "quit":
            None   
        else:
            print("Unknown input") 
            
            
def second_answ(n):
    if n == ")":
        print("Your answer is correct!")
    else:
        print("Your answer is wrong, come back to study!")        
        print("If you want a hint, input 'hint'")
        print("If you don't want a hint, input 'quit' ")
        print("Obviously, if you'll print 'quit', you have to restart the program")
        hint = input("Insert here your choice: \n")
        if hint == "hint":
            print("The second correct answer is ')' ")
        elif hint == "quit":
            None   
        else:
            print("Unknown input")               
              

def print3(x,y):       
    if x == 1 and y == 4:   
        print("Both your answers are correct! Good job! ")
    elif x == 4 and y == 1:   
        print("Both your answers are correct! Good job! ") 
    elif x==1 and y==2:
        print("Your first answer is correct, but your second is wrong")
    elif x==4 and y==3:
        print("Your first answer is correct, but your second is wrong") 
    elif x==4 and y==2:
        print("Your first answer is correct, but your second is wrong")   
    elif x==1 and y==3:
        print("Your first answer is correct, but your second is wrong")
    elif x==2 and y==1:
        print("Your first answer is wrong, but your second is correct")
    elif x==3 and y==4:
        print("Your first answer is wrong, but your second is correct") 
    elif x==2 and y==4:
        print("Your first answer is wrong, but your second is correct")   
    elif x==3 and y==1:
        print("Your first answer is wrong, but your second is correct")  
    elif x==2 and y==2:
        print("Are you kidding me?")     
    elif x==3 and y==3:
        print("Are you kidding me?")
    elif x==2 and y==3:
        print("Both your answers are wrong.")            
    elif x==3 and y==1:
        print("Both your answers are wrong.")                    
    else:
        print("Unknown input.")       