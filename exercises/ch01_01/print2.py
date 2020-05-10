print('Insert the missing part of the code below to output "Covid19".')
print("The missing parts are where you see three ellipsis")
print('...("Covid19"...')
user_input1 = input("Insert here your answer to first missing part: \n")
if user_input1 == "print":
    print("Your answer is correct!")
else:
    print("Your answer is wrong, come back to study!") 
    print("If you want a hint, input 'hint'")
    print("If you don't want a hint, input 'quit' ")
    print("Obviously, if you'll print 'quit', you have to restart the program")
    hint = input("Insert here your choice")
    if hint == "hint":
        print("The first correct answer is 'print' ")
    elif hint == "quit":
        None   
    else:
        print("Unknown input")  
     
    

user_input2 = input("Insert here your answer to second missing part: \n")
if user_input2 == ")":
    print("Your answer is correct!")
else:
    print("Your answer is wrong, come back to study!")        
    print("If you want a hint, input 'hint'")
    print("If you don't want a hint, input 'quit' ")
    print("Obviously, if you'll print 'quit', you have to restart the program")
    hint = input("Insert here your choice")
    if hint == "hint":
        print("The first correct answer is 'print' ")
    elif hint == "quit":
        None   
    else:
        print("Unknown input")   