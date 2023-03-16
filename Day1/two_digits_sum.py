number_initial = input("Type a number")

while int(number_initial) > 99:

    number_initial = input("Type a number")
    print("You have typed a number with 3 decimals places, try again")

#basic function 
number_one = number_initial[0]
number_two = number_initial[1]




sum_numbers = int(number_one) + int(number_two)
print(number_one)
print(number_two)
print("The sum of the 2 digits numbers is : " + str(sum_numbers))