n = int(input("input integer"))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
