'''
Created on 10-Sept-2025

@author: Admin
'''

class Grandfather:
    def __init__(self,name):
        print(" i am grandfather ")
        print(name)
        
class Father(Grandfather):
    def __init__(self,name,dob):
        print(" he is bad")
        print(f" name is {name } whose dob is {dob}")
        super().__init__(name)
        
class child(Father):
    def the_great(self):
        print("its me")
        
#f=Father()
c=child("tejas","89/21/2028")