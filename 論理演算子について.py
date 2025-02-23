x = 2025
if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
    print("閏年です")
else:
    print("平年です")