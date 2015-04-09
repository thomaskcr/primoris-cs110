
Random Numbers
==============

We'll be using random numbers a lot in our games. If you create a game with the same situations it will get boring and predictable, we'll use random numbers to create new problems and keep games exciting. 

Importing Modules
-----------------

Python does not come with a built in random function so we'll need to get a library that provides it. Luckily, Python is distributed with a library that can generate random numbers. To make this library available inside our program we'll use an :code:`import` statement. 

::
    
    import random

Note: If you create a file named :code:`random.py` the import statement will try to import that file instead of the library so make sure you do not name files after libraries you're trying to use!

Getting a Random Number
-----------------------

We can get a random number using the :code:`random()` function. This will return a float between 0 and 1. 

::
    
    import random

    number = random.random()

    print(number)

The output from this will be a random number between 0 and 1. When I ran it I got the following result. 

::
    
    0.5915032817

We can use this to simulate a coinflip. Half the time the generated number will be greater than 0.50. 

::
    
    import random

    number = random.random()

    if number > .50:
        print("Heads")
    else:
        print("Tails")



Getting a Random Integer
------------------------

It is pretty common that we need to get a random integer. For this we have the :code:`randrange` function. 

This function takes two arguments, a lower bound and an upper bound. The range includes the lower bound number but will be less than the upper bound number. For example, if you want a number between 0 and 100 including both 0 and 100, your upper bound is 101 and lower bound is 0.

::
    
    import random

    number = random.randrange(0, 101)

    print ("I chose a number between 0 and 100, it was: " + str(number))




