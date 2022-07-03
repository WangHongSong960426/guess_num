import random
start = input('請決定隨機數字的開始值: ')
end = input('請決定隨機數字的結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1
    n = input('猜猜數字: ')
    n = int(n)
    if r == n:
        print('這是你猜的第', count, '次')
        print('答案就是 ', n, '!')
        print('終於猜對了! ')
        break
    else:
        if r > n:
            print ('你打的數比答案來的小!')
        else:
            print ('你打得數比答案來的大!')
    print('這次你猜的第', count, '次')