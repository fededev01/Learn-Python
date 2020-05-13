from util.functions import names

print("Which of these is a valid variable name in Python?")
print("1")
print("a-variable-name")
print("2")
print("a variable name")
print("3")
print("A_VARIABLE_NAME")
choice = int(input("Input the number of your answer(eg '1', '2' or '3')\n"))
names(choice)       