# my_food_item_list = ["Garri", "Peak milk", "Bournvita", "Cornflakes", "Biscuit", "Peak milk", "Milo", "Groundnut"]
# first_item = my_food_item_list[0]
# second_item = my_food_item_list[1]
# fifth_item = my_food_item_list[4]
# print(first_item)
# print(second_item)
# print(fifth_item)
# # for negative indexing
# item = my_food_item_list[-3]
# print(item)
# # range of list
# list_of_items = my_food_item_list[3:5]
# print(list_of_items)
# list_of_items = my_food_item_list[:5]
# print(list_of_items)
# list_of_items = my_food_item_list[:]
# print(list_of_items)
# list_of_items = my_food_item_list[-4:-2]
# print(list_of_items)
# # how to change an item value
# my_food_item_list[2] = "Milo"
# print(my_food_item_list)
# # to print the elements one after the other
# for i in range(len(my_food_item_list)):
#     print(my_food_item_list[i])
# # a shortcut for looping through a list
# for item in my_food_item_list:
#     print(item)
# list exercise to find maximum number in a non empty list.
# number_list = [5, 7, 12, 90, -5, 10]
# maxNum = number_list[0]
# for number in number_list:
#     if number > maxNum:
#         maxNum = number
# print(maxNum)

# to check the maximum number in the list if it is 2 times more that everyother number in the list, and print the index if true
number_list = [3, 6, 1, 0, 9, 27]
maxNum = number_list[0]
maxNum_Index = 0
counter = 0
for i in range(len(number_list)):
    if number_list[i] > maxNum:
        maxNum = number_list[i]
        maxNum_Index = i
for number in number_list:
    if maxNum == number:
        continue
    if maxNum >= 2 * number:
        counter += 1
if counter == len(number_list) -1:
    print(maxNum_Index)
else:
    print(-1)
