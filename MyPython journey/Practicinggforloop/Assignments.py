'''
Created on 08-Aug-2025

@author: Admin
'''


#function to print list of integers w/o range function

def list_generate(stop):
    
    list35=[]
    i=1
    while i <=stop:
        list35.insert(0,i)
        list35.sort()
        i+=1
    print(list35)
    
stop=int(input("enter the stop value"))
list_generate(stop)    

#create a new list withut new inbuilt in
list65=[]
def tejasvalue(stop):
    for i in range(1,stop+1):
        list65.append(i)
    return list65
stop=int(input("enter the stop value"))
b=tejasvalue(stop)
print(b)

#create a new list using list inbuil function
def sirlegend(stop1):
    list45=[i for i in range(1,stop1+1)]
    return list45
stop1=int(input("enter the stop value"))
c=sirlegend(stop1)
print(c)

#code to count the no of elements in list
list2=[23,44,5,67]
count1=0
for i in list2:
    count1=count1+1
print(f"the length of list is {count1}")

#fimaboci series generation

def fibonaccii_series(numbere):
    a,b = 0,1
    series=[]
    for i in range(0,numbere):
        series.append(a)
        a,b = b,a+b

    return series


numbere=int(input("Enter the position until which the series needs to be printed: "))
j=fibonaccii_series(numbere)
print(j)

#fibonacii numbeers with recrsion

def fibonacii_recursion(numbere):
    if numbere==0 or numbere==1:
        return numbere
    if numbere >1:
        return fibonacii_recursion(numbere-1)+(numbere-2)
    
numbere=int(input("enter the position to stop"))
u=fibonaccii_series(numbere)
print(u)


#function fo rsart ,, stop and dstep value without range function

def thisseries_new(start,stop,step):
    list92=[]
    i = start
    while i<=stop:
        if step==1:
            list92.append(i)
            i+=1
            
        elif step>1:
            i+=step
            list92.append(i)
    return list92
start1=int(input("enter the start value"))
stop1=int(input("enter the stop value"))
step1=int(input("enter the step value"))
z=thisseries_new(start1,stop1,step1)
print(z)


#with range function

def listi_gen(start,end,step):
    list10=list(range(start,end+1,step))
    return list10

j=listi_gen(10,20,2)
print(j)

#infinite add function
def infinite_add(*a):
    sum=0
    print(a)
    for i in a:
        sum=sum+i
        
    return sum
        
        
        
t=infinite_add(6,7,7,9)
print(t)

#variablelenghtkryword arguenents4
def add_infinite(**a):
    print(a)
    result=0
    for t in a:
        result=result+t
    return result
            


o=add_infinite(a=1, b=2, c=3)
print(o)

#

    
        