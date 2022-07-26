# How to reach me...

My email: dave@developintelligence.com
Slack channel: TBA

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
