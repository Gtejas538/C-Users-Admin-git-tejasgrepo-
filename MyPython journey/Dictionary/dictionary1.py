'''
Created on 26-Jul-2025

@author: Admin
'''

dict11={}
print("Type of dictionary is ",type(dict11))

dict2={1:"ganashree",2:"Kannada Kasturi",3:"Nitin"}
print("dict2-->",dict2)

dict3=dict(one="shreyas big shot ", two="nitin")
print("dict3--.",dict3)

#dict wont take duplicate values, it would merge all duplicate values and show it as one
#if key and value borth same it wont print it gain
dict4={1:"ganashree", 2:"kannada kasturi",3:"nitin",3:"nitin"}
print(dict4)

#uisng duplicate keys and diffrent value,it will take the last value and current value

dict10={1:'ganashree',2:"kannada kasturi",3:"nitin",3:"vivek"}
print(dict10)

#uisng same dupicae value and diffrent keys
dict58={1:'ganashree',2:"kannada kasturi",3:"nitin",4:"nitin"}
print(dict58)

#accesing elemt try to use indexing:it wont  take index value it will take key value hence is hping error at dict58[0]


print(dict58)
#print(dict58[0]) key erro as it accepsts key value not index value
print(dict58[1])
print(dict58[3])

print("try to access using for loop")
#uisng for loop try to acees dcitionary key and value
for i in dict58:
    print(dict58[i])
    
#sliicng operator not supporting
#dict58[1:3]
#how to modify elemntsi dictionar it canbe moidfied uidng key value and citionary
dict58[1]="tiger power"
print(dict58)

dict58[87]="tejas power"
print(dict58)
 
#viveksir assihment
l=list('HELLO')
p=l[0],l[-1],l[1:3]
print(p)
print('a={0},b={1},c={2}'.format(*p))

i=1
while True:
    if i%0o7==0:
        break
    print(i)
    i+=1

numc=0
list39=[8,9,10,7]
"""while numc<len(list39):
  currentlist=list39[numc]
    
    
print(currentlist)"""
dict34={1:"jai",2:"tejas",3:"shereyas"}
dict35={1.0:"dummy",2.0:"dummy",3.0:"legend"}

dict34.update(dict35)
print(dict34)