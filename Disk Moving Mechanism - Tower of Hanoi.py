# ----- NOTES -----
'''
1. Check and compare towers
2. Check and compare to see if a tower is empty or not
3. Comparing disk sizes.

'''

class Tower:
    
    def __init__(self, game_state):
        self._game_state = game_state
        self._towers = game_state['towers']
        self._disks = game_state['disks']
        self._tgt = game_state['tgt']
        
    def __str__(self):
        return f'{self._towers}, {self._disks}, {self._tgt}'
    
    #def move_disk(self):

# ----- More User Input Processing -----
'''
>>> SECTION USED FOR DISPLAYING
num_towers = int(input('Number of towers? '))
num_disks = int(input('Number of Disks? '))
tgt_tower = int(input('Target Tower? '))

game_state = {'towers': {},
              'disks': num_disks,
              'target': tgt_tower}

counter = 0
for tower in range(1, (num_towers + 1)):
    print(num_disks * '_', tower, num_disks * '_')
    for length in range(num_disks, 0, -1):
        for spaces in range(counter, num_disks, 1):
            print(spaces * ' ', ((length - counter) * '=') + '|' + ((length - counter) * '='))
            counter += 1
            continue
'''
# ----- Disk Moving Mechanism -----

# -> game_state -> towers -> 1st tower -> last item: '  *|*  ' -> .pop() last item and replace with '   |   '
game_state = {# 'towers' -> tower keys and tower values -> (source_tower = tower key) -> source_tower[-1] (using stacks!)
                'towers': {1: ['***|***', ' **|** ', '  *|*  '], 
                           2: ['   |   ', '   |   ', '   |   '], 
                           3: ['   |   ', '   |   ', '   |   ']}, 
                 
                 # 'disks' -> use 'for' loop, 'range', 'len' functions to build tower.
                 'disks': 3, 
                 
                 # another problem >:(
                 'target': 2,
                 
                 # Counter for steps:
                 'steps': 0}
    
game_mode = '1'
while game_mode == '1':
    
    # Let's say we want to move a disk from the first tower to either of the empty towers:
    for key in game_state['towers']:
        for item in game_state['towers'][key]:
            print(item)
        print('')
        
    source_tower = int(input('Source tower? ')) # -> Let's assume that the user wants to move a disk from tower 1.
    empty_tower = ['   |   ', '   |   ', '   |   ']
    while game_state['towers'][source_tower] == empty_tower:
        source_tower = int(input('Source tower? '))
    
    dest_tower = int(input('Destination tower? ')) # -> Let's assume that the user wants to move a disk either tower 2 or 3.  
    print('')
    
    '''
    >>> SECTION USED FOR TESTING
    print(game_state['towers'][source_tower])
    for item in game_state['towers'][source_tower]:
        #print(item)
    '''
    
    # moved_disk saves the disk as a variable where it can be transferred later:
    moved_disk = game_state['towers'][source_tower][-1] # -> possible loop/calculation here to determine whether an element at index 'i' is either a pole OR a disk (ANOTHER PROBLEM...)
    game_state['towers'][source_tower].pop() # -> possible loop/calculation here to determine at what point to remove an element...
    game_state['towers'][source_tower].append('   |   ') # -> possible loop/calculation here to determine the number of spaces at the end of each pole...
    new_tower = game_state['towers'][source_tower]
    game_state['towers'].update({source_tower: new_tower})
    
    '''
    >>> SECTION USED FOR TESTING
    print(game_state['towers'][source_tower])
    for item in game_state['towers'][source_tower]:
        #print(item)
    '''
    game_state['towers'][dest_tower].pop()
    game_state['towers'][dest_tower].insert(0, moved_disk) # -> possible loop/calculation here to determine the index position to take place...
    
    '''
    >>> SECTION USED FOR TESTING
    print(game_state['towers'][dest_tower])
    for item in game_state['towers'][dest_tower]:
        #print(item)
    '''
    # Now this just displays the towers 
    #for key in game_state['towers']:
        #for item in game_state['towers'][key]:
            #print(item)
        #print('')

# ----- Processing Continues -----