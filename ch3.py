def collatz(num):
    if num % 2 == 0:
        num = num // 2
        print(num)
        return num
    else:
        num = 3 * num + 1
        print(num)
        return num
print("Insert an Integer ")
try:
    integer = int(input())
    while integer != 1:
        integer = collatz(integer)
except ValueError:
        print("This is not a number")