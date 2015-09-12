
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
