n = int(input())

generator = (i for i in range(n, 0-1, -1))


for i in generator:
    print(i)