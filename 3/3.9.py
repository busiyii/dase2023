def array_B(A):
    n = len(A)
    left_array = [1] * n
    right_array = [1] * n
    B = [1] * n

    for i in range(1, n):
        left_array[i] = left_array[i - 1] * A[i - 1]

    for i in range(n - 2, -1, -1):
        right_array[i] = right_array[i + 1] * A[i + 1]

    for i in range(n):
        B[i] = left_array[i] * right_array[i]

    return B

input_str = input("")
A = list(map(int, input_str.split()))
B = array_B(A)
print(A)
print(B)
