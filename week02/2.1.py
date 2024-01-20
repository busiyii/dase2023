def max_product_integer_partition(n):
    if n <= 1:
        return []

    temp = 0
    result = []
    for j in range(1, n//2 + 1):
        product = j * (n - j)
        if product >= temp:
            temp = product
    for j in range(1, n//2 + 1):
        if j * (n - j) == temp:
            result.append(j)
            result.append(n-j)

    return result

# 测试示例
n = 4
result = max_product_integer_partition(n)
print(result)  
n = 5
result = max_product_integer_partition(n)
print(result)  
