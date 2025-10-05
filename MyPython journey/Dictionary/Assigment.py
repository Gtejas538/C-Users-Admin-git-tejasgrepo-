'''
Created on 01-Aug-2025

@author: Admin
'''
dict10={1:"good",2:"bad",3:"ugly"}
#print(dict10.pop()) it will show error as pop function will take atlat one arg
print(dict10.pop(3))
print(dict10)#it will remove value with the given key

#print(dict10.pop(0))  it will give the key error

#it will print the keys and values
print(dict10.keys())
print(dict10.values())

#print(dict10.keys(0))
#print(dict10.values(0)) it wont take any arguement

#if key is existing it wont change value , it not it will add key and value to duct

dict1=dict10.setdefault(1,"dummy")
dict2=dict10.setdefault(50,"shreyas")
print(dict1)
print(dict2)
print(dict10)


#in for loop we can print values or else it will print key items
for i in dict10.values():
    print(i)
    
for j in dict10:
    print(j)
    
    
dict5={"3":"67","4":"76","5":"98"}
del(dict5["5"])
print(dict5)
#del(dict5)
#print(dict5)
print(dict5)
#popitem will rmeove the last element of the dict
#dict5.popitem()
#print(dict5)

#print(dict5.pop("3", "key not there"))
#print(dict5)

print(dict5.pop("1", "key not there"))


#lastindex of maximum element
mylist=[1,5,5,5,5,5,5,1]
max=mylist[0]
indexOfMax=0
for i in range(1,len(mylist)):
    if mylist[i]>=max:
        max=mylist[i]
        indexOfMax=i

print(indexOfMax)

#firstindex of lesr number
mylist=[5,1,5,5,5,1]
least=mylist[0]
indexe=0
for i in range(1,len(mylist)):
    if mylist[i]<least:
        least=mylist[i]
        indexe=i
print("index of lest number is",indexe)

#lastindex of leas number
mylist1=[1,5,5,5,5,1,5,5,1]
indexlast=mylist[0]
for j in range(1,len(mylist1)):
    if mylist1[j]<=indexlast:
        indexlast = j
print("last index of the last number",j)


#string operation
s="a@b@c@d"
print(s.partition("@"))
print(s.split("@",3))

