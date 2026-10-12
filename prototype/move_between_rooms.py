"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the Museum Mystery text game.
rooms = {
    'Museum Entrance': {'north': 'Art Studio', 'east': 'Security Office'},
    'Art Studio': {'south': 'Museum Entrance', 'north': 'Paris Gallery', 'east': 'Mona Lisa Gallery'},
    'Security Office': {'west': 'Museum Entrance', 'north': 'Mona Lisa Gallery'},
    'Paris Gallery': {'south': 'Art Studio', 'east': 'Fashion Gallery'},
    'Fashion Gallery': {'west': 'Paris Gallery', 'east': 'Golden Exhibit Hall'},
    'Golden Exhibit Hall': {'west': 'Fashion Gallery'},
    'Mona Lisa Gallery': {'west': 'Art Studio', 'east': 'Paris Souvenir Room', 'south': 'Security Office'},
    'Paris Souvenir Room': {'west': 'Mona Lisa Gallery'}
}

# Set the starting room.
current_room = 'Museum Entrance'

# Run the game until the player exits.
while current_room != 'exit':
    print('\nYou are in the', current_room)

    command = input(
        'Enter a direction (north, south, east, west) or exit: '
    ).lower().strip()

    if command == 'exit':
        current_room = 'exit'
        print('Thank you for playing Museum Mystery!')

    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
        print('You moved to the', current_room)

    else:
        print('Invalid command. Please try another direction.')
# TODO: Run and debug all milestone cases in prototype/README.md.
