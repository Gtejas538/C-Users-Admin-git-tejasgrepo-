'''
Created on 26-Jul-2025

@author: Admin
'''

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and rv


repeatput = "Yes"
while (repeatput == "Yes") or (repeatput == "yes"):
    list10 = [10,20,20,30,40,40,50,40] 
    print("The elements in the list  :", list10)
    
    nume = int(input("Choose an element from the list: "))
    counte=list10.count(nume)
    if counte==0:
        print("element is not found")
        
    else:    
       
        print(f"The given element is present {counte} times in list")
        indexe=list10.index(nume)
        print("The index of the given element is",indexe)
    
    for j in range(len(list10)):
        if nume==list10[j] and counte>0 and j!=indexe:
            print("the other indexes of the list is",j)
    userchoice=input("Please do type yes-1.If you need to delete element by index all-2.to remove all indices of the current element")
    if userchoice=="yes":
        num1=input("enter the indices to delete")
        num1=[int(j) for j in num1.split()]
        print(num1)
        num1.sort(reverse=True)
        for indexe in num1:
            if indexe<len(list10):
                list10.pop(indexe)
            else:
                print("index out of range")
        
        print("The list after the deletion is",list10)
    elif userchoice=="all":
            for i in range(0,counte):
                list10.remove(nume)
                
            print("The list after removing element  from all indices", list10)
    repeatput=input("Do you want to repeat this exercise choose Yes or No")
    
else:
    print("Process is over")
    exit
    
        