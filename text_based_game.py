# Name: [Enter your full name]
# Project Two: Cyber Rescue Text-Based Adventure Game


def show_instructions():
    """Display the game objective and available commands."""
    print('Welcome to Cyber Rescue!')
    print('Collect all 6 tools before confronting Shadow in the Server Room.')
    print('Move commands: go north, go south, go east, go west')
    print('Collect an item: get <item name>')
    print('-' * 45)


def show_status(current_room, inventory, rooms):
    """Display the current location, collected items, and nearby item."""
    print(f'\nYou are in the {current_room}')
    print(f'Inventory: {inventory}')
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print('-' * 45)


def main():
    """Run the Cyber Rescue adventure until the player wins or loses."""
    # Rooms are connected by directions. Six rooms contain collectible tools.
    rooms = {
        'Lobby': {'north': 'Server Room', 'west': 'Security Office'},
        'Security Office': {'east': 'Lobby', 'north': 'Workshop',
                            'item': 'Access Card'},
        'Workshop': {'south': 'Security Office', 'north': 'Power Room',
                     'item': 'Repair Kit'},
        'Power Room': {'south': 'Workshop', 'east': 'Network Room',
                       'item': 'Backup Battery'},
        'Network Room': {'west': 'Power Room', 'east': 'Archive',
                         'item': 'Firewall Chip'},
        'Archive': {'west': 'Network Room', 'south': 'Control Room',
                    'item': 'Recovery Drive'},
        'Control Room': {'north': 'Archive', 'item': 'Override Code'},
        'Server Room': {'south': 'Lobby'}  # Shadow waits here.
    }

    current_room = 'Lobby'
    inventory = []
    required_items = 6
    villain_room = 'Server Room'

    show_instructions()

    while True:
        # Reaching Shadow ends the game; all six tools are required to win.
        if current_room == villain_room:
            if len(inventory) == required_items:
                print('\nCongratulations! You collected all 6 tools and defeated Shadow!')
            else:
                print('\nShadow caught you before you collected all the tools. GAME OVER!')
            print('Thanks for playing Cyber Rescue!')
            break

        show_status(current_room, inventory, rooms)
        command = input('Enter your move: ').strip()
        command_lower = command.lower()

        if command_lower.startswith('go '):
            direction = command_lower[3:].strip()
            if direction in rooms[current_room] and direction != 'item':
                current_room = rooms[current_room][direction]
            else:
                print('You cannot go that way. Try another direction.')

        elif command_lower.startswith('get '):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get('item')
            if room_item and requested_item.lower() == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]['item']
                print(f'You collected the {room_item}!')
            else:
                print('That item is not available in this room.')

        else:
            print('Invalid command. Use go <direction> or get <item name>.')


if __name__ == '__main__':
    main()
