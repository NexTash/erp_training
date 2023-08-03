# variable
x = 10

# list
ages = [10, 20, 36]

for index, value in enumerate(ages):
    print(index, value)

# dict
ages_with_names = {
    "Amjid": 25,
    "Ali": 18,
    "Abdullah": 27,
    "Faisal": 25
}

print("\t\t\t\tSearch age by name")

name = input("Give name of the Member: ")
age = "not exist"

if name in ages_with_names:
    age = ages_with_names[name]

print(f"Age of {name} is", age)