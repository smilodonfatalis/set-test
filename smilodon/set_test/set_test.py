# Compares two sets and returns items missing from each set

from functions import *

# import files
while(True):
    try:
        group1 = input("Enter first filename: ")
        file1 = importFile(group1, 'rt', 'windows-1250')
        break
    except Exception:
        print("Couldn't read file.")

while(True):
    try:
        group2 = input("Enter second filename: ")
        file2 = importFile(group2, 'rt', 'windows-1250')
        break
    except Exception:
        print("Couldn't read file.")

key = input("Please enter column name to compare: ")

# create sets
try:
    set1 = set()
    for entry in file1:
        set1.add(entry[key])
except KeyError:
    print("Key does not exist in {0}".format(group1))
    exit(1)

try:
    set2 = set()
    for entry in file2:
        set2.add(entry[key])
except KeyError:
    print("Key does not exist in {0}".format(group2))
    exit(1)

# print set lengths
print('Total Unique Items in Group 1: {items}'.format(items=len(set1)))
print('Total Unique Items in Group 2: {items}'.format(items=len(set2)))

# find items distinct to each set
set1_distinct = []
for entry in set1:
    if entry not in set2:
        set1_distinct.append(entry)

set2_distinct = []
for entry in set2:
    if entry not in set1:
        set2_distinct.append(entry)

# print items distinct to each set
print("Total Distinct Items in Group 1: {items}".format(items=len(set1_distinct)))
print(set1_distinct)
print("Total Distinct Items in Group 2: {items}".format(items=len(set2_distinct)))
print(set2_distinct)

# save items distinct to each set to file
try:
    exportFileList(set1_distinct, "group1_distinct.csv", "w")
except Exception:
    print("File export failed for {0} distinct elements".format(group1))

print("Successfully saved {0} distinct elements as group1_distinct.csv".format(group1))

try:
    exportFileList(set2_distinct, "group2_distinct.csv", "w")
except Exception:
    print("File export failed for {0} distinct elements".format(group2))

print("Successfully saved {0} distinct elements as group2_distinct.csv".format(group2))