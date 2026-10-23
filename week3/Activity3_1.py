#Buggy Snippet A: Infinite Loop
print("-----------Buggy Snippet A: Infinite Loop----------")
counter = 0
while counter < 5:
    print(counter)
    counter += 1 #Create counter increment
print("")

# Buggy Snippet B: Incorrect Range
print("-----------Buggy Snippet B: Incorrect Range----------")
for i in range(1, 6): # Goal: print 1, 2, 3, 4, 5
    print(i,end="")
    if (i == 5):
        break
    print(",",end=" ")
print("")

# Buggy Snippet C: Misplaced Break
print("")
print("-----------Buggy Snippet C: Misplaced Break----------")
for char in "hello":
    print(char) # This will print 'h', 'e', 'l' then break
    if char == 'l':
        print("Found 'l', stopping!")
        break