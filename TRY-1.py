print("hello world")

# in a zoo
zoolist = ["dog", "cat", "bird", "horse", "tiger", "snake", "monkey", "sheep", "mouse", "rabbit", "deer"]

# the first way to print list
print(zoolist)

# the second 
for animals in zoolist:
    print("There is a " + animals, end =". ")

# the third 
print()
print("There are", len(zoolist), "kinds of animals.")
for i in range(len(zoolist)):
    print("This is " + zoolist[i])

