

Connect Four and AI
===================

You will be creating a connect four game and then programming computer AI to play against. 

For this lab, an outline of the code has been created. You will need to write two of the functions for this lab so they pass the tests and then write AI code to play against. 

We will have a tornament to see who's code plays connect four the best. 


Fork the Code
-------------

A repository with all of the outlined code for this project is located here: https://github.com/thomaskcr/cs110-connect-four

In the upper right hand corner you will see a "Fork" button. Click that button and add a copy of this repository to your own account. 

Once you have done that, clone the repository to your computer. 


Finish the Board Class
----------------------

In connect_four.py there are two functions that are incomplete. 

:code:`add_piece`: This function takes a column and a player type (red is "R" and black is "B"). Your code should add the piece to the lowest position in the column. 

:code:`get_game_result`: Your code will need to find out if there is currently a winner for the game. This includes horizontal, vertical and diagonal. 


Write your AI
-------------

In the :code:`ai.py` file, there is a function that currently just returns a random column. You have access to the entire board and are told which player you currently are. Write code that you think calulates the best possible move. 

Remember you need to play both offense and defense! 

