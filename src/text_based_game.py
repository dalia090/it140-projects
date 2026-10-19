
"""Project Two: Museum Mystery
Full Name: Dalia Garcia
"""


def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to Museum Mystery!")
    print("Collect all 6 items to win the game.")
    print("Do not enter the Mona Lisa Gallery until you have all items")
    print("collected all the items, or you will lose!")
    print("Move commands: go north, go south, go east, go west")
    print("Collect items by typing: get item name")
    print("Type quit to exit the game.")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see the", rooms[current_room]["item"])


def main():
    """Run the main gameplay loop."""

    # Room dictionary with items and connections.
    rooms = {
        "Museum Entrance": {
            "north": "Art Studio",
            "east": "Security Office"
        },
        "Art Studio": {
            "south": "Museum Entrance",
            "north": "Paris Gallery",
            "east": "Mona Lisa Gallery",
            "item": "Paintbrush"
        },
        "Security Office": {
            "west": "Museum Entrance",
            "north": "Mona Lisa Gallery",
            "item": "Key"
        },
        "Paris Gallery": {
            "south": "Art Studio",
            "east": "Fashion Gallery",
            "item": "Museum Map"
        },
        "Fashion Gallery": {
            "west": "Paris Gallery",
            "east": "Golden Exhibit Hall",
            "item": "Shawl"
        },
        "Golden Exhibit Hall": {
            "west": "Fashion Gallery",
            "east": "Paris Souvenir Room",
            "item": "Golden Frame"
        },
        "Mona Lisa Gallery": {
            "west": "Art Studio",
            "east": "Paris Souvenir Room",
            "south": "Security Office"
        },
        "Paris Souvenir Room": {
            "west": "Mona Lisa Gallery",
            "east": "Golden Exhibit Hall",
            "item": "Mini Eiffel Tower"
        }
    }

    # Set the starting room.
    current_room = "Museum Entrance"

    # Create an empty inventory.
    inventory = []

    # Items required to win.
    winning_items = [
        "Paintbrush",
        "Key",
        "Museum Map",
        "Shawl",
        "Golden Frame",
        "Mini Eiffel Tower"
    ]

    # Display instructions.
    show_instructions()
    """Display the game objective and available commands."""
    print("Welcome to Museum Mystery!")
    print("You are exploring a museum to collect six hidden items.")
    print("Your goal is to collect all six items before facing the Mona Lisa.")
    print("Be careful! If you enter the Mona Lisa Gallery before")
    print("collecting all six items, you will lose the game.")
    print()
    print("Movement commands:")
    print("Type 'go north', 'go south', 'go east', or 'go west'.")
    print("To collect an item, type 'get' followed by the item name.")
    print("Example: get Key")
    print("Type 'quit' at any time to exit the game.")
    print()
    print("Good luck, and enjoy Museum Mystery!")



    # Main gameplay loop.
    while True:
        show_status(current_room, inventory, rooms)

        # Check whether the player entered the villain's room.
        if current_room == "Mona Lisa Gallery":
            if all(item in inventory for item in winning_items):
                print("Congratulations! You collected all 6 items!")
                print("You defeated the Mona Lisa!")
                print("YOU WIN!")
            else:
                print("Oh no! You entered the Mona Lisa Gallery")
                print("before collecting all 6 items.")
                print("GAME OVER!")
            break

        # Ask the player for a command.
        command = input("\nEnter your move: ").strip()

        # Allow the player to quit.
        if command.lower() == "quit":
            print("Thank you for playing Museum Mystery!")
            break

        # Handle movement commands.
        elif command.lower().startswith("go "):
            direction = command[3:].strip().lower()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("Invalid direction. Please try again.")

        # Handle item collection commands.
        elif command.lower().startswith("get "):
            item_name = command[4:].strip().strip("'\"")

            if (
                "item" in rooms[current_room]
                and rooms[current_room]["item"].lower()
                == item_name.lower()
            ):
                collected_item = rooms[current_room].pop("item")
                inventory.append(collected_item)
                print(collected_item, "collected!")
            else:
                print("That item is not available in this room.")

        # Handle invalid commands.
        else:
            print("Invalid command. Try 'go north' or 'get Key'.")


if __name__ == "__main__":
    main()
