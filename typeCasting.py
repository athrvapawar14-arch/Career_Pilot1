"""

# this is an example code for type casting.

# without type casting
a = 20
b = 5.5
c = a/b
print(c)


# with type casting
c = a/b
print(int(c))


"""

# name, coffee, bill, total

print("="*20 + "Le Cafe" + "="*20)

name = input("Customer Name: ")

menu = { "Filter" : 20 , "Black" : 40 , "Chocolate" : 60 }

coffee = []

while True:
    choice = input("your choice: ")
    if choice == "0":
        break
    coffee.append(choice)

    
total = 0


for item in coffee:
    if item in menu:
        total = total + menu[item]
     


# Bill printing. 

print("="*20 + "Bill" + "="*20)

print(name)
print(total)

print("="*45)









