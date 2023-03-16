height= float(input("Type your Height:"))
weight = float(input("Type your Weight"))

#f-string


calculus_bmi = round(weight/(height * height),2)

# Sempre adicionar a letra F minusculo no inicio da frase para conseguir fazer a interpolacao dessa bagaca de F-String 


print(f"You score is {calculus_bmi} and your fucking Weight is {weight} and your fucking height is {height}")
print("Your body composition is " + str(calculus_bmi))

