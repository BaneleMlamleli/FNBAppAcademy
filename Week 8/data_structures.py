
# lists
def lists():
    letters = ['a','b','c','d']
    print(letters)
    letters.append('e')
    print(letters)
    letters.insert(2, 'z')
    print(letters)
    letters.remove('z')
    print(letters)
    letters.sort(reverse=True)
    print(letters)
    
# tuples
def tuples():
    myTuple = (1, 2, 6, 3, 4, 5, 0, 2)
    print(myTuple)
    print(myTuple[2])
    print(myTuple[-2])

# sets
def sets():
    mySet = {1, 2, 3, 4}
    print(mySet)
    mySet.add(5)
    print(mySet)
    mySet.remove(3)
    print(mySet)
    
    mySecondSet = {11,12, 2, 13, 14}
    unionSet = mySet.union(mySecondSet)
    print(unionSet)
    
    intersectionSet = mySet.intersection(mySecondSet)
    print(intersectionSet)

# dictionary
def dictionary():
    myDiction = {'a':1, 'b':2, 'c':3, 'd':4}
    print(myDiction)
    myDiction['e'] = 5
    print(myDiction)
    myDiction['c'] = 6
    print(myDiction)
    # print(myDiction)

# lists()
# tuples()
# sets()
dictionary()
