def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter the starting number (n): "))

for number in countdown(n):
    print(number)


