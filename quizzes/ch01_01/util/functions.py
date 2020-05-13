def print1(z):
    if z == "print":
        print("Your answer is correct!")
    else:
        print("Your answer is wrong, come back to study!")        

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