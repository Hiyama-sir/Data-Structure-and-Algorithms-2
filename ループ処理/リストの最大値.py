my_list = [1,3,2,5,4,9]

max_val = my_list[0]
for val in my_list:
    if max_val < val:
        max_val = val
    else:
        pass
print("最大値:",max_val)