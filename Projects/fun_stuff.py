import time

# Game State
player = {
    "location": "Entrance",
    "inventory": [],
    "alive": True
}

# The Map: Each room has a description, exits, and optional items
rooms = {
    "Entrance": {
        "desc": "You are at the Spooky Cave entrance. A cold breeze blows from the North.",
        "north": "Main Hall",
        "item": "torch"
    },
    "Main Hall": {
        "desc": "A vast hall with glowing mushrooms. Paths lead North, East, and West.",
        "south": "Entrance",
        "north": "Treasure Room",
        "east": "Spider Nest",
        "west": "Old Library"
    },
    "Old Library": {
        "desc": "Dusty shelves line the walls. There's a key on a desk. Path leads East.",
        "east": "Main Hall",
        "item": "key"
    },
    "Spider Nest": {
        "desc": "Sticky webs are everywhere! You hear clicking sounds. Path leads West.",
        "west": "Main Hall"
    },
    "Treasure Room": {
        "desc": "A massive golden door stands before you. It looks locked.",
        "south": "Main Hall"
    }
}

def play():
    print("--- WELCOME TO THE EXPANDED SPOOKY CAVE ---")
    
    while player["alive"]:
        loc = player["location"]
        room = rooms[loc]
        
        print(f"\nLocation: {loc}")
        print(room["desc"])

        # Check for items in the room
        if "item" in room:
            item_name = room["item"]
            pick_up = input(f"You see a {item_name}. Take it? (yes/no): ").lower()
            if pick_up == "yes":
                player["inventory"].append(item_name)
                print(f"You picked up the {item_name}!")
                del room["item"] # Remove item from room after picking up

        # Get player move
        move = input("\nWhere do you want to go? (north): ").lower()
        
        if move == "quit":
            print("Thanks for playing!")
            break

        # Room logic and movement
        if move in room:
            new_loc = room[move]
            
            # Special Event: Spider Nest
            if new_loc == "Spider Nest":
                if "torch" not in player["inventory"]:
                    print("\nIt's too dark and the spiders attack! GAME OVER.")
                    player["alive"] = False
                else:
                    print("\nYou use your torch to keep the spiders away!")
                    player["location"] = new_loc
            
            # Special Event: Treasure Room
            elif new_loc == "Treasure Room":
                if "key" in player["inventory"]:
                    print("\nYou use the key to open the door! YOU WIN!")
                    break
                else:
                    print("\nThe door is locked. You need a key.")
            
            else:
                player["location"] = new_loc
        else:
            print("You can't go that way!")

if __name__ == "__main__":
    play()