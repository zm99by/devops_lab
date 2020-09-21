f = int(input("Input integer"))


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print("#Example: ", fac(f))
