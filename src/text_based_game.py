

"""Project Two: Museum Mystery
Full Name: Dalia Garcia
"""


def show_instructions():
    """Display the game objective and available commands."""
    print("\nWelcome to Museum Mystery!")
    print("Explore the museum and collect all 6 hidden items.")
    print("Collect all items before entering the Mona Lisa Gallery.")
    print("The Mona Lisa is the villain. Entering her gallery")
    print("without all 6 items will end the game.")
    print("\nMovement commands:")
    print("go north, go south, go east, go west")
    print("Collect an item using: get item name")
    print("Example: get Key")
    print("\nGood luck!")


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and item."""
    print("\n" + "-" * 35)
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

    print("-" * 35)


def main():
    """Run the Museum Mystery gameplay loop."""

    # Dictionary connecting rooms and their items.
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
        "Paris Souvenir Room": {
            "west": "Mona Lisa Gallery",
            "east": "Golden Exhibit Hall",
            "item": "Mini Eiffel Tower"
        },
        "Mona Lisa Gallery": {
            "west": "Art Studio",
            "east": "Paris Souvenir Room",
            "south": "Security Office"
        }
    }

    # Set the starting room and empty inventory.
    current_room = "Museum Entrance"
    inventory = []

    # List of items required to win the game.
    winning_items = [
        "Paintbrush",
        "Key",
        "Museum Map",
        "Shawl",
        "Golden Frame",
        "Mini Eiffel Tower"
    ]

    # Display game instructions.
    show_instructions()

    # Continue playing until the player wins or loses.
    while True:

        # Display the current room and inventory.
        show_status(current_room, inventory, rooms)

        # Check whether the player entered the villain's room.
        if current_room == "Mona Lisa Gallery":
            if all(item in inventory for item in winning_items):
                print("\nCongratulations! You have collected all")
                print("items and defeated the Mona Lisa!")
                print("YOU WIN!")
            else:
                print("\nOh no! You entered the Mona Lisa Gallery")
                print("before collecting all 6 items.")
                print("GAME OVER!")

            print("Thanks for playing Museum Mystery!")
            break

        # Ask the player for their next command.
        command = input("Enter your move: ").strip()

        # Handle the quit command.
        if command.lower() == "quit":
            print("Thanks for playing Museum Mystery!")
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
                print("You collected the", collected_item + "!")
            else:
                print("Invalid item. That item is not available here.")

        # Handle invalid commands.
        else:
            print("Invalid command.")
            print("Use 'go north' or 'get Key', for example.")


# Start the game.
if __name__ == "__main__":
    main()
