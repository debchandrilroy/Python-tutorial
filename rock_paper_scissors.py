import random

print("wellcome to ROCK PAPER SCISSORS")

print("Wining rules for the game: \n"
      +"Rock vs Paper-->Paper Win \n"
      +"Paper vs Scissors-->Scissors Win \n"
      +"Rock vs Scissors-->Rock Win")

while True:
    print("Rock:1 \n"
          +"Paper:2 \n"
          +"Scissors:3")
    choice=input("What is your Choice:")
    choice = int(choice)
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺'))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print(choice_name)

    print("Now its computer turn......")

    comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='paper'
    else:
        comp_choice_name='Scissors'
        
    print("Computer choice is", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        result = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        result = 'Rock'
     # Printing either user or computer wins or draw
    
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")