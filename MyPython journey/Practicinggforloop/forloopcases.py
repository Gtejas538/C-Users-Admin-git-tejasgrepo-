'''
Created on 18-Jul-2025

@author: Admin
'''

#printig a sqauare using Practicinggforloo
"""n = 5  

for i in range(n):  
    for j in range(n):  
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:  
            print("*", end=" ")  
        else:  
            print(" ", end=" ")  
    print()
  """    
# program to print increasing pyramid
"""n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print("")"""
    
#reverse number triangle pattern
"""rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows+1):
    for j in range(1, rows+1):
        if j>i-1:
            print(j, end="")
    print( )"""
        
#zero one triangle
"""rows = int(input("Enter the number of rows for the 0-1 triangle: "))

for i in range(1, rows + 1):  
    for j in range(1, i + 1):  
        if (i + j) % 2 == 0:  
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()  """
    
#reverse pyramid
"""rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows+1):
    for j in range(1, rows+1):
        if j>i-1:
            print("*", end="")
    print()
"""        

"""#reverse right hand pyramid
for i in range(1,6):
    for j in range(1,6):
        if j>=i: i1 j5 , i2 
            print("*", end="")
    print()"""
            
"""#left half pyaramid
rows = 5
for i in range(1, rows + 1):
        # Print spaces for alignment
    print(" " * (rows - i), end="")
        # Print stars
    print("*" * i)

# Example usage: k pattern
for i in range(4):
    print("."*(4-i), end="")
    print("")
for j in range(4):
    print("."*(j+1), end="")
    print("")
"""
""" 
    
#reverse number triangle attern
"""
j=4
for i in range(4):
    for z in range(1,5):
        if i<z:
            print(z,end="")
        elif i>0:
            print(" ",end ="")
        
        # elif i==z:
            # print(" ")
            
            
    print()
       ##fitst add space and later number      
             
#reverse right hand pyramid

for i in range(0,5):
    for j in range(1,6):
        if j>i:
            print("*", end="")
    print()
              
        
    
        
        
        
        
    

    
       
        
        
    
        