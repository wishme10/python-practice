print("Hello, World!")  
age=20
price=19.99
print (age, price, sep="\n")
first_name= "john"
is_online = False
first_name = "john"
last_name = "smith"
print (first_name , last_name)
print (f"we checked in a patient named {first_name} {last_name}")
print (f"he is {age} years old")
print ("he is a new patient")
name=input ("what is your name? ")
print ("hello" + name)
name = input ("what is your name? ")
print ("hello" +name)
age = input ("your age : ")
print ("hello" +name +age)
age = int (input("your age: "))
print (age + 5)
birthdate=input ("enter your birthdate: ")
right_age = 2020- int(birthdate)
print (age)
simple calculator
first_nub= float(input ("give your first_nub: "))
second_nub= float(input ("give your second_nub: "))
print ("sum: " +str(first_nub + second_nub))
course = "genz are cockcroaches"
print (course.replace("genz", "millenials"))
print (course.find("gen"))
print ("croaches" in course)
print (3 + 5)
print (3 - 5)
print (3/2)
print (3//2)
print (3 % 2)
print (3 ** 2)
x = 3
x = x + 3
print (x)
x = 6
x += 2
print (x)
x -= 2
print (x)
x %= 2
print (x)
x **= 2
print (x)
x = (3 + 2) * 4
print (x)
x = 10 > 9
print(x)
x = 10 < 9
print (x)
x = 10 >= 9
print (x)
x = 10 != 9
print (x)
x = 10 ==9
print (x)
price = 25
print( price >10)
print (price >10 and price <40)
print (price >30 or price <40)
print ( not price >30)
temperature = 35
if temperature >30: 
    print("its a hot day")
    print ("drink plenty of water")
temperature = 25
if temperature >30: 
    print("its a hot day")
    print ("drink plenty of water")
print ("done")
temperature = 24
if temperature >30: 
    print("its a hot day")
    print ("drink plenty of water")
elif temperature >20: 
     print ("it's a nice day")
elif temperature >10: 
     print("it's a bit cold")
else:
     print("its cold day")
print("done")
weight= float(input ("what is your weight? "))
unit=input("(K)g or (L)bs: " ).upper()
if unit == "(L)bs" or unit == "L":
     conversion = weight * 0.453592 
     print(f"coversion in Kilograms = {conversion}" )
elif unit == "(K)g" or unit == "K": 
     conversion = weight / 0.453592
     print(f"conversin in Pounds = {conversion}")
else:
     print("write (K)g or (L)bs")



age = int(input("type your age: "))
if age <= 25: 
    print("you are young as your age is " + str(age) ) 
elif age > 25  and age <= 50: 
    print(f"your are mature as your age is {age}")
elif age > 50: 
    print ("you are old")
else:
    print("please enter correct age")

a = 2
while a <= 50:
    print(a)
    a += 2
a = 3
while a <= 15:
     print(a * "*")
     a += 1





