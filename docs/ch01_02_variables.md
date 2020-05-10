# Variables
If you want go to the main page, click [here](https://fededev01.github.io/Learn-Python).
If you want come back the summary, click [here](https://fededev01.github.io/Learn-Python/ch00_summary).

## Introduction
Variables play a very important role in most programming languages, and Python is no exception. 
Unlike other programming languages, Python has no command for declaring a variable.
A variable allows you to store a value by assigning it to a name, which can be used to refer 
to the value later in the program.
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.
To assign a variable, use one equals sign.
Assigning a variable doesn't produce any output at the Python console.
Variables can be reassigned as many times as you want, in order to change their value.

### How does it works

```python
x = 7
print(x)
```

The output will be the following:
```output
7
```

Now, if you want add 3 to x, you will write this:
```python
print(x + 3)
```

And the output will be this:
```output
10
```

Note that after the addition x+3, the value assigned to x is 7 yet.

Another example of using variables in Python, is this:
```python
x = 5
y = "John"
print(x)
print(y)
```
Output will be:
```output
5
John
```

The variables stores its value throughout the program.


## Types

In Python, variables don't have specific types, so you can assign a string to a variable, 
and later assign an integer to the same variable.
String variables can be declared either by using single or double quotes:

Start by assigning to x a float number
```python
x = 123.456
print(x)
```

The output of the code below will be the following:
```output
123.456
```

Now, let's assign to x a string
```python
>>> x = "This is a string"
>>> print(x + "!")
```

The output of the code below will be the following:
```output
This is a string!
```

To avoid mistakes, try to avoid overwriting the same variable with different data types.

## Variables Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

>> Legal variable names:
> myvar = "John"
> my_var = "John"
> _my_var = "John"
> myVar = "John"
> MYVAR = "John"
> myvar2 = "John"
> this_is_a_normal_name = "John"

>> Illegal variable names:
> 2myvar = "John"
> my-var = "John"
> my var = "John"
> 123abc = "John"
> spaces are not allowed
