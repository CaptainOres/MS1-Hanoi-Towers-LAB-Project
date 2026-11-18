# Integrity pledge: I Skylar McColl declare that the following work was done by yours truly. 
# --------------------------------------
# Name:         Skylar McColl
# Program:      LABSMS1Q2.py
# --------------------------------------

'''
Purpose: To create a text based interface to play the game Hanoi Towers, and the use of stacks in addition to any other required and relevant data structures. Then being able to use and store a game session with binary files, then be able to pick up where you left off.
'''

import pickle

def load_game(file_name):
    # load game here
    print("loading save...")
    
    try:
        with open(file_name, "rb") as file:
            game_state = pickle.load(file)
        print("Save loaded successfully!")
        return game_state
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")
    
    return None



def save_game(game_state, file_name):
    with open(file_name, "wb") as file:
        pickle.dump(game_state, file)
    print(f"Game saved to {file_name}!")



def start_game():
    # make game here  -- YOU NEED TO DO ERROR CHECKING HERE!!!
    tower_num = int(input("Number of towers [min=3,..,max=9]? "))
    disk_num = int(input("Number of disks [min=3,..,max=9]? "))
    goal_tower_num = int(input(f"Target Tower [min=2,..,max={tower_num}]? "))
    
    game_state = {
        "pegs": tower_num,
        "num_disks": disk_num,
        "goal_tower": goal_tower_num,
        "moves": 0
    }
        
    print("New game started!")
    return game_state



def save_sel(start_sel):
    # error checking the start selection, and making said selection / file handling.
    
    if start_sel == 1:
        print("Starting a new game ............")
        return start_game() # Returns the new game state
        
    elif start_sel == 2:
        file_name = str(input("Enter file name (e.g.: game.p): "))
        return load_game(file_name) # Loads and returns the saved state
    else:
        print("Invalid selection.")
        return None



def main():
    
    print("WELCOME TO HANOI TOWERS GAME!\n")
    start_sel = int(input("Enter 1 to Start a new game and 2 to Resume a saved game: "))    
    game_state = save_sel(start_sel)
    print(game_state)
    