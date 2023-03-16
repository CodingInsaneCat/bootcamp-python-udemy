name = input("Please type your name:")
print(name)


for i in range(10):
    name = input("Please type your name:")
    print(name)


while name != "Giovanni":
    name = input("Please type your name:")
    if name == "Giovanni":
        print(f"Welcome, {name}")
    else:
        print("You are not welcome here, sorry bud :( ")