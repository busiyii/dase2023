L = [1, 2, 3, 4, 5]
list1= []
list2 = []

for item in L:
    list1.insert(0, item)

index = 0
while index <= len(L) - 1:
    list2.insert(0, L[index])
    index += 1

print(list1)
print(list2)