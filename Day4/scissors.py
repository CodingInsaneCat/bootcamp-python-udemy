import random 

## Pedra, Papel e Tesoura para escolha

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors"))

random_choice_computer = random.randint(0,2)

print(f"Escolha gerada aleatória {random_choice_computer}")

#Logica para o caso do usuário escolher Pedra
if user_choice == 0:
    print(rock)
    if(random_choice_computer) == 1:
        print(paper)
        print("You Lose!")
    elif random_choice_computer != 0:
        if random_choice_computer == 2:
            print(scissors)
        else:
            print(paper)
        print("You Win")
    elif random_choice_computer == 0:
        print("Computer chooice")
        print(rock)
        print("Draw")
    else:
        print("You Win!")
        
#Lógica para caso o usuário escolha papel
elif user_choice == 1:
    print(paper)
    if(random_choice_computer) == 0:
        print(rock)
        print("You Win!")
    elif random_choice_computer != 1:
        if random_choice_computer == 2:
            print(scissors)
            print("You Lose!")
        elif random_choice_computer == 0:
            print(rock)
            print("You Win")
    elif random_choice_computer == 1:
        print("Computer chooice")
        print(paper)
        print("Draw")

elif user_choice == 2:
    print(scissors)
    if(random_choice_computer) == 0:
        print(rock)
        print("You Lose!")
    elif random_choice_computer == 1:
        
            print(scissors)
            print("You Win!")
            if random_choice_computer == 0:
             print(rock)
             print("You Lose")
    elif random_choice_computer == 2:
        print("Computer chooice")
        print(scissors)
        print("Draw")
   
        

