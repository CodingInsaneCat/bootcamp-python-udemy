#year = int(input("Which year do you want to check?"))
year = [1804, 1808, 1812,2100]

#First step to check 

for i in range(len(year)):
    print(year[i])
    if (year[i] % 4 == 0 and year[i] % 100 !=0) or (year[i] % 4 == 0 and year[i] % 100 ==0 and year[i] % 400 == 0):
        
        print(f"The Year {year[i]} is a Leap year")
    else:
        print("Is not leap year")
# print(year % 4 == 0)
# print(year % 400 == 0)
# if year % 4 == 0 and year % 400 != 0:
#     print("Leap Year")

