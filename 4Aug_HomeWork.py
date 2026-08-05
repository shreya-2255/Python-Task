# Task 1: Identity Card
name = "Smruti"
age = 21
city = "Pune"
dob = "22/11/2004"
college = "TKA"
blood_group = "A+"

print("----- My ID Card -----")
print("Name =",name)
print("Age =",age)
print('City = "'+ city + '"')
print("dob = ", dob)
print('College = "' + college + '"')
print("Blood Group = ", blood_group)

# Output: 
# ----- My ID Card -----
# Name = Smruti
# Age = 21
# City = "Pune"
# dob =  22/11/2004
# College = "TKA"
# Blood Group =  A+
           
# Task 2: Find Data Type

a =  25
b = 25.5
c = "twenty Five"
d = True
e = 2 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e)) 

# Output: 
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'complex'>

# Task 3: Memory Detective

v1 = 100
v2 = 200
v3 = 100

print(id(v1))
print(id(v2))
print(id(v3))

# Output: 
# 140731611599064
# 140731611602264
# 140731611599064
