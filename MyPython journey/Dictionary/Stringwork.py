'''
Created on 02-Aug-2025

@author: Admin
'''
#single line string: singleoduble qupte ,songle single quotes
from ntpath import join
  # multi line sting    triple double quote ,tiple single quotes
  
stringn='my name is "vivek"'
print(stringn)
print(len(stringn))
print(stringn[11])
#triplesinglequote will print mutline comments 
multiline_string = '''This is a string
that spans
multiple lines.'''
print(multiline_string)
string4=stringn.capitalize()
print(string4)
print(stringn)
string5=stringn.casefold()
print(string5)
string89=stringn.center(38,"*")
print(string89)
string33=stringn.index("v")
print(string33)
string9=" ".join(["Today","is","saturday"])
print(string9)
print(stringn.split(" ",1))
print(string89.strip("*"))
print(stringn)
strnitin=stringn.strip(" ")
print(strnitin)

