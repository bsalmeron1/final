
# Author: [Your Name]
# Date: [Date]
# Description: This program tracks inventory levels and categorizes items based on stock quantity.

# Initialize an empty list to store inventory items
inventory = []

# Function to add an item to inventory
def add_item(item_name, quantity):
    """
    Adds an item and its quantity to the inventory.

    Parameters:
        item_name (str): Name of the inventory item.
        quantity (int): Quantity of the item.
    
    Returns:
        str: Confirmation message.
    """
    inventory.append({"name": item_name, "quantity": quantity})
    return f"Item added: {item_name} - Quantity: {quantity}"

# Function to check inventory and flag low stock items
def check_inventory(stock_threshold):
    """
    Checks all inventory items and categorizes them as low stock or sufficient stock.

    Parameters:
        stock_threshold (int): The minimum acceptable quantity before an item is considered low stock.
    
    Returns:
        str: Inventory summary with categorized stock levels.
    """
    if not inventory:
        return "Inventory is empty."

    summary = "Inventory Report:\n"
    low_stock_count = 0

    for item in inventory:
        if item["quantity"] < stock_threshold:
            summary += f"- {item['name']} (Low Stock: {item['quantity']})\n"
            low_stock_count += 1
        else:
            summary += f"- {item['name']} (In Stock: {item['quantity']})\n"

    summary += f"Total Low Stock Items: {low_stock_count}"
    return summary

# Main program loop
def main():
    """
    Runs the main program allowing users to add items and check inventory.
    """
    print("Welcome to Inventory Manager!")

    while True:
        print("\nOptions: \n1. Add Item \n2. View Inventory \n3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter item quantity: "))
                print(add_item(item_name, quantity))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            print(check_inventory(5))  # Threshold set to 5 for low stock warning

        elif choice == "3":
            print("Exiting Inventory Manager. Keep your stock updated!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
def check_inventory(stock_threshold):
    """
    Checks all inventory items and categorizes them as low stock or sufficient stock.

    Parameters:
        stock_threshold (int): The minimum acceptable quantity before an item is considered low stock.
    
    Returns:
        str: Inventory summary with categorized stock levels.
    """
    if not inventory:
        return "Inventory is empty."

    summary = "Inventory Report:\n"
    low_stock_count = 0

    for item in inventory:
        if item["quantity"] < stock_threshold:
            summary += f"- {item['name']} (Low Stock: {item['quantity']})\n"
            low_stock_count += 1
        else:
            summary += f"- {item['name']} (In Stock: {item['quantity']})\n"

    summary += f"Total Low Stock Items: {low_stock_count}"
    return summary
for grade in grades_list:
    if grade >= passing_score:
        passing += 1
    else:
        failing += 1