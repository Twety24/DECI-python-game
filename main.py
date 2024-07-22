import random
import time

# Function to display the introduction and initial choices
def intro():
    print("\nYou awaken in a mystical forest with towering trees and a faint mist swirling around your feet.")
    time.sleep(2)
    print("You have no memory of how you got here, but you feel an urge to explore.")
    time.sleep(2)
    print("Paths lead to the north, east, south, and west.")
    time.sleep(2)
    print("Choose a direction to begin your adventure.")

# Function to prompt the player to choose a direction
def choose_path():
    path = ''
    while path not in ['north', 'east', 'south', 'west']:
        path = input("Which direction do you choose? (north/east/south/west): ").lower()
    return path

# Function to handle the north path scenario
def north_path():
    print("\nYou head north and encounter a wise old wizard who offers you a challenge.")
    time.sleep(2)
    if random.choice([True, False]):
        print("You solve the wizard's riddle and he rewards you with a magical amulet. You gain 50 points!")
        return 50
    else:
        print("You fail the wizard's riddle and he teleports you back to the forest entrance. You lose 20 points.")
        return -20

# Function to handle the east path scenario
def east_path():
    print("\nYou head east and find a peaceful village. The villagers welcome you and offer you food and shelter.")
    time.sleep(2)
    print("You gain 30 points for your kindness and hospitality.")
    return 30

# Function to handle the south path scenario
def south_path():
    print("\nYou head south and stumble upon a dark cave.")
    time.sleep(2)
    if random.choice([True, False]):
        print("Inside, you find a hidden treasure chest filled with gold. You gain 100 points!")
        return 100
    else:
        print("Inside, you are ambushed by goblins and lose some of your belongings. You lose 50 points.")
        return -50

# Function to handle the west path scenario
def west_path():
    print("\nYou head west and discover an ancient ruin.")
    time.sleep(2)
    if random.choice([True, False]):
        print("Exploring the ruins, you find a powerful artifact that grants you wisdom. You gain 70 points!")
        return 70
    else:
        print("Exploring the ruins, you trigger a trap and barely escape with your life. You lose 40 points.")
        return -40

# Function to display the game over message and prompt the player to play again
def game_over(score):
    print(f"\nYour adventure has come to an end. Your final score is {score} points.")
    choice = ''
    while choice not in ['yes', 'no']:
        choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

# Main function to start and manage the game
def main():
    playing = True
    while playing:
        score = 0
        turns = 0
        max_turns = 5  # Condition to end the game after a certain number of turns
        intro()
        while True:
            path = choose_path()
        
            if path == 'north':
                score += north_path()
            elif path == 'east':
                score += east_path()
            elif path == 'south':
                score += south_path()
            elif path == 'west':
                score += west_path()
            
            print(f"\nYour current score is: {score} points.")
            turns += 1
            
            if turns >= max_turns:
                print("\nYou have reached the maximum number of turns for this adventure.")
                break

            continue_adventure = input("Do you want to continue exploring? (yes/no): ").lower()
            if continue_adventure != 'yes':
                break

        playing = game_over(score)
        if playing:
            print("\nStarting a new adventure...\n")

if __name__ == "__main__":
    main()
