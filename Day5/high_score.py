students_heights = input("Input a list of students heights").split(",")


high_score = 0
size = len(students_heights)
for heigth in students_heights:
    if int(heigth) > int(high_score):
        high_score = heigth


print(f"The highest score is {high_score}")

