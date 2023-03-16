students_heights = input("Input a list of students heights").split(",")

sum_heights = 0
size = len(students_heights)
for heigth in students_heights:
    sum_heights += float(heigth)

print(f"The average is {round(sum_heights/size,2)}")



