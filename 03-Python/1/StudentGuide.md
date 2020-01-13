## Unit 3.1 - Let's Begin Python

### Overview

In today's class, students will transition from VBA to the programming language Python. Today's class will check Python installation for students, then cover the basics of terminal navigation, variables, conditionals, and loops.

### Class Objectives

* Students will check Python 3 installation.
* Students will be able to navigate their desktop via the terminal.
* Students will be able to create Python scripts and run them in the terminal.
* Students will be able to understand basic programming concepts in Python.

- - -

### Activities Preview

* **Terminal**
* Instructions:

  * Students will now dive into the terminal, create three folders, and a pair of Python files which will print some strings of their own creation to the console.

  * Follow along with these instructions in your terminal and write the commands below:

    * Create a folder called `LearnPython`.

    * Navigate into the folder.

    * Inside `LearnPython` create another folder called `Assignment1`.

    * Inside `Assignment1` create a file called `quick_python.py`.

    * Add a print statement to `quick_python.py`.

    * Run `quick_python.py`.

    * Return to the `LearnPython` folder.

    * Inside `LearnPython` create another folder called `Assignment2`.

    * Inside `Assignment2` create a file called `quick_python2.py`.

    * Add a different print statement to `quick_python2.py`.

    * Run `quick_python2.py`.

* **Create A Virtual Environment**
* Instructions: 

  * `Conda Environments` [documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
  
  * Create a virtual environment that will run Python 3.6. We'll be using this environment for all the class activities.

    * First run `conda create -n PythonData python=3.6 anaconda` in the terminal. Warn students that this may take a few minutes to install.

    * Now enter `source activate PythonData` to activate the environment. When `(PythonData)$` appears, this means you are in the environment.

    * Now make sure everyone is using the correct version of Python by entering `python --version`.

      ![Python version](Images/python_version.png)

    * Lastly, show that you can exit the environment by entering `source deactivate`. If `source deactivate` does not work, try using `conda deactivate` instead.

  * Students will need to activate their environment each time that they open a new terminal.
  
  * Windows users should always use `git-bash` for their terminal.

* **Hello Variable World!**
* Instructions:

  * Create two variables called `name` and `country` that will hold strings.

  * Create two variables called `age` and `hourly_wage` that will hold integers.

  * Create a variable called `satisfied` which will hold a boolean.

  * Create a variable called `daily_wage` that will hold the value of `hourly_wage` multiplied by 8.

  * Print out statements using all of the above variables to the console.

* **Down To Input**
* Instructions:

  * Create two different variables that will take the input of your first name and your neighbor's first name.

  * Create two more inputs that will ask how many months each of you has been coding.

  * Finally, display a result with both your names and the total amount of months coding.

* **Conditional Conundrum**
* File/Instructions:

  * [conditionals_unsolved.py](Activities/08-Stu_ConditionalConundrum/Unsolved/conditionals_unsolved.py)

  * Look through the conditionals within the provided code and figure out which lines will be printed to the console.

  * Do not run the application at first, see if you can follow the thought process for each chunk of code and then place a guess. Only after coming up with a guess for each section should you run the application.

  * Bonus: After figuring out the output for all of the code chunks, create your own series of conditionals to test your fellow students. Once you have completed your puzzle, slack it out to everyone so they can test it.

* **Rock, Paper, Scissors**
* Files/Instructions:

  * Deeper dive into modules during the next class. For now here is a `random` module [documentation](https://docs.python.org/3.6/library/random.html), you'll need for this activity

  * [RPS_Unsolved.py](Activities/10-Stu_RockPaperScissors/Unsolved/RPS_Unsolved.py)

  * Using the terminal, take an input of `r`, `p` or `s` which will stand for rock, paper, and scissors.

  * Have the computer randomly pick one of these three choices.

  * Compare the user's input to the computer's choice to determine if the user won, lost, or tied.

  * Hints: Look into this [stackoverflow](https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list) question for help on using the `random` module to select a value from a list.

* **Number Chain**
* Instructions: 

  * Using a `while` loop, ask the user "How many numbers?", and then print out a chain of ascending numbers from 0 to the number input.

  * After the results have printed, ask the user if they would like to continue. If "y" is entered, keep the chain running by inputting a new number and starting a new count from 0 to the number input. If "n" is entered, exit the application.

  * Bonus: Rather than just displaying numbers starting at 0, have the numbers begin at the end of the previous chain.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
