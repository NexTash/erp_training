total_marks = 1100
marks_9th = int(input("Please Give 9th Marks: "))
marks_10th = int(input("Please Give 10th Marks: "))


obtain_marks = marks_10th + marks_9th

percentage = round(obtain_marks/total_marks*100)
# if
if obtain_marks > total_marks:
    print(f"Obtain Marks can not be higher than {total_marks}")
    exit()

print(f"You got {percentage}%")

# if else
# if else if
if percentage < 50:
    print("Fail")
elif percentage < 60:
    print("Pass")
elif percentage < 80:
    print("Pass With C Grade")
elif percentage < 90:
    print("Pass With B Grade")
elif percentage < 100:
    print("Pass With A Grade")
elif percentage == 100:
    print("Pass With A+ Grade")
else:
    print("Wrong Inputs")
