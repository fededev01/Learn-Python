from util.functions import print3

print("Input all correct ways to write a simple program which prints a string in Python.")

print("1")
print('print("Hello")')
print("2")
print('      print("Hello") ')
print("3")
print('print(Hello)')
print("4")
print("print('Hello')")
print("Hint: Here there are two right ways to print a string. ")
user_input = int(input("insert here your first answer: \n"))
user_input2 = int(input("Insert here your second answer: \n"))
print3(user_input,user_input2)