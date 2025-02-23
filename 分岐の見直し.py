x = 2025
if x % 4 != 0:
    print("平年です")
elif x % 100 != 0:
    print("閏年です")
elif x % 400 != 0:
    print("平年です")
else:
    print("閏年です")