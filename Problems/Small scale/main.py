b = float(input())

while True:
    a = input()

    if a == '.':
        break
    elif b > float(a):
        b = float(a)
print(b)
