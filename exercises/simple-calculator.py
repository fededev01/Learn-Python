while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
       add1 = float(input("Enter a number: "))
       add2 = float(input("Enter another number: "))
       resadd = str(num1 + num2)
       print("The answer is " + resadd)
   elif user_input == "subtract":
      sub1 = float(input("Enter a number: "))
      sub2 = float(input("Enter another number: "))
      resub = str(sub1 - sub2)
      print("The answer is " + resub)
   elif user_input == "multiply":
      mult1 = float(input("Enter a number: "))
      mult2 = float(input("Enter another number: "))
      resmul = str(mult1 - mult2)
      print("The answer is " + resmul)
   elif user_input == "divide":
      div1 = float(input("Enter a number: "))
      div2 = float(input("Enter another number: "))
      resdiv = str(div1 - div2)
      print("The answer is " + resdiv)
   else:
      print("Unknown input")
