def bin2hex(nb_hex):
    while len(nb_hex) % 4 != 0:
        nb_hex = "0" + nb_hex

    hex_str = ""
    for i in range(0, len(nb_hex), 4):
        four_bits = nb_hex[i:i+4]
        hex_digit = hex(int(four_bits, 2))[2:]
        hex_str += hex_digit

    return hex_str