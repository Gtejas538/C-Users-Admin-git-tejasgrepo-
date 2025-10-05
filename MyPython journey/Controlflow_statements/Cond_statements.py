'''
Created on 12-Jul-2025

@author: Admin
'''

#age = int(input("please enter your  age : "))
"""if age>18:
    print("allow inside")
    
else:
    #print("dont allow")"""
    
    
"""if age<=0:
    print(" invalid age")
elif age >0 and age <13:
    print("we are a teenager")
    
elif age >= 13 and age <= 18:
    print("you are adult")
elif age>18 and age<60:
    print("you are an adult")
else:
    print("you are senior citizen")
    """
# this will work even withput uisng add and less than ,sir has igven the prigram we need to write the flowchart

"""tejas = int(input("please enter his age: "))

if tejas <= 0:
    print("please enter valid input")
elif tejas > 18:
    if tejas > 60:
        print("you are a senior citizen")
    else:
        print("you are adult")
else:
    if tejas<13:
        print("you are a child")
    else:
        print("you are teenager")
        
        
        """
        
#write a prgram wheter number is even or noot

"""tejasnum =int(input("enter a number"))

if(tejasnum % 2!=0):
    print("itsa odd number")
else:
    print(" its a even number")"""

"""#program to convert temperature from celsuis to fareheint or vicversa
c1 = input(" enter yes  for convert temperature from celsuis to fareheint")
d1 = input(" enter yes  for converting temperature from fareheint to celsuis")

if c1 == "yes":
    c = float(input("enter the celsius value "))
    result1 = (c * 9/5) + 32

    print(result1)
    
if d1 == "yes":
    f=float(input("enter the Fahrenheit value"))
    celsius = (f - 32) * 5/9
    print(celsius)
    

#Vivek sir
#no = int(input("Enter the value of the number :"))

#1. number is positive negative or zero

if(no > 0):
    print(" its a positive number ")
elif(no < 0):
    print(" its a negative number")
else:
    print("its a zero")   """

#2 number is even or odd
"""
if (no % 2 ==0):
    print("its a even number")
else:
    print("its a odd number")
    """
#3 largest of two numbers

#no1 = int(input("Enter the value of the number1 :"))
#no2 = int(input("enter the value of the number2 :"))
"""
if(no1 > no2):
    print("number1 is bigger than number2")
else:
    print("number2 is bigger than number1")
    
    """
    
#4 largest of three numbers
"""
no3 = int(input("enter the value of num3 :"))
if no1>no2>no3:
    print("number 1 is greater")
elif no2>no1>no3:
    print("number 2 is greater")
elif no3>no2>no1:
    print("number 3 is greater")
"""
  
#5 whether chracter is a voel or consant like take a ,i ,o ,u,e
"""
ch = input("enter a string value ")
if ch == "A" or ch =="a":
    print("its a vowel")
else:
    print("its a constant")
"""
  
#6 check if its leap year or not
"""
year = int(input("enter the year : "))
if year % 4 ==0:
    print("its a leap year")
else:
    print("its not a leap year")
    
    
#7 this is already done
#8 if a string is e mpty or not
str1 = input("enter the string")
if str1 == "":
    print(" string is empty")
else:
    print("string is not empty")
    

#9 chek number didivisble by 5 nad 11
thenumber = int(input("enter the number"))

if thenumber %5 == 0 and thenumber %10 == 0:
    print("number is divisible by 5 and 10")
else:
    print("not divisible"
          )
    
#10 if charater is alaphaet ,didgit or special
charvar = "9"
if charvar.isalpha():
    print("it is an alphabet")
elif charvar.isdigit():
    print(" it is a digit")
else:
    print("it is  a special character")
    
#11:grade a student based on marks
grade=int(input("enter a student grade"))
if grade >=90 and grade <=100:
    print("grade is a")
elif grade >=80 and grade<90:
    print("grade is b")
elif grade >=70 and grade<80:
    print("grade is c")
elif grade >=60 and grade<69:
    print("grade is d")
elif grade <60:
    print("grade is f")
else:
    print("invalid grade")

#12
a = int(input("Enter the value of the sidea :"))
b= int (input("enter the value of sideb  :"))
c = int(input("Enter the value of sidec :"))

if a>0 and b>0 and c>0:
    if a + b > c and a + c > b and  b + c > a:
        print("triangle is valid ")
    else:
        print("not valid")
else:
    print("invalid value")
    
#16
balance = int(input("enter the balance "))
amount=int(input("enter the amount to be withdrawn"))
if balance - amount > 0 and amount % 500 ==0 or amount %100==0:
    print("you can withdraw ")
else:
    print("no siifcient balance")
    
"""    
#sir teaching match sttemnt
"""choice = int(input(" do you want to conver from
1. celsuis to farhnet
2. Frahen to celsius"))
    
    match choice:
    case 1:
        print("conver to f")
    case 2:
        print("convert to c")
    case _:
        print(" please enter proper value")"""

#13 if number is mutiple of aother number 
"""jai = int(input("enter the main number  "))
jai2 = int(input("enter the number which is a mutiply of other we need to check"))

if jai%jai2 == 0:
    print("its a mutiple")
else:
    print("its not a mutiple")"""
    
#15 check its a armstring number

"""numberuu= int(input("Enter your number "))
temp = numberuu
sum = 0


while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
else:
    print()

# display the result
if numberuu == sum:
    print(numberuu,"is an Armstrong number")
else:
    print("its not armstrong number")    
           

#14 if a person can doante blood

ageee=int(input("enter the age of the person"))
weightee=int(input("enter the weightage"))

if ageee>18 and weightee>50:
    print("the person can donate blood")
else:
    print("person cannot donate the blood")
    
#17 electicity bill calculation
j=int(input("enter the no of units used"))


if j<=100:
    payamount=j*5
    print(f"the amount tp be payed is {payamount}")
elif j>100 and j<200:
    payamount=(j-100)*7+(100*5)
    print(f"the amount to be payed is {payamount}")
elif j>200:
    payamount+=(j*10)
else:
    print("over")    
"""

#20calcator program
"""print("Calculator")
print()
a=int(input("enter the first number"))
b=int(input("enter the second number"))

zoperator=input("Please enter the operation that needs to be performed among this : +,-,*,/,%")
match zoperator:
    case '+':
        result=a+b
        print(f"the result of the operation is {result}")
    case '-':
        result=a-b
        print(f"the result of the operation is {result}")
    case "*":
        result=a*b
        print(f"the result of the operation is{result}")
    case "/":
        if (a>0) or (b>0):
            result=a/b
            print(f"the result of the operation is{result}")
        else:
            print("invalid input")
            exit()
    case "%":
        if (a>0) or (b>0):
            result=a%b
            print(f"the result of the operation is {result}")
        else:
            print("invalid input")
            exit()
    case 'default':
            exit()
"""    
#18 simple login system
username="tejasg"
password="tejasgreat"

print("     Login system      ")
username1=input(" Enter the username")
password1=input("Enter the password")
if username1==username and password1==password:
    print(" Login is done ")
elif username1=="" or password1=="":
    print("Please enter the username and  password together")
else:
    print("incorrect username or password")     
        
#19 bust ticket fare 
print("   Bus Ticket for Madakasira to Pavagada ")

original_ticketrate=50
ticket_rate = 0
fareflag=int(input("Enter the age of the person"))
if fareflag<5:
    print("The fare is free")
    print(f"The ticket rate is {ticket_rate}")
elif fareflag>=5 and fareflag<=18:
    ticket_rate = original_ticketrate * 0.5
    print(f"The ticket rate is {ticket_rate}")
elif fareflag>18:
    ticket_rate = original_ticketrate
    print(f"The ticket rate is {ticket_rate}")
    
    
    

