import random as rn


def f(n):
    return sum(1 for i in range(1, n+1) if str(i)[-1] == str(i)[0])


def f2(n):
    s = sum(1 for i in range(min(n, 9)))
    return n // 10 - (str(n)[0] > str(n)[-1]) + s


def debug():
    a = rn.randint(1, 500)
    b = a + rn.randint(1, 5000)
    x, y = (f(b), f(a)), (f2(b), f2(a))
    print(x == y, a, b, x, y)


def main():
    l, r = map(int, input().split())
    print(f2(r) - f2(l) + (l < 10))


# for i in range(1000):
#     debug()
main()
