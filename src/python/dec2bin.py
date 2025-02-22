def dec2bin(number):
    if number == 0:
        return "0"
    binary_str = ""
    while number > 0:
        binary_str = str(number % 2) + binary_str
        number = number // 2
    return binary_str