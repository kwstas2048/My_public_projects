import random

print("a(n) = k * a(n-1) + l")
# k = int(input("k="))
# l = int(input("l="))
# n = int(input("n="))
# a = int(input("a[0]="))
k = 0
while abs(k) < 2:
    k = random.randrange(-4, 4)
# print("k=", k)
l = random.randrange(-6, 6)
while l == 0:
    l = random.randrange(-2, 2)
# print("l=", l)
a = random.randrange(3)
print("a[0]=", a)
a = k * a + l
print("a[1]=", a)
# print("a[n] =", k, "* a[n-1] +", l)
i = 2
while i < 4:
    a = k * a
    a += l
    guess = int(input("Guess the next term:"))
    if guess == a:
        break
    else:
        print('a[{0}]={1}'.format(i, a))
        i += 1

if guess == a:
    print("Congratulation your guess is right")
    print("a[n] =", k, "* a[n-1] +", l)
else:
    print("Game Over")
    print("a[n] =", k, "* a[n-1] +", l)