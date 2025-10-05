'''/
Created on 14-Sept-2025

@author: Admin
'''

try:
    print(9/0)
    raise NameError('Hi There')
except TypeError as te:
    print(te,type())
except ZeroDivisionError as ze:
    print(ze,type(ze))
    
print("god is great")
    
