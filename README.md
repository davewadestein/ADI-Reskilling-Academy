# How to follow along...

## In the cloud...
* __Binder__ link: https://mybinder.org/v2/gh/davewadestein/ADI-Learn-to-Code/HEAD
* __Google Colaboratory__ link: https://colab.research.google.com/github/davewadestein/ADI-Learn-to-Code/blob/main/Python%20Fundamentals%20Day%201.ipynb
* 
# or locally on your machine...
* install Visual Studio Code (https://code.visualstudio.com/)
* install Anaconda (600+ MB) (https://www.anaconda.com/)
* install Python (www.python.org) + install Jupyter
   * on Windows, probably __`pip install jupyterlab`__ from a DOS/command window
* some troubleshooting notes re: installing on Windows courtesy of Trevor:
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

My email: dave@developintelligence.com

# Some Terminology
* "Pythonic"
  * a coding style that leverages Python's unique features to write code that is readable and beautiful.
  * writing code in a way that experienced Python programmers would write it
  * idiomatic
* BDFL = Benevolent Dictator for Life (formerly Guido van Rossum)
  * Guido stepped down as BDFL in 2019 due to social media harrassment after a contentious PEP was approved

# Important points about teaching/learning
* if you can't explain it in lay terms, you don't truly understand it
* you must zoom in/out as needed
  * don't zoom in until it matters
  * do/don't go down the rabbit hole

# Some formatting rules for Python
* variables only use lower case and underscores, e.g., year, cost, cost_per_ounce
* things you want to identify as constants would be all upper case, e.g., ROUTING_NUMBER

# Best practices for programming
 * "Programs must be written for people to read, and only incidentally for machines to execute." –Hal Abelson
 * Eagleson's Law: "Any code you wrote more than 6 months ago might as well have been written by someone else"
 * Prefer clear code over comments
 * Variable names–they should be descriptive
 * Follow formatting rules for your language
   * get a plug-in to make it a non-issue
 * DRY = Don't Repeat Yourself
 * According to DWS: You need "mechanical sympathy" to excel at programming or a programming language
   * Jackie Stewart
 * "Performance doesn't matter until it matters, and it rarely matters." –DWS

# Important things about Python
* everything in Python is an object
  * every object lives in memory and we can inspect it
* "truthiness"
  * any nonzero number is True (0, 0.0 are False)
  * a nonempty container is True (empty container is False)
* Python is "Duck Typed"
* built-in functions cannot change ("mutate") objects (e.g., _sorted()_)
  * corollary 1: in order to change an object you need a method (e.g., _.append()_ ... "mutator")
  * corollary 2: not all methods change their objects (e.g., _.count()_ ... "inspector")

# Python Types
* Immutable vs. Mutable Types
  * mutable: list
  * immutable: strings
* simple types (scalars) vs. containers
  * simple types: int, float, bool
  * containers: str, list, dict
* iterables are things we can iterate through
  * e.g., containers
  * and files

# Walrus Operator
  * add this
  * 
# What tools/skills do I need to be a good programmer?
* good problems-solving skills
  * ability to break things into smaller pieces
  * methodical / attention to detail
* perseverance
* not math sense, per se


