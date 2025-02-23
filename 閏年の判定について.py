#西暦
x = 2025
#うるう年かの判定
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("閏年です")
        else:
            print("平年です")
    else:
        print("閏年です")
else:
    print("平年です")