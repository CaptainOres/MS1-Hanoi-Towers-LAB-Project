import pickle

class Tower():
    '''
    Purpose: Displays the tower(s) based on user inputs.
    Attributes (__init__): # of towers, # of disks, target tower
    Returns: NONE
    '''
    
    
    def __init__(self, game_state):
        
        # for unpacking the current game_state dict. into the Tower class.
        self._tower_num = game_state
        self._disk_num = game_state
        self._target_tower = game_state
        self._game_state = game_state
        
        # creating a starting run if one doesn't currently exist.
        
        if "board" not in self._game_state:
            
            # board state if starting new game is first tower with all the disks + empty towers for each tower in the number selected.
            self._game_state["board"] = [list(range(self._disk_num, 0, -1))] + [[] for tower in range(self._tower_num)]
     
    
    # the function for building the towers with the data of where the disks are and how big they are from _game_state.        
    def build_tower(self):
        board = self._game_state["board"]
        
        for tower in range(1, (self._tower_num + 1)):
            tower_key = (self._disk_num * '=') + str(tower) + (self._disk_num * '=')
            print(tower_key)
            
            current_disks = board[tower - 1]
            empty_slots = self._disk_num - len(current_disks)
            
            # printing the empty pole segments at the top of each tower.
            for diskless in range(empty_slots):
                print((self._disk_num * ' ') + '|' + (self._disk_num * ' '))
                
            # printing the actual disks on the tower from top to bottom.
            for disk_size in reversed(current_disks):
                spaces = self._disk_num - disk_size
                print((spaces * ' ') + (disk_size * '*') + '|' + (disk_size * '*') + (spaces * ' '))
            
            print('\n')
            
   
def error_check_int(prompt, min_val, max_val):
    # keeps asking for a valid number until the user enters one.
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
                
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.") 
          
    
# loads a saved game converting a pickled binary file back into usable python objects, except when the file isn't found.          
def load_game(file_name):
    print("loading save...")
        
    try:
        with open(file_name, "rb") as file:
            game_state = pickle.load(file)
        print("Save loaded successfully!")
        return game_state
        
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")
    return None
        
    
    # saves an existing game by convering the object data into binary and dumping it to a file.
def save_game(game_state, file_name):
    with open(file_name, "wb") as file:
        pickle.dump(game_state, file)
    print(f"Game saved to {file_name}!")
        
    
# asks the user using error_check_int for the starting parameters of the game, and sets up the game_state upon a fresh run.
def start_game():
    tower_num = error_check_int("Number of towers [min=3,..,max=9]? ", 3, 9)
    disk_num = error_check_int("Number of disks [min=3,..,max=9] ", 3, 9)
    target_tower = error_check_int(f"Target Tower [min=2,..,max={tower_num}]? ", 2, tower_num)
    
    # sets the game_state for a new game
    game_state = {
        "pegs": tower_num,
        "num_disks": disk_num,
        "goal_tower": target_tower,
        "moves": 0
    }
        
    print("New game started!")
    return game_state


def save_sel(start_sel):
    if start_sel == 1:
        print("Starting a new game ............")
        return start_game()
    
    elif start_sel == 2:
        file_name = str(input("Enter file name (e.g.: game.p): "))
        game_state = load_game(file_name)
        
        if game_state is None:
            print("Starting a new game instead ............")
            return start_game()
        return game_state
    else:
        print("Invalid selection.")
        return None
    
# ------ More to be added before main ------ #
    
    

    
    
def main():
    print("WELCOME TO HANOI TOWERS GAME!\n")
    # 
    start_sel = error_check_int("Enter 1 to Start a new game or 2 to Resume a saved game: ", 1, 2)
    game_state = save_sel(start_sel)
    print()

    
