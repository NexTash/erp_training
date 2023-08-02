x = input("Give first number: ")
y = input("Give second number: ")

x = int(x)
y = int(y)

print(f"\n\n")
print(f"Sum  \t\t : {x+y}")
print(f"Product  \t : {x*y}")
print(f"Subtraction  \t : {x-y}")
print(f"Division  \t : {x/y}")

# conditions
if x>y:
    print("Amjad Gandoo hai")
    
    if x == 10:
        print("waqai?")

else:
    print("Amjad Muthal hai")

# loops
num = input("which number you want to print table")
num = int(num)
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")