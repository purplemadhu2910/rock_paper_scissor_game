import random
while True:
    print("Choose your move: ")
    #user must select the move to play
    user_choice = input("'r' for rock, 'p' for paper, 's' for scissor\n")
    
    computer_choice = random.choice(['r','p','s'])
    #if user does not want to play the game type q to exit from the game
    if user_choice == 'q':
        print("Thanks for playing")
        break
    #user must select from r,p,s else the game is over
    if user_choice not in ['r','p','s']:
        print("Invlid choice! please selct r,p,s")
        break
        
    
    if user_choice == computer_choice:
        print("Tie")
    elif (user_choice == 'r' and computer_choice == 's'
          or user_choice == 's' and computer_choice == 'p'
          or user_choice  == 'p' and computer_choice == 'r'):
        print("User wins")
    else:
        print("Computer wins")
        print(computer_choice)

