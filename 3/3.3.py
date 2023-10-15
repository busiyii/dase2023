import re

def is_valid_id_number(id_number):
    pattern = r"^\d{15}$|^\d{17}([0-9]|x)$"
    return bool(re.match(pattern, id_number))

id_number = input()  

print(is_valid_id_number(id_number))  
