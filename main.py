import re
import json

# Load and clean the shopping list from shoppingList.txt
with open('shoppingList.txt') as f:
    uList = [re.sub(r"^\d*. ", "", line.strip()).lower() for line in f]

# Load the grocery aisles data from grocery.json
with open('grocery.json') as f:
    json_data = json.load(f)

# Initialize the sorted list dictionary
sList = {aisle: [] for aisle in json_data}
sList["UNKNOWN"] = []  # Add UNKNOWN aisle for unmatched items

# Sort items from the shopping list into the correct aisles
for item in uList:
    found = False
    for aisle, products in json_data.items():
        if item.upper() in map(str.upper, products):
            sList[aisle].append(item.title())  # Capitalize each word
            found = True
            break
    if not found:
        sList["UNKNOWN"].append(item.title())  # Capitalize each word

# Remove empty aisles and duplicates from the sorted list
sList = {aisle: list(set(items)) for aisle, items in sList.items() if items}

# Save the sorted list to sortedShoppingList.txt
with open("sortedShoppingList.txt", "w") as f:
    for aisle, items in sList.items():
        f.write(aisle + "\n")
        f.write("\n".join(items))
        f.write("\n\n\n")
