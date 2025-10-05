'''
Created on 10-Sept-2025

@author: Admin
'''

class a:
    def __init__(self):
        print("i")
        
class b(a):
    def tejas(self):
        print("j")

class c(a):
    def tejas(self):
        print("z")
        
class d(b,c):
    #def tejas(self):
        print("o")

#cu=c()       
du=d()
du.tejas()
#cu.tejas()


a=input("eer the number")
b=input("enter he number 2")

print(a+b)


list1=[10,20,30]
list2=[30,40,50]
print(list1+list2)