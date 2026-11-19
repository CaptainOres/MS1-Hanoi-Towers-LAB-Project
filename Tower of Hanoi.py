# Group Members: Emanuel Parungao, Skylar Mccoll
# Programming Project - Milestone #1

# ----- Tower of Hanoi -----

# ----- Tower Class -----
class Tower():
    '''
    Purpose: Displays the tower(s) based on user inputs.
    Attributes (__init__): # of towers, # of disks, target tower
    Returns: NONE
    '''
    # 1. Instance Attributes:
    def __init__(self, num_towers, num_disks, target_tower):
        self._num_towers = num_towers
        self._num_disks = num_disks
        self._target_tower = target_tower
    
    # 2. Building Tower(s) From User Inputs In Main():
    def build_tower(self, counter, disk_stack, pole_stack, tower_stack):
        
        # Displays how many towers:
        for tower in range(1, (self._num_towers + 1)):
            tower_key = (self._num_disks * '=') + str(tower) + (self._num_disks * '=')
            print(tower_key)
            
            # Setting ONLY the first tower:
            if tower == 1:
            
                # Displaying length of tower as it goes down:
                for length in range(self._num_disks, 0, -1):
                
                    # Displaying space to form a triangle:
                    for spaces in range(counter, self._num_disks, 1):
                        disk = (spaces * ' ') + ((length - counter) * '*') + '|' + ((length - counter) * '*')
                        print(disk)
                        disk_stack.append(disk)
                        counter += 1
                        continue
                tower_stack.update({tower_key: disk_stack})
                
            else:
                for length in range(self._num_disks):
                    pole = (self._num_disks * ' ') + '|' + (self._num_disks * ' ')
                    print(pole)
                    pole_stack.append(pole)
                tower_stack.update({tower_key: pole_stack})
            print('\n')
                    
    # 3. Moving a disk:
    def move_disk(self, source_tower, dest_tower, disk_stack):
        return

# ----- Manager Function -----
def main():
    '''
    Purpose: Starts the program
    Parameters: No parameters are taken
    Returns: NONE
    '''
    mode = game_display()
    x, y, z, mode = start_game(mode)
    display = display_tower(x, y, z)
    next_steps(mode, display)
    
# ----- Helper function 1 -----
def game_display():
    '''
    Purpose: Displays the starting message that starts the program.
    Parameters: No parameters are taken.
    Returns: Mode -> 1 = Starting new game, OR 2 = Opening & resuming a saved file.
    '''
    # 1. Display Message:
    print('WELCOME TO TOWER OF HANOI GAME!')
    mode = input('\nEnter 1 to start a new game or 2 to resume a saved game: ')
    
    # 2. Error Checking:
    while mode != '1' and mode != '2':
        mode = input('\nEnter 1 to start a new game or 2 to resume a saved game: ')
    return mode

# ----- Helper Function 2 -----
def start_game(mode):
    '''
    Purpose: Prompts the user for game parameters.
    Parameters: Mode is taken as a parameter.
    Returns: Displays the game from user inputs.
    '''
    # 1. Initiating game if Mode = 1:
    if mode == '1':
        print('\nStarting a new game..........')
        num_towers = int(input('Number of towers [min=3,...,max=9]? '))
        num_disks = int(input('Number of disks [min=3,..,max=9]? '))
        target_tower = int(input('Target Tower [min=2,...,max=3]? '))
    
    # 2. Starting saved game if Mode = 2:
    while mode == '2':
        file_name = input('Enter file name (e.g.: game.p): ')
        
        # 2.1. 'Try' clause, opening a saved game:
        try:
            with open(file_name, 'r+') as file:
                contents = file.readlines()
                file.close
                print(file.closed)
        
        # 2.2 'Except' clause, if file not found:
        except FileNotFoundError:
            print('File:', file_name, 'cannot be found: Starting new game..........')
            mode = '1'
            num_towers = int(input('Number of towers [min=3,...,max=9]? '))
            num_disks = int(input('Number of disks [min=3,..,max=9]? '))
            target_tower = int(input('Target Tower [min=2,...,max=3]? '))            
            break
    
    return num_towers, num_disks, target_tower, mode

# ----- Helper Funciton 3 -----
def display_tower(num_towers, num_disks, target_tower):
    '''
    Purpose: Builds the tower from user inputs.
    Parameters: 3 Parameters, # of towers, # of disks, target tower.
    Returns: Displays the towers.
    '''
    # 1. Building blocks of the tower:
    steps = 0
    counter = 0
    disk_stack = []
    pole_stack = []
    tower_stack = {}
    
    # 2. Building the tower with a Tower Class:
    tower = Tower(num_towers, num_disks, target_tower)
    tower.build_tower(counter, disk_stack, pole_stack, tower_stack)
    return tower

# ----- Helper Function 4 -----
def next_steps(mode, tower):
    '''
    Purpose: Asks the user for the next steps in the game.
    Parameters: No parameters are taken
    Returns: NONE
    '''
    # 1. Prompting the user:
    while mode == '1':
        print('\n\t1 - Move a Disk\n\t2 - Save and End\n\t3 - End without Saving\n')
        user_input = input('Enter 1 or 2 or 3: ')
        
    # 2. Error Checking:
        while user_input != '1' and user_input != '2' and user_input != '3':
            print('\n\t1 - Move a Disk\n\t2 - Save and End\n\t3 - End without Saving\n')
            user_input = input('Enter 1 or 2 or 3: ')
            
    # 3. Processing user input:
        if user_input == '1':
            source_tower = int(input('Source Tower? '))
            dest_tower = int(input('Destination Tower? '))
            tower.move_disk(source_tower, dest_tower, disk_stack)
            continue
        #elif user_input == '2':
        elif user_input == '3':
            print('Ending Game..........\nGoodbye!')
            break
