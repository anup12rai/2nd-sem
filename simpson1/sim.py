
a = 0
b = 2
n = 4

h = (b - a) / n

total = 0

for i in range(n + 1):
    x = a + i * h
    y = x**2

    if i == 0 or i == n:
        total = total + y
    elif i % 2 == 0:
        total = total + 2 * y
    else:
        total = total + 4 * y

answer = (h / 3) * total

print("Integration =", answer)
