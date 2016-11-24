def rec(n):
    if n<1:
        print('Неверный код')
    else:
        if n == 2 or n == 1:
            return 1
        else:
            return rec(n - 1) + rec(n - 2)


print(rec(int(input())))
