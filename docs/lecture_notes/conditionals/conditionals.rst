
Conditionals
============

In Python when we need to make a decision we will use the :code:`if` statement. The :code:`if` statement is an example of what we call a conditional. The statement is called a conditional because we are going to be testing an expression and only executing the code inside that statement if the expression is true. These expressions are basically yes or no questions. 


:code:`if` Statement
--------------------

We know that we can ask a question with if statements, so lets look at some of the types of questions we can ask. In this first example we'll define a variable called temperature. If our variable is under 32, we're going to print "Brr, it's freezing out!". 

::

    temperature = 30

    if temperature < 32:
        print("Brr, it's freezing out!")

Our question here is :code:`temperature < 32` or in English "is the value of the variable temperature less than 32?" This statement is either true or false (if you think back to earlier you'll also know that this is a boolean value). 

We can then translate the entire if statement into English: "if the value of the temperature variable is less than 32 then print out the string 'Brr, it's freezing out!'". 

Comparisons
~~~~~~~~~~~

We're going to be using 6 comparisons for now

===================== ======
Meaning               Symbol
===================== ======
Less than             < 
Greater than          >
Less than or equal    <=
Greater than or equal >=
Equal                 ==
Not equal             !=
===================== ======

It is very important to note the equal statement. It has two equals signs, :code:`==` and not one. A single equal sign is how we assign variables, a double equal sign is how we test they are equal. 

::

    speed_a = 40
    speed_b = 40

    if speed_a == speed_b:
        print("The objects are moving the same speed.")

This example also shows us that we can compare two variables. 


Blocks
~~~~~~

In the if statements above you can see that we tell the interpreter what should be printed by indenting the line. We will use 4 spaces to indent each line. 

A set of lines that are grouped is called a block. In Python, indentation is used to denote a block. A block can be inside of another block. 

::

    code code code             #                 ---
    code code code             #                  |   <- Block 1
    code code code             #                  |
        code code code         # ---              |
        code code code         #  |  <- Block 2   |
        code code code         #  |               |
        code code code         # ---              |
    code code code             #                  |
    code code code             #                 ---

As you can see, block 2 here is actually part of block 1. 

Once an indentation level has been ended, if you go back to that level it starts a new block.

::

    code code code             #                 ---
    code code code             #                  |   <- Block 1
    code code code             #                  |
        code code code         # ---              |
        code code code         #  |  <- Block 2   |
        code code code         #  |               |
        code code code         # ---              |
    code code code             #                  |
    code code code             #                  |
        code code code         # ---              |
        code code code         #  |  <- Block 3   |
        code code code         #  |               |
        code code code         # ---              |
    code code code             #                  |
    code code code             #                 ---

In this example, block 2 and 3 are both part of block 1 but block 2 and block 3 are completely different blocks. 

In if statements, we can use blocks to execute multiple lines.

::

    a = 5

    if a < 6:
        print("This statement will print")
        print("This statement will also print")

    print("This statement is going to print")

In this example the output is the following

::
    
    This statement will print
    This statement will also print
    This statement is going to print

If we change our example so that the if statement is no longer true

::

    a = 100

    # 100 is not less than 6
    if a < 6:
        print("This statement will not print")
        print("This statement will also not print")

    print("This statement is going to print")

We only get one line of output. 

::
    
    This statement is going to print

The fact that the last print statement is not lined up with the if statement lets the interpreter know that this statement is not part of the if. 


Indentation
~~~~~~~~~~~

For this class, we will use 4 spaces for indentation. It is important to indent to the same level, a block with a line indented 4 spaces and then another indented 5 will cause an error. 

::

    a = 5

    if a < 6:
        print("This statement will print")
        print("This statement will also print")
         print("This statement will cause an error")

    # Our program will exit with an error before getting to this last print statement
    print("This statement is going to print")

The output from running this will include an error and never print our last print statement inside the if statement or the one outside of it. 

::

    This statement will print
    This statement will also print
    SyntaxError: unexpected indent


:code:`if-else` Statements
--------------------------

The else statement allows us to tell our program to do something if the expression is false. Going back to our temperature example, we can tell it to also print something if it is not freezing out. 

::

    temperature = 50

    if temperature < 32:
        print("Brr, it's freezing out!")
    else:
        print("It's not freezing out.")

When we run this example, the temperature is not less than 32. The else statement will execute and our output will be 

:: 
    
    It's not freezing out.

We can go back and change the temperature to 30 in the example and run it again.

::

    temperature = 30

    if temperature < 32:
        print("Brr, it's freezing out!")
    else:
        print("It's not freezing out.")

Now the temperature is less than 32 so we execute the print statement in the if block and then finish the if statement. Since the statement is true, we do not execute our else statement so we get the following output

::
    
    Brr, it's freezing out!


:code:`if-elif-else` Statements
-------------------------------

We can also write an if statement that has more than one expression. This is called an else-if. In Python an else-if uses the keyword :code:`elif`. 

::

    temperature = 30

    if temperature < 32:
        print("Brr, it's freezing out!")
    elif temperature > 90:
        print("Wow, it's really hot out")
    else:
        print("It's normal out.")

In this example, if the temperature is less than 32 we will print "Brr, it's freezing out!". 

We've also added another statement that is a combination of else and if. If the temperature is not less than 32, we test to see if it is above 90. If the temperature is above 90 our program will print "Wow, it's really hot out". 

Finally, if both of these statements are not true, our program will print "It's normal out."


Comparing Text
--------------

We can compare strings as well as numbers. For strings we'll only use the :code:`==` and :code:`!=` operators in this course. 

Remember from earlier that when we get user input it comes as a string. We can compare strings just like we did with numbers. 

::
    
    print("Enter the secret word:")
    secret_word = input()

    if secret_word == "wattlebird":
        print("Welcome to Gryffindor Tower")

What if someone types in "Wattlebird" with a capital "W"? Just like variable names, string comparisons are case sensitive in Python. "Wattlebird" would not equal "wattlebird" so that would be false.

If we want to accept any capitalizations, we can modify our program to make it so you can type "Wattlebird", "WATTLEBIRD" or any other capitalization pattern. We'll use a string function called :code:`lower()`. This function will convert all of the letters to lower case. 

::
    
    print("Enter the secret word:")
    secret_word = input()

    if secret_word.lower() == "wattlebird":
        print("Welcome to Gryffindor Tower")

