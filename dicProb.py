# to check for the number of occurrence of each items in a list, here is the way to go.
list = [2, 2, 3, 5, 5, 7, 7, 0, 2, 3, 1, 0, 5]
dic = {}
for x in list:
    if x in dic:
        count = dic[x]
    else:
        count = 0
    dic[x] = count + 1
for key, value in dic.items():
    print(key, value)