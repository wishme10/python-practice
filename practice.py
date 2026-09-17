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
# simple calculator
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
# if else statement
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

# while loop
a = 2
while a <= 50:
    print(a)
    a += 2
a = 3
while a <= 15:
     print(a * "*")
     a += 1
a = 1
while a <= 5:
    print (a)
    a += 1

# list
names = ["john", "mosh", "sara", "adam"]
print (names)
names = ['sara', 'ali', 'mahad', 'john', 'robit' ]
names [4] = "robt"
print (names)
names = ['sara', 'ali', 'mahad', 'john', 'robit' ]
print (names [2])
names = ['sara', 'ali', 'mahad', 'john', 'robit']
print (names [1:4])
names = ['sara', 'ali', 'mahad', 'john', 'robit']
print (names [-3])

# list methods
nub = [1, 2, 3, 4, 5]
nub.append (6)
print (nub)
nub = [1, 2, 3, 4]
nub.remove (2)
print (nub)
nub = [2, 4, 6, 8, 10]
nub.insert (2, 5)
print (nub)
nub = [2, 4, 6, 8, 10]
nub.clear ()
print (nub)
nub = [2, 6, 9, 5, 0, 3]
print ( 5 in nub)
nub = [2, 5, 9, 8, 10, 3, 1, 7]
print (len (nub))

# forloop
numbers = [1, 2, 3, 4]
for items in numbers:
    print (items)

# another way using while loop
numbers = [1, 2, 3, 4]
i = 0
while i < len(numbers):
    print (numbers [i])
    i += 1

# the range () function
nub = range (5)
print (nub)
nub = range (5)
for numbers in nub:
    print (numbers)
nub = range (5, 10)
for value in nub:
    print (value)
nub = range (5, 10, 3)
for item in nub:
    print (item)
for nub in range (5, 10, 2):
    print (nub)
 #tuples
numbers = (1, 2, 4, 5, 5)
print (numbers.count (5))
print (numbers.index(4))

names = ["john", "adam", "jimmy", "peter"]
i = 0
while i <= 2:
    print (names[i])
    i += 1
nub = [1, 10, 67, 50, 62, 23]
i= nub[0] 
for value in nub:
    if value > i:
        i = value
print(i)

