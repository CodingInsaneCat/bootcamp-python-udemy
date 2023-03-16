print("Welcome to the pizza delivery La Brasiera")

size = input("What size pizza do you want? S, M ,L: ")
add_peperonni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


if size == "S":
    if add_peperonni == "Y":
        if extra_cheese == "Y":
            final_bill  = 15 + 2 + 1
            print(f"For small pizza with extra pepperoni and extra cheese the price is ${final_bill} bucks")
        else:
            final_bill = 15+2
            print(f"For small pizza with extra pepperoni and extra cheese the price is ${final_bill} bucks")
    else:
        
    else:
        final_bill = 15
        print(f"For small pizza with extra pepperoni and without extra cheese the price is ${final_bill} bucks")
elif size == "M":
    print ("Medium Pizza $20")
else:
    print("Large Pizza $25") 