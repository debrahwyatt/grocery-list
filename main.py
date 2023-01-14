import re
import json

# Load in shoppingList.txt
with open('shoppingList.txt') as f:
  uList = f.readlines()

# Parse and tokenize the list
for i in range(len(uList)):
  uList[i] = re.sub("^[\d]*. ", "", uList[i].replace("\n", "")).lower()

# Opening JSON file
f = open('grocery.json')
json_data = json.load(f)
f.close()

# Create a blank list for sorted items
sList = {}
for aisle in json_data:
  sList[aisle] = []

# Check the list against grocery.json and sort it
for item in uList:
  found = False
  for aisle in json_data:
    if item.upper() in map(str.upper, json_data[aisle]):
      found = True
      try:
        sList[aisle].append(item)
      except KeyError:
        sList[aisle] = [item]
  if not found:
    try:
      sList["UNKNOWN"].append(item)
    except KeyError:
      sList["UNKNOWN"] = [item]

#Sort the dictionary by aisle order
temp = {}
for aisle in sList:
  if sList[aisle] != []:
      temp[aisle] = sList[aisle]
sList = temp
del temp

#TODO: Remove Duplicates
        
# Save the list to file.
f = open("sortedShoppingList.txt", "w")
for x in sList:
  f.write(x + "\n")
  for item in sList[x]:
    f.write(item + "\n")
  if x != list(sList)[-1]:
    f.write("\n\n")
f.close()
