dict = {1:1, 2:2 , 3:3}
print(dict)
if 4 not in dict:
    dict[4] = dict.get(4,0) + 1
    print(dict[4])