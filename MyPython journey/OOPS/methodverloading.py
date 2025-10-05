'''
Created on 13-Sept-2025

@author: Admin
'''

class A:
    def method1(self,a,b=0):
        result=a+b
        print(result)
        

a=A()
a.method1(3)
a.method1(3,5)


class B:
    def methodn(self,*args):
        print(args)
        
b=B()

b.methodn(1)
b.methodn(2,3)

