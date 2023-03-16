import random
import hangman_files

word_list = ["ovo", "abacate", "limao", "nariz", "puta", "nojenta", "prostituta", "mentirosa"]
correct_words = []
lives = 6


# Escolher uma palavra de maneira aleatória

chosen_word = random.choice(word_list)

# Mostrar a quantidade de espacos da palavra
for i in range(len(chosen_word)):
    correct_words.append("_")

print(f"A palavra escolhida tem o total de {correct_words} espacos")

# Solicitar ao usuário adivinhar uma palavra
# while correct_words != chosen_word:
end_of_game = False
print(f"TESTAND {not end_of_game}")
while not end_of_game:
    print(end_of_game)
    guess_word = input("Which letter do you want to try?").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess_word:
            correct_words[position] = letter

    if guess_word not in chosen_word:
        print(chosen_word)
        print(f"Vidas {lives}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(correct_words)
    if '_' not in correct_words:
        end_of_game = True
        print("You Win!!")

    print(hangman_files.stages[lives])
