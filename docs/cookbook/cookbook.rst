

Python 3 Cookbook
=================


Variables
---------




Conditionals
------------



Loops
-----


While Loop
~~~~~~~~~~

::
    
    >>> x = 0               # Don't forget to initialize your variable!
    >>> while (x < 5):
    ...     x += 1          # This is the same as x = x + 1
    ...     print(x)
    ... 
    1
    2
    3
    4

For Loop
~~~~~~~~

::
    
    >>> for i in xrange(1, 5):
    ...     print(i)
    ... 
    1
    2
    3
    4


Nested Loops
~~~~~~~~~~~~

::
    
    >>> for i in xrange(1, 5):
    ...     for j in xrange(1, 5):
    ...         print(i, j)
    ... 
    (1, 1)
    (1, 2)
    (1, 3)
    (1, 4)
    (2, 1)
    (2, 2)
    (2, 3)
    (2, 4)
    (3, 1)
    (3, 2)
    (3, 3)
    (3, 4)
    (4, 1)
    (4, 2)
    (4, 3)
    (4, 4)

Files
-----

Reading From a File
~~~~~~~~~~~~~~~~~~~

::
    
    with open('C:\path\to\file.txt', 'r') as f:
        lines = f.readlines()

    # Lines is now a list of all of the lines in your file

    for line in lines:
        print(line)

Writing to a File
~~~~~~~~~~~~~~~~~

::
    
    import random

    with open('C:\path\to\file.txt', 'w') as f: # Notice this is a w not an r
        # \n means newline
        f.write("Number: " + str(random.randint(1,100)) + "\n")

Strings
-------

Splitting a String
~~~~~~~~~~~~~~~~~~

We can split a string using a token with the following code. In my example, I am splitting the string by commas but you can use any symbol or even letter. 

::
    
    colors = 'blue, red, green'
    color_list = colors.split(",")

    for color in color_list:
        print color
