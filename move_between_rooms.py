"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# Create the gameplay loop required by the milestone.
while current_room != "exit":
    # Display the current room.
    print()
    print("You are in the", current_room)

    # Prompt for a movement command or "exit".
    command = input("Enter a command (go north, go south, go east, go west, or exit): ").lower()

    # Branch for a valid move, exit, or invalid input.
    if command == "exit":
        current_room = "exit"
    elif command.startswith("go "):
        direction = command[3:]

        # Update the room only after a valid movement command.
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You cannot go that way.")
    else:
        print("Invalid command.")

# The gameplay loop ends when the player reaches the exit condition.
print("Thanks for playing!")
