# Group Members: Emanuel Parungao, Skylar Mccoll
# Programming Project - Milestone #1

# ----- Tower Of Hanoi -----

# Program:      

import pickle

class Tower():
    
    '''
    Purpose: Stores information crutial for Tower Of Hanoi, aswell as the current game state.
    Attributes: (__init__(self, game_state)): _tower_num = ["pegs"], _disk_num = ["num_disks"], _target_tower = ["goal_tower"], _game_state = game_state
    '''
    
    
    def __init__(self, game_state):
        
        '''
        Purpose: To initialize the data stored currently inside the Tower class, and the data that may or may not be in game_state yet.
        Parameters: self, game_state
        Returns: None (but will hand off a initialized list version of _game_state["board"] to self if there isn't one.)
        '''        
        
        # for unpacking the current game_state dict. into the Tower class.
        self._tower_num = game_state["pegs"]
        self._disk_num = game_state["num_disks"]
        self._target_tower = game_state["goal_tower"]
        self._game_state = game_state
        
        # creating a starting run if one doesn't currently exist.
        if "board" not in self._game_state:
            
            # board state if starting new game is first tower with all the disks + empty towers for each tower in the number selected.
            self._game_state["board"] = [list(range(self._disk_num, 0, -1))] + [[] for tower in range(self._tower_num)]
     
           
    def build_tower(self):
        
        '''
        Purpose: To build the towers using the data of where the disks currently are and on which tower (keyed) in self._game_state["board"] This happens each iteration of the gameplay loop.
        Parameters: self
        Returns: None
        '''        
        
        board = self._game_state["board"]
        
        # Changed to allow for printing row by row for the towers to be inline with one another.
        gap = " "
        
        headers = []
        for tower in range(1, (self._tower_num + 1)):
            headers.append((self._disk_num * '=') + str(tower) + (self._disk_num * '='))
        
        print(gap.join(headers))
            
        # Looping through each row, zero being at the top and row num_disks - 1 at the bottom.
        for row in range(self._disk_num):
            row_pieces = []
            for tower_idx  in range(self._tower_num):
                current_disks = board[tower_idx]
            
                # If the tower has a disk in this row draw it, otherwise draw the pole.
                if row < len(current_disks):
                    disk_size = current_disks[row]
                    spaces = self._disk_num - disk_size
                    piece = (spaces * ' ') + (disk_size * '*') + '|' + (disk_size * '*') + (spaces * ' ')
                else:
                    piece = (self._disk_num * ' ') + '|' + (self._disk_num * ' ')
                        
                row_pieces.append(piece)
                    
            print(gap.join(row_pieces))
        print()
            
         
    #def victory_check(self):
        
        
            
    def move_disk(self, source_tower, dest_tower):
        
        '''
        Purpose: To manipulate disks and to ensure that the moves being requested by the user are valid with error checking.
        Parameters: self, source_tower, dest_tower
        Returns: None
        '''        
        
        # converting between tower numbers (1,2,3,..) into indexes (0,1,2,..).
        board = self._game_state["board"]
        source_idx = source_tower - 1
        dest_idx = dest_tower - 1
        
        # Prevents moving when the tower is empty.
        if not board[source_idx]:
            print(f"Invalid move. The source tower {source_tower} is empty. Please try again!\n")
            return self.build_tower()
        
        # Prevents the user from placing a larger disk on a smaller disk.
        disk = board[source_idx][-1]
        if board[dest_idx] and board[dest_idx][-1] < disk:
            print("Invalid move. Can't put a bigger disk on a smaller one. Please try again!\n")
            return self.build_tower()
        
        # For moving the top disk, also adding 1 to moves inside of game_state, then redrawing the towers
        board[source_idx].pop()
        board[dest_idx].append(disk)
        self._game_state["moves"] += 1
        self.build_tower()
        victory_check()
        
        
def error_check_int(prompt, min_val, max_val):
    
    '''
    Purpose: To have a helper function for error checking in our code for integers used mainly in the GUI.
    Parameters: prompt, min_val, max_val
    Returns: val
    '''    
    
    # keeps asking for a valid number until the user enters one.
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
                
            pass
        except ValueError:
            pass # Silently ignores the users wrong entry and allows for errors to be checked without a newline.
          
              
def load_game(file_name):
    
    '''
    Purpose: To load a saved game by converting a pickled binary file back into usable python objects, except when the file isn't found. 
    Parameters: file_name
    Returns: game_state, or None
    '''    
    
    # DEBUG: print("loading save...")
        
    try:
        with open(file_name, "rb") as file:
            game_state = pickle.load(file)
        print("Save loaded successfully!")
        return game_state
        
    except FileNotFoundError:
        print(f"file: {file_name} not found: Starting a new game................")
    return None
        
    
def save_game(game_state, file_name):
    
    '''
    Purpose: To save an existing game by convering the object data into pickled binary data and dumping it to a file.
    Parameters: game_state, file_name
    Returns: None (but will either overwrite data if the same name is used concurrently, or create a new file with the given name wherever this code is stored.)
    '''    
        
    with open(file_name, "wb") as file:
        pickle.dump(game_state, file)
    # DEBUG: print(f"Game saved to {file_name}!")
    
    
def start_game():
    
    '''
    Purpose: To ask the user using error_check_int for the starting parameters of the game, and then set up the game_state upon a fresh run.
    Parameters: None
    Returns: game_state
    '''    
    
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
        
    # DEBUG: print("New game started!")
    return game_state


def save_sel(start_sel):
    
    '''
    Purpose: A function for that uses the selection made to either start a new game == 1, or to input a file_name for an existing save and attempt to load it.
    Parameters: start_sel
    Returns: start_game() for 1 or when game_state is None, then it returns game_state
    '''
    
    if start_sel == 1:
        print("Starting a new game ............")
        return start_game()
    
    elif start_sel == 2:
        file_name = str(input("Enter file name (e.g.: game.p): "))
        game_state = load_game(file_name)
        
        if game_state is None:
            return start_game()
        return game_state
    
    
# Manager and display functions.
def display_towers(game_state):
    
    '''
    Purpose: To create the display for all the towers based on the current game_state for the starting board once during the program launch.
    Parameters: game_state
    Returns: towers
    '''
    
    towers = Tower(game_state)
    towers.build_tower()
    return towers
    
    
def next_steps(game_state, tower):
    
    '''
    Purpose: To have a function that allows the user to make a choice as to what they want to do next, either making a move, save and quit, or quit without saving.
    Parameters: game_state, tower
    Returns: None
    '''    
    
    while True:
        print("    1 - Move a Disk\n    2 - Save and End\n    3 - End without Saving\n")
        user_input = input("Enter 1 or 2 or 3: ")
        
        while user_input != '1' and user_input != '2' and user_input != '3':
            print("    1 - Move a Disk\n    2 - Save and End\n    3 - End without Saving\n")
            user_input = input("Enter 1 or 2 or 3: ")
        
        if user_input == '1':
            source_tower = error_check_int(f"Source Tower [1..{game_state["pegs"]}]? ", 1, game_state["pegs"])
            dest_tower = error_check_int(f"Destination Tower [1..{game_state["pegs"]}]? ", 1, game_state["pegs"])
            tower.move_disk(source_tower, dest_tower)
        
        elif user_input == '2':
            
            while True:
                file_name = str(input("Enter file name to save (e.g.: game.p): ")).strip()
                if file_name:
                    break
            
            save_game(game_state, file_name)
            print('Game Saved ......\nSee you later ......!')
            break
            
        elif user_input == '3':
            print('Ending Game ......\nGoodbye!')
            break
        
    
def main():
    
    '''
    Purpose: To have a main() function that acts as the executable responsible for operating the program.
    Parameters: None
    Returns: None
    '''    
    
    print("WELCOME TO HANOI TOWERS GAME!\n")
    # 
    start_sel = error_check_int("Enter 1 to Start a new game or 2 to Resume a saved game: ", 1, 2)
    game_state = save_sel(start_sel)
    print()

    towers = display_towers(game_state)
    next_steps(game_state, towers)
    
