import csv
import random

#player name input
player_1=input("Player 1:")
player_2=input("Player 2:")

#read truth & dare from csv file
def read_truths_and_dares(truth_and_dare):
    with open(truth_and_dare, 'r') as csvfile:
        reader = csv.reader(csvfile)
        truths, dares = [], []
        for row in reader:
            truths.append(row[0])
            dares.append(row[1])
    return truths, dares

#to know user choice
def get_user_choice():
    while True:
        #random player Choice
        player=random.choice([player_1,player_2])
        print(f"spin to {player}")
        choice = input("Choose 'T' for Truth or 'D' for Dare (or 'Q' to quit): ").lower()
        if choice in ("t", "d", "q"):
            return choice
        print("Invalid choice. Please enter 'T', 'D', or 'Q'.")
#main code
def main():
    truths, dares = read_truths_and_dares('truth_and_dare.csv')
    while True:
        user_choice = get_user_choice()
        if user_choice == "q":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "t":
            print(f"Random Truth: " + random.choice (truths))
        elif user_choice == "d":
            print("Random Dare: " + random.choice(dares))
        else:
            continue

if __name__ == "__main__":
    main()
