#Lesson two

Hi Lauren!  Here's what we will work on in this lesson :)

Break down:
* Review
	* Variables, lists, dictionaries in Python
	* Making requests in Python
		* Downloading webpages
		* Getting specific information
* New Stuff
	* Introduction to Flask
		* Writing routes
		* Templating in Jinja2
	* Basic Data Viz
		* C3.js
		* Leaflet.js
	* Integrating Javascript and Flask
		* sending data from server to the front end via JSON
		* sending data to the server via forms, api's, or files

##Review

Variables:

Variables are used to store data.

1)
Create a python program called one.py

In this program you should accept user input via raw_input().  If you need more information about this method, run python from the terminal and type: help(raw_input).  

Here are a few examples of raw_input:

name = str(raw_input("Hello there, what's your name?")) 
age = str(raw_input("How old are you?"))

Use raw_input to get the users name and occupation.

Variables can live beyond the run of a program.  There are a few ways to do this:

* File I/O
* Persistent Messages, via pickle
* Database connections

2)
Add onto one.py -> store the users name and occupation in a dictionary and send that dictionary to a pickle object.  Call that object user.pickle

Then create a new program called two.py

This program should print out a greeting to the user, ask them how they are liking their new occupation and then recording their result.  This should be stored to another object called job_satisfaction.pickle



