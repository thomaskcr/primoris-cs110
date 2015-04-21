# Introduction to Python with Games

**Spring 2015 Section**

**Instructor**: Kyle Thomas - thomaskcr@gmail.com

Hosted by Primoris Academy - Westwood, NJ

![Primoris Academy Logo](https://github.com/thomaskcr/primoris-cs110/blob/development/assets/img/primoris_logo.jpg "Primoris Academy") 

This course is designed to introduce students to the fundamentals of programming using the Python language. The theme for this course will be games but the ultimate goal is to teach students how to examine a problem from the point of view of a programmer and then give them the tools to solve it. Games provide a way for someone with just about any interest to find a problem that interests them and then explore it. 
    
The course will start with learning how to set up a development environment, control flow statements in Python and using basic data structures. These principles will be applied to developing different types of games every week. We will cover as many types of games as possible including card games, arcade games, board games and RPGs. Each week will introduce new programming challenges and provide a platform for students to explore topics they are interested in. 

The course structure will consist of a weekly lecture based on the notes packet distributed with this course that will introduce the new topics for the week. Students will have a weekly lab to complete that will be started in class and due the next week. 


## Course Calendar

This is a tentative course calendar. If you have any games, on this calendar or not, that you are excited about building let me know and I'll make sure that they are prioritized or create a lab based on your request. 

### Week 1

The first week will cover everything needed to get started programming in Python on Windows. We will start with learning how to install the Python interpreter and use the Python shell. Once we can execute Python code, we will introduce the concept of version control and learn how to use GitHub. The class will end covering some basic features of the Python language and we will write our first programs. 

#### Outline

- Lecture Topics
  - [Getting Started](docs/lecture_notes/introduction/introduction.rst): Quick introduction to programming and python with information on installing the tools we'll need for this course.
  - [Saved Programs](docs/lecture_notes/saved_programs/saved_programs.rst): We'll go through saving your Python programs to files and running them. 
  - [GitHub Basics](docs/lecture_notes/github/github.rst): You will use GitHub to turn your assignments into me. 
  - [Python Language Basics](docs/lecture_notes/language_basics.rst): In this set of notes we'll cover variables, types, operators and getting user input.
  - [Conditionals](docs/lecture_notes/conditionals/conditionals.rst): In these notes we'll cover the if statement. 
  - [Random Numbers](docs/lecture_notes/random_numbers.rst): These notes cover generating and using random numbers. 
- Walkthroughs
  - [Python Installation Video](http://youtu.be/e3KC07KVRAE): A walkthrough of the process of installing Python on a Windows computer and using the interactive shell to execute expressions. Below are the four things you'll need to install for this class. 
    - [Download Python](https://www.python.org/downloads/) This is the site to get the Python installer. We are using Python 3.4 for this course, the current version is 3.4.3.
    - [Download Wing IDE 101](https://wingware.com/downloads/wingide-101) This is the IDE (where you write and run your programs) we'll be using for this class.
    - [Pygame Installer](http://programarcadegames.com/pygame-1.9.2a0.win32-py3.4.msi) We won't be using this the first couple weeks but it doesn't hurt to have it ready to go. 
    - [GitHub for Windows Download](https://windows.github.com/) You'll need this to submit your assignments.
  - Hello World: By tradition, the first program beginners execute in a new language prints the phrase "Hello, World!". In this walkthrough we will write the "Hello, World!" program after setting up a GitHub account and then add the program to our profile. 
    - [YouTube Video](http://youtu.be/Mw28iQS982s)
    - [GitHub Repo for Hello World](https://github.com/thomaskcr/python-hello-world)
  - [Dice Game](docs/walkthroughs/dice_game/dice_game.rst): We'll create a dice game. 
    - [YouTube Video](http://youtu.be/OgX6GJMW7XM) The Chrome screen seems to be capturing wrong. Luckily I don't spend much time there in the video. The page I have opened is the Dice Game link above. I ended up adding an extra feature in the video.
    - [GitHub Repo for Dice Game](https://github.com/thomaskcr/python-dice-game)
- Lab
  - [Penny Drop Calculator](docs/labs/week_1/penny_drop_calculator.rst) **[50 Points]**
  - [Math Game](docs/labs/week_1/math_game.rst) **[100 Points]** 
- Scratch Lab (Only due for Scratch Group)
  - [Scratch Dice Game](docs/labs/week_1/scratch_dice_game.rst) **[200 Points]**

#### Additional Resources

- [Wing IDE Tutorial](https://wingware.com/doc/intro/tutorial) This site can give more information about the features of Wing IDE including many that we won't have a chance to use in this class.
- [Git Community Book](http://git-scm.com/book/en/v2) If you really want to learn git in depth, this book goes through all of the details. 
- [Invent With Python: Writing Programs](http://inventwithpython.com/chapter3.html): This chapter covers flow of execution, strings, data types, saving/running programs in IDLE (we use Wing IDE), the `print()` and `input()` functions, comments and variable naming. 
- [Invent With Python: Guess the Number](http://inventwithpython.com/chapter4.html): This covers some topics from next week as well but goes into more detail about modules/imports and then covers conditionals, blocks, comparisons, type conversion and the random functions. The while statement will be covered next week and break statement will be covered later in the course. 



### Week 2

#### 2:45 Class

- Lecture Topics
  - [Getting Started](docs/lecture_notes/introduction/introduction.rst): Quick introduction to programming and python with information on installing the tools we'll need for this course.
  - [Saved Programs](docs/lecture_notes/saved_programs/saved_programs.rst): We'll go through saving your Python programs to files and running them. 
  - [Python Language Basics](docs/lecture_notes/language_basics.rst): In this set of notes we'll cover variables, types, operators and getting user input.
  - [Conditionals](docs/lecture_notes/conditionals/conditionals.rst): In these notes we'll cover the if statement. 
  - [Random Numbers](docs/lecture_notes/random_numbers.rst): These notes cover generating and using random numbers. 
- Lab
  - [Math Game (Python)](docs/labs/week_2/math_game.rst) **[100 Points]** 
  - [Guessing Game (Scratch)](docs/labs/week_2/guessing_game_scratch.rst) **[100 Points]** 

#### 4:45 Class

- Lecture Topics
  - Loops
  - Lists
  - Reading/Writing Files
- [Cookbook](docs/cookbook/cookbook.rst) Updates:
  - Loops
  - Writing to Files
  - Reading Files
- Lab
  - [Hello World: Introduction to GitHub](docs/labs/week_1/hello_world.rst) **[50 Points]** 
  - [Quiz Game](docs/labs/week_2/quiz_game_lab.rst) **[100 Points]** 
  - Guessing Game



#### Additional Resources

- [Python 3 Cheat Sheet](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf) 

### Week 3

#### Outline

- Lecture Topics
  - Pygame Basics
- Walkthroughs
  - Drawing Shapes: We'll draw some shapes in Pygame. 
  - Moving Shapes: We'll move our shapes around the screen.
  - Finding the Mouse: Determine where a mouse click happened. 
- Lab
  - Hangman


#### Additional Resources


### Week 4

#### Outline

- Lecture Topics
  - Sprites
- Walkthroughs
  - Controlling an Object with the Keyboard
  - Collision Detection
- Lab
  - Racing Game



#### Additional Resources

### Week 5

#### Outline

- Lecture Topics
  - Writing Functions
  - Dictionaries
  - Card Games
- Walkthroughs
  - Creating a Shuffle Deck Function
  - Taking Cards from a Deck
- Lab
  - Blackjack


#### Additional Resources

### Week 6

#### Outline

- Lecture Topics
  - Physics: Reflections
- Walkthroughs
  - Reflections: Bouncing lasers off a mirror. 
  - Local Leaderboard: We'll create and display a high score list.
- Lab
  - Pong

#### Additional Resources

### Week 7

#### Outline

- Lecture Topics
  - Physics: Gravity
- Walkthroughs
  - Jumping: Make a character jump in the air. We'll explore the parameters associated with gravity that determine how high your character can jump. 
  - Jumping Forward: We'll use momentum to allow our character to jump forward.
- Lab
  - Platformer

#### Additional Resources


### Week 8

#### Outline

- Review
- Lab
  - Space Invaders
  

#### Additional Resources



## General Resources

- [Download Python](https://www.python.org/downloads/) This is the site to get the Python installer. We are using Python 3.4 for this course, the current version is 3.4.3.
- [Python For Beginners](https://www.python.org/about/gettingstarted/): This is a getting started guide from the official python website. 
  - [Python for Non-Programmers](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers) One of the links on this page is a getting started page specifically put together for non-programmers. This is a collection of resources that can be used by a beginner to learn how to program. As you can see, there is no shortage of free resources online for learning how to program.
- [Official Python Documentation](https://docs.python.org/3.4/index.html) This is the Python language documentation. The most relevant links on this page are the Tutorial, Library Reference and Language Reference
  - [Python Tutorial](https://docs.python.org/3.4/tutorial/index.html) This is a tutorial introduces a subset of Python's features to get a developer started using the language. It may go more or less in depth than this course depending on the topic. This course lines up approximately with chapters 1-7. 
  - [Language Reference](https://docs.python.org/3.4/reference/index.html) Similar to the tutorial but much more complete and organized by topic instead of as an introduction to the language. 
  - [Library Reference](https://docs.python.org/3.4/library/index.html) Find information about the modules/functions distributed with your python installation. This will probably be less useful for this class but is a good place to see what comes with the Python language. 
- [Installing Python on Windows](http://docs.python-guide.org/en/latest/starting/install/win/) Instructions to help walk through the installation of Python on Windows. 
- [Installing Python on Mac OS X](http://docs.python-guide.org/en/latest/starting/install/osx/) For this course, we will assume students are working on Windows since it is the most common operating system but python can be run on just about any OS. These directions walk through the nuance of installing on a Mac. 
- [Installing Python on Linux](http://docs.python-guide.org/en/latest/starting/install/linux/) Linux is a free and open-source operating system used often on servers and by developers. There are a lot of flavors of Linux, my personal favorite is Fedora for my development machines and CentOS (an enterprise-class relative of Fedora) for servers. If interested in Linux here are some resources to get started: 
  - [Fedora Official Site](https://getfedora.org/) Fedora official site. Includes links to downloads and documentation with information on getting started and installation. Fedora offers LiveCDs that allow users to run Fedora without installing it to try it out. 
  - [Ubuntu Official Site](http://www.ubuntu.com/) Ubuntu is a popular Linux flavor for beginners.
  - [Ubuntu Community Installation Guide](https://help.ubuntu.com/community/Installation) Gives information on installing and getting started with Ubuntu.
