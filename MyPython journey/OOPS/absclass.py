'''
Created on 13-Sept-2025

@author: Admin
'''
from abc import ABC, abstractmethod


class car(ABC):
    def move_forward(self):
        print("its moving fowrad")
    
    @abstractmethod    
    def vivek_god(self):
        pass
    
class human(car):
    def move_backward(self):
        print("its going back")
    
    
    def vivek_god(self):
        print("its great")
        
h=human()
h.move_backward()
h.vivek_god()
#c=car()
#c.vivek_god()
#c.move_forward()