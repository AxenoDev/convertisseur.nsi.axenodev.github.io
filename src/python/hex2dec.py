def hex2dec(nb_hex):
    res = 0
    for i in range(len(nb_hex)):
        if nb_hex[i] == "A":
            i_str = 10
        elif nb_hex[i] == "B":
            i_str = 11
        elif nb_hex[i] == "C":
            i_str = 12
        elif nb_hex[i] == "D":
            i_str = 13
        elif nb_hex[i] == "E":
            i_str = 14
        elif nb_hex[i] == "F":
            i_str = 15
        else:
            i_str = int(nb_hex[i])

        res += i_str * 16 ** (len(nb_hex) - i - 1)

    return res