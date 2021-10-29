# python program - Rock-Paper_scissors game

def rock_paper_scissors(a,b):
    if a == '1': # player 1 is rock
        if b == '2': # player 2 is scissors
            return '1'
        else: # player 2 is paper
            return '2'
    elif a == '2': # player 1 is scissors
        if b == '1': # player 2 is rock
            return '2'
        else:     # player 2 is paper
            return '1'
    elif a == '3' : # player 1 is paper
        if b == '1': # player 2 is rock
            return '1'
        else: # player 2 is scissors
            return '2'

def main():
    game = '1'
    while game == '1':
        print("Playing Rock-Paper-Scissors")
        print("Player 1 choice")
        print("Please enter number :")
        print("[1] Rock  [2] Scissors  [3] Paper")
        player_1 = input()
        print("Player 2 choice :")
        print("Please enter number :")
        print("[1] Rock  [2] Scissors  [3] Paper")
        player_2 = input()
        if player_1 in ['1', '2', '3'] and player_2 in ['1', '2', '3']: # checks that a valid input was enter
            if player_1 == player_2:
                print("It's a Draw!")
            else:
                print("Player " + str(rock_paper_scissors(player_1, player_2)) + " Win! Congratulations!")
            end_game = '0'
            while end_game == '0':
                print("Do you want to play another game?")
                print("[1] Yes  [0] NO")
                temp = input()
                if temp in ['0', '1']: # checks that a valid input was enter
                    end_game = 1
                    game = temp
                else:
                    print("Please choose from the given choices\n")
        else:
            print("Please choose from the given choices\n")


if __name__ == '__main__':
    main()