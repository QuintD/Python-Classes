b_set = {5, 20, 70, 46, 50}
highestNum = 0
for item in b_set:
    if item > highestNum:
        highestNum = item
print("the item with the highest vale in", b_set, "is", highestNum)