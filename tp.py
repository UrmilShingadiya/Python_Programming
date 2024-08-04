#1 Write a Python program to create a tuple
newtuple =  ("abc", "pqr", "xyz")
print(newtuple)

#2. Write a Python program to create a tuple with different data types.
my_tuple = (1, 1.12, "abc",[1, 2, 3], {"key": "value"})

print("Integer:", my_tuple[0])
print("Float:", my_tuple[1])
print("String:", my_tuple[2])
print("Boolean:", my_tuple[3])
print("List:", my_tuple[4])

#3. Write a Python program to create a tuple with numbers and print one  item.
x = (1, 2, 3, 4, 5)
print(x)
x = 5
print(x)

#4 Write a Python program to unpack a tuple in several variables.
info = ("ABC", 25, "Engineer")

name, age, occupation = info
print("Name:", name)
print("Age:", age)
print("Occupation:", occupation)

#5. Write a Python program to add an item in a tuple
new_tuple = (1,2,3,4,5)
print(new_tuple)
x = new_tuple + (6,)
print(x)

#6. Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'a','m','p','l','e')
x = ''.join(tup)
print(x)

#7. Write a Python program to get the 4th element and 4th element
 
t = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(t)

i = t[3]
print("4th Elements From Tuple :",i)
j = t[-4]
print("4th Elements From Last Tuple :",j)

#8. Write a Python program to create the colon of a tuple.
from copy import deepcopy

t = ("XYZ", 'J', 23 , 11.11 , [23,12] , True) 
print(t)
x = deepcopy(t)
x[4].append(50)
print(x)

#9. Write a Python program to find the repeated items of a tuple.

x = (1,2,5,7,3,6,9,2)
print(x)
count = x.count(2)
print(count) 

#10. Write a Python program to check whether an element exists within a tuple.

a = ("w", 3, "x", "a", "v", "f", "b", "r", "j", "k")

print("r" in a)
print(5 in a)

#11. Write a Python program to convert a list to a tuple.

a_list = [5, 10, 7, 4, 15, 3]
print(a_list)

x = tuple(a_list)
print(x)

#12. Write a Python program to remove an item from a tuple.
x = (1,2,5,7,3,6,9,2)
a = list(x)
a.remove(3)
print(a)

#13. Write a Python program to slice a tuple.
a = (10,20,30,40,50,60,70,80,90,100)
print(a[2:7])
print(a[0:3])

#14. Write a Python program to find the index of an item of a tuple.
a = (10,20,30,40,50,60,70,80,90,100)
print("Index Number :",a.index(70))
print("Index Number :",a.index(30))

#15. Write a Python program to find the length of a tuple

x = (1,2,3,4,5)

print(x)
print(len(x)) 

