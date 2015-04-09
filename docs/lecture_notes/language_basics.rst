
Python Language Basics
======================

We now know how to execute our programs but before we can start creating games we'll need to learn the basics of Python. The concepts are the same in most programming langauges, you'll see that a lot of the things you learned in Scratch are very similar in Python. If you didn't learn scratch don't worry, these notes will cover all of the concepts you need to know for this course. 

Comments
--------

Before we learn more about writing code, a very important part of programming is reading code. Python provides a tool to help you leave notes for yourself and others in your code. This tool is called a **comment**. In Python comments are created by starting a line with a :code:`#`. This symbol tells the Python interpreter to ignore this line of code. 

::

    # This program prints "Hello, World!" 
    print("Hello, World!")

You can use comments to prevent a line of code from executing. This is a commonly used technique in **debugging**, which is the process of finding and fixing errors in your program. 

::

    # This program doesn't do anything
    # print("Hello, World!")

In this example, the :code:`print` statement comes after a :code:`#` which tells the interpeter to ignore that line. 

Variables
---------

A **variable** in programming is used to store information. You can access this information by using the variable name and you can also change the information in a variable. 

The way we create a variable is using the equals sign. We **assign** a value to a variable. 

::

    # Hello World with a variable
    phrase = "Hello, World!"
    print(phrase)

In this example, we create a variable called :code:`phrase`. We then instruct the interpreter to print the information held in the location called :code:`phrase`. Since we told the program that we wanted to store "Hello, World!" at that location, the program will print "Hello, World!". 

We can reuse variables also. 

::

    # Reassigning a variable
    phrase = "Hello, World!"
    phrase = "Goodbye!"
    print(phrase)

When we run this program, the output will be "Goodbye!" instead of "Hello, World!". This is because when we access the :code:`phrase` variable during the print statement, we are accessing it's current value. The statements are executed in order, so first phrase is set to "Hello, World!" but then it is set to "Goodbye!". 

Think of a variable as a name for a location that allows you to access and change what is held in that location. A variable can only hold one "thing" though. These things are called **objects**. Each object has a **type**. 

Types
~~~~~

The object a variable holds can be described by its type. The type defines how this object will interact with other objects. There are many different types, and you can even create your own types, but for the purposes of this class we'll only need to learn a few. 

**String**: A string is just text. The text can contain numbers, but when we hold numbers as a string we are telling the Python interpreter we want them treated as numbers. 

**Integer**: Just like in math, in programming integers are whole numbers. -1, 0, 5 and 330 are all integers. 

**Float**: The word float is short for floating point number. These are any numbers that have a decimal point in them. Examples include 1.55, 2.0, and -5.994483

**Boolean**: A boolean object can only have two possible values, true or false. 

Naming Variables
~~~~~~~~~~~~~~~~

It is very important to give variables good names. This will help you know what that variable is for later when looking at your code and reduce the number of comments you need to write. Imagine if you labeled every notebook for school with a random letter. You would need to remember what every letter means. After spring break it might be hard to remember what the letters mean. Instead labeling them with the name of your class makes it easy to know exactly what each notebook contains. This same lesson should apply to variable naming. 

In addition to good habits, there are rules for naming variables. 

- A variable cannot start with a number
- A variable cannot contain a space
- A variable **can** contain an underscore (_) but most other symbols are off limits

Variables are also case sensitive. The variable :code:`Phrase` is different from the variable :code:`phrase`. 

Operations
----------

We've actually already seen **operators** in action when we executed math problems in the Python interactive shell. An operator is part of an expression, the ones we'll deal with for now are 

- :code:`+` Addition
- :code:`-` Subtraction
- :code:`*` Multiplication 
- :code:`/` Division

Additionally, parenthesis (:code:`()`) are used for grouping operations just like they are in math. 

Numbers
~~~~~~~

We'll start by looking at some operations we can perform on numbers. 

::

    result = 2 + 2
    print(result)

    result = 2 + 3 * 3
    print(result)

    result = (2 + 3) * 3
    print(result)

The output from this program will be 

::
    
    4
    11
    15

As you can see the Python interpreter follows the order of operations. 

Strings
~~~~~~~

Operations can also be performed on strings. For now we will only look at the **concatenation** operation, which is a fancy way of saying combining two strings. In Python, we use the :code:`+` sign to indicate we will be combining two strings. 

::
    
    string_1 = "Hello, "
    string_2 = "World!"

    combined = string_1 + string_2
    
    print(combined)

Here we combine variables :code:`string_1` and :code:`string_2` and put the result into the location :code:`combined`. This program will output 

::

    Hello, World!


Type Conversion
~~~~~~~~~~~~~~~

Sometimes we want to combine two different types, we can do this using type conversion. We'll look at two type conversions. Converting something to a string and converting to an integer. 

To convert something to a string we use the :code:`str` **function**. We'll learn more about functions later, but we've actually already encounted one. :code:`print` is a function that takes an **argument** and prints it to the output. Here, :code:`str` takes an argument and returns a string. 

An example of when we will use this is combining an integer with a string. 

::

    val = 4
    print("The value is: " + str(val))

Here we need to convert the variable :code:`val` to a string so we can combine it with another string. 

We can also convert strings into integers. A common place this is needed is when we take user input. Input almost always comes in string form so if we are expecting a number we will need to tell Python that what we were given was a number. 

::
    
    val = "4"
    number = int(val)

Here we end up with number being the integer 4 instead of a string. 

User Input
----------

We just mentioned user input as a good time to use type conversion functions. The :code:`input()` function allows us to get user input and assign it to a variable. The function will wait for a user to enter text and press enter. 

::

    print("What is your name?")
    name = input()
    print("Hello, " + name)

When I execute this program the following will happen ("Kyle" was typed by me)

::
    
    What is your name?
    Kyle
    Hello, Kyle

Sometimes we want users to type in numbers so we can do something with them. In this example, we'll add two numbers for the user. 

::
    
    # Get numbers from user
    print("Hello, I am very good at adding numbers.")
    print("Type your first number")
    first_number = input()
    print("Type your second number")
    second_number = input()

    # Convert our numbers to integers
    first_number = int(first_number)
    second_number = int(second_number)
    
    # Add the numbrs and print the result
    # Don't forget to convert result to a string!
    result = first_number + second_number
    print("The result is: " + str(result))

This example also shows how comments can tell you what is happening in your program. The output from this program looks like this

::
    
    "Hello, I am very good at adding numbers."
    "Type your first number"
    4
    "Type your second number"
    6
    The result is: 10

