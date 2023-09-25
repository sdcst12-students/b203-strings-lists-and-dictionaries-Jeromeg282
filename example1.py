#!python

'''
Using the "in" operator to search tuples, lists, strings and dicts
This can tell you if a particular value can be found in a list, tuple or string, but it can only find keys in dictionaries
'''

a = (3,4,5,6,7)
b = [3,4,5,6,7]
c = {
    "a" : 3,
    "b" : 4,
    "c" : 5,
    "d" : 6,
    "e" : 7
}
d = "34567"

if 3 in a:
    print("found in tuple")
if 3 in b:
    print("found in list")
if 3 in c:
    print("value found in dict")
if "c" in c:
    print("key found in dict")
if "3" in d:
    print("character found in string")

