list_height = input("Type the numbers using commas to separated grades:")
int(list_height.split(","))


soma = 0
for notes in list_height:
    print(type(notes))
    print(type(soma))
    soma = soma + notes
    
print(soma)