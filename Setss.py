a_set = {45, True, "burger", 34.90}
# for item in a_set:
#     print(item)

# to check if an item exist in a set

# print("burger" in a_set)
# if 465 in a_set:
#     print(465, "can be found in", a_set)
# else:
#     print(465, "cannot be found in", a_set)

# to add an element in a set
a_set.add("milk")
# print(a_set)

# to remmove items from a set you use discard() or remove() your best bet is to use .discard() unless you are very sure that the element in question is really in the set.
# a_set.discard(300)
# a_set.discard('milk')
# print(a_set)

#******* using the .pop() method
print(a_set)
# a_set.pop()
# print(a_set)

# ****this strategy shows you which item was poped out
# fim = a_set.pop()
# print(a_set, fim)

# **** this clears out all the elements of the set.
a_set.clear()
print(a_set)