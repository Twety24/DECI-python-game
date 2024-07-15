import random

def intro():
    print("\nYou awaken in a mystical forest with towering trees and a faint mist swirling around your feet.")
    print("You have no memory of how you got here, but you feel an urge to explore.")
    print("Paths lead to the north, east, south, and west.")
    print("Choose a direction to begin your adventure.")

def choose_path():
    path = ''
    while path not in ['north', 'east', 'south', 'west']:
        path = input("Which direction do you choose? (north/east/south/west): ").lower()
    return path

def north_path():
    print("\nYou head north and encounter a wise old wizard who offers you a challenge.")
    if random.choice([True, False]):
        print("You solve the wizard's riddle and he rewards you with a magical amulet. You gain 50 points!")
        return 50
    else:
        print("You fail the wizard's riddle and he teleports you back to the forest entrance. You lose 20 points.")
        return -20

def east_path():
    print("\nYou head east and find a peaceful village. The villagers welcome you and offer you food and shelter.")
    print("You gain 30 points for your kindness and hospitality.")
    return 30

def south_path():
    print("\nYou head south and stumble upon a dark cave.")
    if random.choice([True, False]):
        print("Inside, you find a hidden treasure chest filled with gold. You gain 100 points!")
        return 100
    else:
        print("Inside, you are ambushed by goblins and lose some of your belongings. You lose 50 points.")
        return -50

def west_path():
    print("\nYou head west and discover an ancient ruin.")
    if random.choice([True, False]):
        print("Exploring the ruins, you find a powerful artifact that grants you wisdom. You gain 70 points!")
        return 70
    else:
        print("Exploring the ruins, you trigger a trap and barely escape with your life. You lose 40 points.")
        return -40

def game_over(score):
    print(f"\nYour adventure has come to an end. Your final score is {score} points.")
    choice = ''
    while choice not in ['yes', 'no']:
        choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

def main():
    playing = True
    while playing:
        score = 0
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
            
            continue_adventure = input("Do you want to continue exploring? (yes/no): ").lower()
            if continue_adventure != 'yes':
                break

        playing = game_over(score)
        if playing:
            print("\nStarting a new adventure...\n")

if __name__ == "__main__":
    main()