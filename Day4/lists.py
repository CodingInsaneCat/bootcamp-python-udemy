import random as randomico

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(",")

print("Who will pay the bill??")

valor_gerado = randomico.randint(0,len(names)-1)
print(names[valor_gerado])
    #print(names[valor_gerado])
print(f"The {names[valor_gerado]} will pay the bills")