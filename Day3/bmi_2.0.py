#height= float(input("Type your Height:"))
#weight = float(input("Type your Weight"))

#f-string


#calculus_bmi = round(weight/(height * height),2)
calculus_bmi = 178
# Sempre adicionar a letra F minusculo no inicio da frase para conseguir fazer a interpolacao dessa bagaca de F-String 

if calculus_bmi < 18.5:
    print(f"You score is {calculus_bmi} you are underweight")
elif calculus_bmi > 18.5 and calculus_bmi < 25:
    print(f"You score is {calculus_bmi} you are normal weight")
elif calculus_bmi > 25 and calculus_bmi < 30:
    print(f"You score is {calculus_bmi} you are overweight")
elif calculus_bmi > 30 and calculus_bmi < 35:
    print(f"You score is {calculus_bmi} you are obese") 
else:
    print(f"You score is {calculus_bmi} you are clinically obese") 
