'''
Created on 13-Jul-2025

@author: Admin
'''
#two types of looping sttaement sin python 1.while loop 2.for loop
#whileloop normal, for loop -speciality it iterates  over collection
#for loop can be used in collection or range
#range function avalable in pythn - it will generate sequence of int in part rage
# while loop
# 3 parts 1. we need  1.initialize a variable 2.defing condition in hile keyword
# 3.based on our requirement incr or decrement

"""range()- one value which we give to range it will consider as stop value 
we can access range by for value , after taking stop value it will consider from Zero print it ,
we can access range value uding for loop in range of 1 to 100 print the value
in range of 1 to 100 print even number"""
print(range)
for i in range(10):
    print(i)
for i in range(1,100):
    if i % 2 == 0:
        print(i)
    
"""count = 1
while count<=10:
    print(f"the number is {count}")
    print("number from 1 to 10 ", count)
    #count=count+1
    count+=1
    
"""