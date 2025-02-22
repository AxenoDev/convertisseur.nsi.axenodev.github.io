def hex2bin(nb_hex):
    nb_int = int(nb_hex, 16)
    nb_bin = ""
    while nb_int > 0:
        nb_bin = str(nb_int % 2) + nb_bin
        nb_int = nb_int // 2
    return nb_bin