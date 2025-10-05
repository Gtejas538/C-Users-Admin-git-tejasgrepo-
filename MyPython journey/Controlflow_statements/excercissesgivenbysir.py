'''
Created on 25-Jul-2025

@author: Admin
'''

# List operations
"""list1=[10,0,30,40]
list2=[20,1,60,80]
print(list1+list2)
#in this it will be concatenated
print(list1-list2)=[34,8,98]
print(list1/list2)
print(list1%list2)
print(list1//list2)

#tuple and set comprehension
list3=[9,0,8,6,7]
list4 = [i*2 for i in list3]
print(list4)

tuple10=(10,11,12,13,14)
tuple11=(j*2 for j in tuple10)
print(tuple11)
#it doesnt generate a tuple 

set10={10,20,30,40}
set11 = {i*2 for i in set10}
print(set11) #it will generate set but in other order


list5=[10,20,30,50]
i=1
while i<5:
    print(list5)
    
#using whileloop accessing the element
list101 = [8,9,10,11,12]
numcount=0
while numcount<len(list101):
    print(list101[numcount])
    numcount=+1
    
#list removeopeations
list3 = [10,20,30,40,50,20]

list3.remove(20)
 #it will remove first occurence of that elent 
print(list3)



#tuple checking
tuple45=()
print(tuple45)

tuple45=(90,68,87,65)
print(type(tuple45))

mytuple=tuple()
print(mytuple)

tuplevivek = tuple(range(10))
print(tuplevivek)

tupletejas = tuple((9,0,8,9,9,5))
print(tupletejas)

tupletejas = (9,9,9)
print(tupletejas)

mysurutuple =(9,9.0,None,True,8+7j)
print(mysurutuple)

jai=(7,8,76,8,87,78)
print(jai)

adrusta=(8,9,7,8,9,7)
print(adrusta[0])

busuu=tuple(range(10))
print(busuu[-1])

pointuu = (9,8,7,6,6)"we cannot delete or modify data in tuple using index"
#pointuu[2]=9
#pointu[-1]=0
print(pointuu)
for i in tuple(range(10)):
    print(i)
    
#set checking
dset={}
print(dset)
print(type(dset))
dset1={8,9,6,5,0}
print(dset1)
print(type(dset1))

myset = set()
print(myset)
deste = set(range(10))
print(deste)
#deste = set(8,9,10,6)
#print(deste)

dset1={9,9,9,9}
print(dset1)"set can contain same kind of elemts but it wil print one value"

dft1={9,0,7,6,79.0,"gyt"}  "set can cntain diifent kind of elemnts but it will be printed in order"
print(dft1)

dft1={9,0,7,6,79.0,9,6,8,8}
print(dft1)"set can contain dupicate elments but it will printed once"

my_set = {"apple","banana","cherry"}
for item in my_set:
    print(item) "elent in ser can be accsedd using for loop"
    
    
dft1 = {9,0,7,6,79.0,9,6,8,8}
dft1[4]=8
print(dft1)"elemnts in set can be mofified by indexing but by built in fm"

for in list(range(10)):
    print(i)
    
#list built inn - 
list5=[9,8,7,6,5,4]
print('',list5[2:])

list8=[10,90]
list4=[98,100]
list8.extend(list4)

#slicing operator can be used for negative vaues

list50=[90,10,110,120]

print(list50[0:])
print(list50[2:])
print(list50[0])

print(list50[-1:0])
print(list50[-6:-10])
print(list[-6:1])
print(list50[0:-100])

#tuples
tuple10=(43,44,45,46)
print(tuple10[0:])
print(tuple10[2:])
print(tuple10[1:3])
print(tuple10[:2])
print(tuple10[-2:0])
print(tuple10[-10:-2])
print(tuple10[0:-3])
print(tuple10[3:-3])
print(tuple10[-2:2])

viveksir big assigmnent
 
#for true: 
    
 list99 =[10,20,30,40,20,30]
 print(list99)
 occurence=0
 n=int(input("choose an elementfrom the list to check"))
 
 for i in list99:
    if i==n:
        occurence=+1
    else:
        continue
 print("the occurence of elent is.",occurence)
 
thambicount=0

while thambicount<len(list99):
    if list99[thambicount]==n:
        print("index of that element is",thambicount)
    else:
        continue

m=int(" press 1  to delete the index of the elent",thambicount)

if m==1:
    list99.remove(thambicount)
    print("element delated")
else:
    print("ement not deleted ")
    
#z=str(input("enter yes if we need to repea the process"))
#if z=="yes":
#continue    
"""        
list12=[90,100,110,120,130]
countf=0
for i in list12:
    countf=countf+1
print(countf) 
         
 
    

    

