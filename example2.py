#!python3

"""
iterating through a list/tuple/string or dict

This is simply cycling through all of the possibe values one at a time and checking the value or doing something with it.  We can use the for loop 
We make use of an indexing variable that temporarily takes on the value of each member element 
Note that the "else" at the end of the for loop is optional
"""

x = (1, 2, 3, 4, 5, 6, 7)

for i in x:
    if i == 3:
        print(f"{i} this member element was 3")
    else:
        print(i)
else:
    print("End of the tuple")


'''
Note that working through a list does the exact same thing
'''
x = [1, 2, 3, 4, 5, 6, 7]

for i in x:
    if i == 3:
        print(f"{i} this member element was 3")
    else:
        print(i)
else:
    print("End of the list")

'''
You can also iterate through the characters of a string
'''
x = "This is a long sentence"
for i in x:
    if i == "e":
        print(f"{i} was found in the sentence")
    else:
        print(i)
    
    
'''
Using for to iterate through a dictionary retrieves only they keys, not the values of those keys. In order to retrieve the values, we can use the keys.
'''
x = {
    "a": 2,
    "b": 3,
    "c": 4
}

for i in x:
    print(i, x[i])
