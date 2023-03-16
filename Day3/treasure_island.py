print(''' 0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777
''')


directions_answer = input("Left or Right?")

if directions_answer.lower() == "right":
    print("Wrong,Game Over!")
elif directions_answer.lower() == "left":
    swim_question = input("Swim or Wait?")
    if swim_question.lower() == "swim":
        print("Wrong,Game Over!")
    elif swim_question.lower() == "wait":
        door_question = input("Which door?")
        if door_question.lower() == "red": 
            print("Wrong,Game Over!")
        elif door_question.lower() == "blue": 
            print("Wrong,Game Over!")
        elif door_question.lower() == "yellow": 
            print("You Win!!!!")
        