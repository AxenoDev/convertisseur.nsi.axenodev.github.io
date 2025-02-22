def dec2hex(number):
    if number == 0:
        return "0"
    hex_str = ""
    q = 16
    while number > 0:
        r = number % q
        number = number // q
        if r == 10:
            r = "A"
        elif r == 11:
            r = "B"
        elif r == 12:
            r = "C"
        elif r == 13:
            r = "D"
        elif r == 14:
            r = "E"
        elif r == 15:
            r = "F"
        hex_str = str(r) + hex_str
    return hex_str
