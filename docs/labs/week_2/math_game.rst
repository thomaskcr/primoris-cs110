
Math Game
=========

For the math game lab you are going to write a program that creates a math problem that the user must answer and tells them whether their response is correct. 

Example
-------

You can choose any math problems you would like, in my example I am going to use addition. 

Here is an example when the user gets the problem correct:

::

    What is 55 + 23 + 71?
    149
    That's right, good job!

And here is an example when the user gets the problem wrong:

::
    
    What is 87 + 29 + 83?
    12
    Sorry, that's incorrect.

Here is the algorithm for my example:

1. Generate a random number and store it in :code:`number_1`
2. Generate a random number and store it in :code:`number_2`
3. Generate a random number and store it in :code:`number_3`
4. Print out the math problem

    ::
        
        print("What is " + number_1 + " + " number_2 + " + " + number_3 + "?")

5. Get the input from the user and store it in :code:`user_input` (Don't forget to convert to an integer)
6. Calculate the answer

    ::
        
        answer = number_1 + number_2 + number_3

7. Test whether user's answer is correct and output message

    ::

        # Test user response
        if (user_input == answer):
            # User response was correct
            print("That's right, good job!")
        else:
            # User's response was wrong
            print("Sorry, that's incorrect.")


Write Your Program
------------------

Decide on your own problem and then write a program that asks a user to solve it and then tells them whether they were right or wrong. 

If you decide to combine operations make sure your order of operations is correct and communicate that to your user so they can get it right! You may need to include parenthesis. 

You'll need to use the :code:`randint()` function to generate your random numbers. 

You should stick to addition and multiplication for now so you can ensure positive integer numbers as answers. We haven't discussed decimal numbers for input yet. 

Make sure to test your program with a calculator to confirm that it is behaving correctly.

