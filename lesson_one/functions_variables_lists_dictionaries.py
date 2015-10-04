#By convention we keep all our imports at the top of the file, but you can put them elsewhere (please don't)
import json
import requests
import lxml.html

def remove_all(listing,x):
    while x in listing:
        listing.remove(x)
    return listing

#Variables
x = 1
print x
x += 1 # <=> x = x + 1

print "printing out a list"
listing = [1,2,3,4]
for i in listing:
    print i
print "printing from xrange"
for i in range(10):
    print i
print "printing the range function:"

print range(10)

#Here we were calling methods - these are functions attached to an object
print "after appending"
listing.append(5)
print listing
print "after removing"
listing.remove(4)
print listing
print "after popping"
listing.pop()
print listing

#Here we are using a function - not attached to a method
list_two = [1,1,4,3,4,1,5]
print "This is our original list",list_two
print "This is our list after removing all the 1s",remove_all(list_two,1)

dictionary = {}
dictionary["Eric"] = "Eric is 6', he is 29, and he likes everyone!"
print dictionary
print json.dumps(dictionary) #converted to json, what up

#the messy way
text = requests.get("https://www.google.com").text
html = lxml.html.fromstring(text)
links = html.xpath("//a/@href")
safe_links = []
for link in links:
    if link.startswith("http"):
        safe_links.append(link)

responses = []
for link in safe_links:
    responses.append(requests.get(link))
print responses

#the clean way
text = requests.get("https://www.google.com").text
html = lxml.html.fromstring(text)
links = html.xpath("//a/@href")
responses = []
for link in links:
    print link
    if link.startswith("http"):
        responses.append(requests.get(link))
print responses



