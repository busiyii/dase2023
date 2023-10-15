def decimal_to_binary(decimal_num):
    binary_num = ""
    whole_part = int(decimal_num)
    decimal_part = decimal_num - whole_part

    binary_num += bin(whole_part)[2:] + "."

    while(decimal_part != 0 ):
        decimal_part *= 2
        bit = int(decimal_part)
        binary_num += str(bit)
        decimal_part -= bit

    return binary_num

decimal_num = float(input())  
binary_num = decimal_to_binary(decimal_num)
print(f"{decimal_num} 的二进制表示为: {binary_num}")
