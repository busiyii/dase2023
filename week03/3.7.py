def commonfactor(a, b):
    while b:
        a, b = b, a % b
    return a
       
num1 = int(input())
num2 = int(input())

result = commonfactor(num1, num2)
print(result)
