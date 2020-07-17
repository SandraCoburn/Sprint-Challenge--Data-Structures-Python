import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.value is None:
            self.value = value
            print(self.value)
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        #when name is the same 
        if self.value == target:
            #add name to duplicates array
            return duplicates.append(target)
            #go to left side to check for duplicates
        if target < self.value:
            if self.left is None:
                return None
            else:
                return self.left.contains(target)
        else:
            #check right side for duplicates
            if self.right is None:
                return None
            else:
                return self.right.contains(target)
        

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
nl = BSTNode()
#loop throught the first list
for name_1 in names_1:
    #add names to nl from list 1
    nl.insert(name_1)
#loop throught the second list to compare
for name_2 in names_2:
    nl.contains(name_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#cmp(names_1, names_2)