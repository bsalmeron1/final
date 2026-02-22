# Jacqueline Sandwichhis, Breanna Tepetongo, Adrian Marqetequigluesias

# Dictionaries store menu items and prices
drinks = {
    "boba": 3,
    "breanna pee": 3,
    "jackie diarrhea": 3
}

pastries = {
    "fish tentacle": 5,
    "pompri placenta": 5,
    "konguru pickled ramble": 5
}

artists = ["mr Q", "King V", "Chief K", "MLK"]

total = 0


# Student-developed procedure with parameter
def order_items(menu, item_type):
    global total
    
    print(f"\nHere are the available {item_type}:")
    print(menu)
    
    while True:  # ITERATION
        choice = input(f"Choose a {item_type} (or type 'done' to finish): ")
        
        if choice == "done":  # SELECTION
            break
        
        elif choice in menu:  # SELECTION
            price = menu[choice]
            total += price
            print(f"{choice} added! That costs ${price}.")
        
        else:
            print("That item is not on the menu. Please choose again.")


# Main Program

name = input("What's your name?: ")
print(f"\nWelcome {name}-chan to the Cat Cafe! ^-^")

# Ordering drinks
want_drink = input("Would you like a drink? (yes/no): ")
if want_drink.lower() == "yes":
    order_items(drinks, "drink")

# Ordering pastries
want_pastry = input("Would you like a pastry? (yes/no): ")
if want_pastry.lower() == "yes":
    order_items(pastries, "pastry")

# Listening to music
listen = input("Would you like to listen to music? (yes/no): ")
if listen.lower() == "yes":
    print("Available artists:", artists)
    artist_choice = input("Choose an artist: ")
    
    if artist_choice in artists:
        print(f"Now playing {artist_choice}!")
    else:
        print("That artist is not available.")

# Receipt
receipt = input("\nWould you like your receipt? (yes/no): ")
if receipt.lower() == "yes":
    print("\n--- RECEIPT ---")
    print(f"Customer: {name}")
    print(f"Total Spent: ${total}")
    print("Thank you for visiting the Cat Cafe! ^-^")