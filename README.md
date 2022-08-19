# Week 4 survey link
https://www.surveymonkey.com/r/ADI_Week4_DWS

# How to reach me (or others)

My email: dave@developintelligence.com

Slack channel: sw-reskill-class2 (search for this channel in the global options)

Slack URL: https://analog.enterprise.slack.com/

Sabrina Devitt (sabrina@developintelligence.com)

# How to follow along...

## In the cloud...
* __Binder__ link: https://mybinder.org/v2/gh/davewadestein/ADI-Reskilling-Academy/HEAD
* __Google Colaboratory__ link: https://colab.research.google.com/github/davewadestein/ADI-Reskilling-Academy/

# or locally on your machine...
* do this:
  * install Visual Studio Code (https://code.visualstudio.com/)
* or this:
  * install Anaconda (600+ MB) (https://www.anaconda.com/)
    * download and install (right-click and elevate permissions)
    * choose the defaults
    * Jupyter will be in your Start Menu
    * Anaconda Navigator is in the Start Menu but you need to "pin it" if you want it over and over...
    * JupyterLab is the equivalent of Binder up the in cloud
  * troubleshooting Anaconda
    * if JupyterLab will not open, note this from Kevin Goodspeed:
       > To Launch JupyterLab from Anaconda requires Running as Administrator or Run Elevated.  I got the same error, and solved it by going to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit), right-clicking on 'Anaconda Navigator (Anaconda3)' and selecting Run as Administrator.
       * Matt added this clarification–if you are running "elevated" you simply need to enter your password, but if you are running as
       administrator, you have to enter your username, which is different from your email address.
* or if you are a glutton for punishment, do this:
  * install Python (www.python.org) + install Jupyter
  * on Windows, probably __`pip install jupyterlab`__ from a DOS/command window

* stop here for now

* once Python is installed you need to install __`pytest`__
   * at a command prompt, do these things:
      * type __`pip install pytest`__
      * (you may see a warning at the end if the install suggesting you add a folder to your PATH)
      * you should add that folder to the path by hitting the Windows key and typing __`env`__ into your Windows search bar
      * once you've added to the path, reboot your computer
      * then go to command window and type __`where pytest`__ and it should respond with a folder rather than a error
      * at that point you should be able to create a new folder into which you'll end up putting Python code, and once inside that folder, even if it's empty, you shoud be able to run __`pytest`__
      * if any problems, ask...
   
## Useful Python resources
* https://www.pythoncheatsheet.org/
* https://pythontutor.com/
* Python cheat sheet [http://sixthresearcher.com/wp-content/uploads/2016/12/Python3_reference_cheat_sheet.pdf]

## Local git setup
* Install git from https://git-scm.com/download/win ("git bash")
* You may want to install Notepad++ if you don't have it (https://notepad-plus-plus.org/downloads/)
* https://docs.github.com/en/get-started/getting-started-with-git/associating-text-editors-with-git

## Git on Pluralsight
 * Paolo Perrotta

## Installing Jupyter and Python locally
* some troubleshooting notes re: installing on Windows courtesy of former students:
 1. First ensure that your windows machine has a copy of Python. I got mine right from the Microsoft Store.
 2. From here you need only to run the following code within the command line (windows+R cmd) to install

					pip install jupyterlab
					
 3. According to Jupyter Lab, to run the program after the installation you run the following code from command line (this did not work for me...)
	
					jupyter-lab
					
						or
						
					python -m notebook
					
 4. If step 2 did not work for you, verify that the python.exe file is a user variable. Run the following code in command line and copy the PATH that is output
					
					where.exe python
				
 5. Press the windows key and enter "environment variables". From the "Advanced" tab within the "System Properties" window, click "Environment Variables"

 6. From the new "Environment Variables" window, click the New user variable button and enter the following. Be sure to click "OK" when closing windows after entering info

					Variable Name: python

Project Manager: sabrina@developintelligence.com
- reach out to her for any concerns/issues/recordings



# What tools/skills do I need to be a good programmer?
* good problems-solving skills
  * ability to break things into smaller pieces
  * methodical / attention to detail
* perseverance
* not math sense, per se
* common errors to be aware of: off-by-one
  * the three banes of existence for programmers are: uninitialized variables and off-by-one errors

# Books you may want to consider
  * Introducing Python by Bill Lubanovic (beginner)
  * Fluent Python by Luciano Ramalho (intermediate)
  
# TDD Testing Tools ...
  * If you want to write tests in Python to test C Code: 
https://av.tib.eu/media/21089#:~:text=Alexander%20Steffen%20%2D%20Writing%20unit%20tests,in%20C%20(or%20C%2B%2B).&text=It%20will%20also%20cover%20creating,test%20to%20hide%20external%20dependencies.
  * If you want to control your instruments with Python: https://pyvisa.readthedocs.io/en/latest/ (https://pypi.org/project/PyVISA/)
  
# Linux–how to run it on your machine or in the cloud
* https://docs.microsoft.com/en-us/windows/wsl/about
* http://repl.it
* Git bash (https://git-scm.com/downloads)
  * not Linux, but rather, a Bash clone that lets you run some Linux-like commands


# "Group" programming assignment
1. add a "store game" feature to Chutes and Ladders
* when you quit, you have the option to save the game
  * save whose turn it is and the player names and positions
  * player whose turn it is is first line
  * subsequent lines are player and position, e.g.,
  > Grace<br>
  > Dave 55<br>
  > Carlos 41<br>
  > Grace 65
  * you might consider a special extension (other than .txt), e.g., .chute
* when you start the game, you may choose to enter a filename with content such as the above
  * if contents are valid, restore the game and continue
  * if not valid, tell user!
    * Simon's suggestion: some code or word or phrase like "chutes_and_ladder_stored_games" at the top
  
* e.g., Cows and Bulls
  * what to store?
    * secret code
    * guesses so far / responses (or recreate them)
    * Balbir suggestion: store the guesses and the responses together in a dict
  * what to change in this program?
    * how many digits in the code? (if we didn't ask that, add it) / maybe have the restore function here
    * when you quit, perhas 'q' for 'quit' and 's' for 'save'
  * how to do this?
    * functions!
    * test them 
1. Make some new functions for some of the main program code
1. let a player quit independent of the game
1. let a new player take over for an existing player
1. etc.

# 2nd "Group" Project Options
* The Monty Hall Problem
	* https://en.wikipedia.org/wiki/Monty_Hall_problem
	* The goal is to simulate it. In other words, pick a random door behind which the “car” is hidden, then pick a random door that represents the choice made by the contestant, then have the contestant switch to the other door. Ask how many times to run this simulation and you should see it converging on a 66.67% probability that the contestant wins the car by switching. These are the only two possible scenarios:
	  1. contestant picks car on first try, Monty Hall reveals a goat behind one of the remaining doors, contestant switches to final remaining door, and loses
	  1. contestant does not pick car on first try, Monty Hall reveals a goat behind one of the remaining doors, contestant switches to final remaining door, and wins
	* Your simulation should show that #1 happens 1/3 of the time (because with 3 doors, there is a 1/3 chance of picking the car on the first choice), and that #2 happens 2/3 of the time.
	* Let the user enter the number of doors, so as the number of doors increases, the benefit from switching increases. As an example, consider how it would work with 100 doors. Contest picks a door, Monty Hall shows the contestant that nothing of value is behind 98 of the other doors, and then asks if contestant wants to stick with original choice or switch to the one remaining door. In this example, the contestant clearly had a 1/100 chance of getting car on first try, but if contestant switches, there is a 99/100 chance the car will be behind the remaining door. So your simulation should show that with 100 doors, the benefit from switching occurs 99% of the time.
* Roshambo / Rock-Scissors-Paper
  * play against the computer
  * you pick one of Rock / Scissors / Paper
  * computer picks one
  * compare
     * paper cover rocks (paper wins)
     * rock smashes scissors (rock wins)
     * scissors cuts paper (scissors wins)

# Blackjack
* computer deals 2 cards to each player
* the rank of the cards is all that matter, suits are ignored
* J, Q, K count as 10
* A counts as 1 or 11 (don't worry about this at first)
* the value of a hand is the total of all the cards, e.g., 4 and K total 14, A and 5 total 16 (or 6)
* player can "hit" (ask for another card) or "stand"
* dealer must hit on a hand below 17 and stand on 17+
* player with higher hand wins
* 21 is a "blackjack"
* hands over 21 are a "bust" and the other player wins
* you can get Unicode suit symbols like this:
  `suits = '\u2663 \u2662 \u2661 \u2660'.split()`
