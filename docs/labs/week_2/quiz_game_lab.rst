
Quiz Game
=========

In this lab you are going to create a game that asks a user 5 random questions from a list of questions. You will read your questions from a file and then select 5 random questions from the list. 

1. You will need to create a file format to store your question and answer pairs in. For example, you could separate them using pipes:

::
    
    How many symphonies did Ludwig van Beethoven compose?|9
    How many prime numbers are there between 50 and 100?|10
    Which U.S. city has these three nicknames: air crossroads of the world, Chicago of the north, largest city in the largest state?|ANCHORAGE

2. You will read your file as a list of lines. To get the length of your list use the :code:`len(questions)` command. Generate 5 random numbers between 0 and length of list. Make sure they're all different!

3. Separate your question from your answer and print your question. Prompt for the users input. If it's a string you may want to remove spaces and punctuation from the answer and convert it to all upper case before comparing to your answer.

4. At the end of the 5 questions, print the user's score.

Don't forget your README file and to put your program on GitHub named :code:`cs110-math-quiz` so it can be graded. 

Rubric
------

- **[5 Points]** Student has a GitHub repository under their username named :code:`cs110-quiz-game` that contains the quiz game Python file. 
- **[10 Points]** Correctly uses randint() function to generate different random numbers.
- **[10 Points]** Correctly prints the question
- **[30 Points]** Allows user to input their response and converts it properly
- **[30 Points]** Script correctly determines whether user's answer was correct and outputs appropriate message at end of game.
- **[10 Points]** Student has a properly formated `README.md` file in their repository
- **[5 Points]** Commit messages


