# Fetching items in a tuple
data = ("red", "green", "blue", "yellow", "brown", "yellow", "pink")
# print(data)
# print(type(data))
# print(data[-3])
# print(data[2:4])
# print(data[2:-2])
# this syntax below is long and not the best as it cant be used when the items are much.

# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])
# print(data[5])
# print(data[6])
# for item in data:
#     print(item)
#     print(data.index(item))
# the method above does not give us the corresponding index position, it rather repeats it for repeated values. Hence the alternative below.
# for x in range(len(data)):
#     print(x)
#     print(data[x])
# to append to a tupple, we use the list constructor to convert the tuple to a list, do the adding or removing and reconvert to tuple using the tuple constructor

# a_list = list(data)
# # to append or add to the list if you use insert, then you will specify the index position
# a_list.append("indigo")
# a_list.insert(3, "violet")
# # to remove from the list, we use pop.
# a_list.pop(4)
# # to convert the modified list back to a tuple we use the tuple constructor
# data = tuple(a_list)
# print(a_list)
# print(data)

# if "white" in data:
#     print("White is in our tuple")
# elif "red" in data:
#     print("Red is in our tuple")

# TUPLE EXERCISE***************
a_tuple = (10, 20, 30, 40, 50)
sumt = 0
for item in a_tuple:
    sumt = sumt + item
    print("the present sum of the values in the tuple is", sumt)

print(" the final sum of the tuple is ", sumt)
print(a_tuple)