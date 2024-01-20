w = float(input())
x = float(input())
y = float(input())
z = float(input())

numbers = [w, x, y, z]

numbers.sort(reverse=True)

for number in numbers:
    print(number)