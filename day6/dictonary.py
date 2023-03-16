students_scores = {
    "Harry":76,
    "Ronald": 98,
    "Loraine":87,
    "Mariah":67

}


for key in students_scores:
    print(key)
    if students_scores[key] > 91:
        print("Outstanding")
    elif students_scores[key] >= 81 and students_scores[key] < 90:
        print("Exceceds Expectation")
        print(f"inside from looping Exceeds {students_scores[key] }")
    elif students_scores[key] >= 71 and students_scores[key] < 80:
        print("Loraine is a whore")
