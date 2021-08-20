Week 2 Python

Learning objectives:
	* Program in Python
	* Solve exercise 2-1, 2-2 and 2-3

P.S. 	
	Only native python functionality is allowed

1. Install python2 using appropiate method regarding to the OS
	i.e. in ubuntu 
	apt update && apt install python2
	
2. Compile syntax
	python2 FILE.py

3. Permission of the file that created on windows and copied onto linux.
	The permission depends on the WINDOWS side. i.e linux normal user would not be able to read, but super user can.

4. python code execution time
	mark a time point 
	import time
	M1=time.time()
	#SOME CODE HERE
	print "%s seconds" % time.time()-M1 

* How to use the files?
	python ex2-1.py
* What are these files?
ex2-1.py contains the exercise content and solution. By compiling the source file, a new stdo file will be created. The remaining file is just an example of using a python package and its built in function.


* Exercise 2.1:
Write a script with two methods. The first method should read in a matrix like the one here and return a list of lists. The second method should do the inverse, namely take, as input, a list of lists and save it in a file with same format as the initial file. The first method should take the file name as a parameter. The second method should take two arguments, the list of lists, and a filename of where to save the output.
