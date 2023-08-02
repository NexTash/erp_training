# while loop

check = "y"
while check == "y":
    print("amji")
    check = input("want to reprint, press y, to terminate press any other key: ")

# for
for i in range(1, 11):
    print(i)

# list
ages = [10, 20, 30, 52, 52, 50]
for i in ages:
    print(i)

# dict
ages_with_names = {
    "amjid": 25,
    "ali": 18,
    "Abdullah": 27,
    "Faisal": 25
}

for i in ages_with_names:
    print(i, "=>", ages_with_names[i])