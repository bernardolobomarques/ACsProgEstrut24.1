def fat(num):
    if num == 1:
        return 1
    return num * fat(num-1)

num = int(input())
print(fat(num))