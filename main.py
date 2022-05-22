import re
import json

# Load in shoppingList.txt
with open('shoppingList.txt') as f:
  uList = f.readlines()

# Parse and tokenize the list
for i in range(len(uList)):
  uList[i] = uList[i].replace("\n", "")
  uList[i] = re.sub("^[\d]*. ", "", uList[i]).lower()

# Create a blank list for sorted items
sList = {}

# Opening JSON file
f = open('grocery.json')
json_data = json.load(f)
f.close()

# Check the list against grocery.json and sort it
for x in json_data:
  for item in json_data[x]:
    if item.lower() in uList:
      try:
        sList[x].append(item)
      except KeyError:
        sList[x] = [item]
  
# TODO: if item not in list, add it to "UNKNOWN" key.

# Save the list to file.
f = open("sortedShoppingList.txt", "w")
for x in sList:
  f.write(x + "\n")
  for item in sList[x]:
    f.write(item + "\n")

  if x != list(sList)[-1]:
    f.write("\n\n")

f.close()
