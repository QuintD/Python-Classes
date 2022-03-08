
# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1
# print('loop has ended')

# counter = 8
# while counter % 2 == 0:
#     print(counter)
#     counter /= 2
# print('loop has ended')

counter = 8
while counter > 0:
    if counter == 4:
        counter -= 1
        # break
        continue
    print(counter)
    counter -= 1
print('loop has ended')