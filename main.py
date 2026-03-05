import json

# --- Task 1: Read the inventory ---
# File ko read mode ('r') mein open karke data load karna
# Shuruat mein file mein kitni books hain wo print karna (Output: 2)
# --- Task 2: Update and save ---
# Nayi book ki dictionary
# List mein nayi book add karna
# Updated list ko wapas file mein save karna (indent=4 ke saath)
# --- Task 3: Display the inventory ---
# Assignment ke mutabik file ko DOBARA read karna
# Har book ki details format ke saath print karna

 #--- Task 1: Read the inventory ---
with open('inventory.json', 'r') as file:
    inventory = json.load(file)

print(f"Total number of books currently in the file: {len(inventory)}")
print("-" * 30)

# --- Task 2: Update and save ---
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}

inventory.append(new_book)

# Updated list 
with open('inventory.json', 'w') as file:
    json.dump(inventory, file, indent=4)

# --- Task 3: Display the inventory ---
with open('inventory.json', 'r') as file:
    updated_inventory = json.load(file)

# Har book ki details format ke saath print karna
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")