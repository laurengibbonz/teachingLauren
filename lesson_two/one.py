import pickle

name = str(raw_input("Hello there, what's your name?")) 
occupation = str(raw_input("Where do you work?"))
print name,occupation
dict = {}
dict["name"] = name
dict["occupation"] = occupation
pickle.dump(dict,open("user.pickle","w"))