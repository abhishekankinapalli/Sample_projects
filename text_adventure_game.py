# A simple text-based adventure game.
def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest. You can go 'left' or 'right'.")
    choice = input("Which way do you want to go? ")
    
    if choice == "left":
        print("You found a treasure chest! You win!")
    elif choice == "right":
        print("You fell into a pit. Game over!")
    else:
        print("Invalid choice. Try again.")
        start_game()

start_game()
