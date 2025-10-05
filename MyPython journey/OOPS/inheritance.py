'''
Created on 10-Sept-2025

@author: Admin
'''

'''
Created on 10-Sept-2025

@author: Admin
'''

class GrandFather:
    def function_work(self):
        print(" i iam a grandfather")
        
class Father(GrandFather):
    def function_j(self):
        print(" i am the Father")
    def car(self):
        print("Fathers car")
class Mother():
    def function_m(self):
        print("Ia m the mother")
    
    def car(self):
        print("Mothers car")
        
class children(Father,Mother):
    def function_c(self):
        print("Ia m the child")
        
p=Father()
p.function_work()
p.function_j()

c=children()
c.function_m()
c.car()

print(children.mro())
print(c.__dir__())

        
    
