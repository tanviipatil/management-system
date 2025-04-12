def welcome():
    print("welcome to the conloop program!")
    welcome()

def name(userName):
    print(f"Hello,{userName}!")
    name("kishore")

def add(a,b):
    return a+b
sum = add(5,3)
print(f"The sum of 5 and 3 is :{sum}")
        

#for loop

for i in range(5):
    print(i)

#odd num
for i in range(1,10,2):
    print(i)

#even num
for i in range(0,10,2):
    print(i)

colors = ['red','blue','green','yellow']
for color in colors:
    print(color)

#for loop with else
for i in range (2):
    print(i)
else:
    print("loop ended")

#break statement
for i in range(5):
    if i ==3:
        break
    print(i)

for i in range(5):
    if i ==3:
        continue
    print(i)

