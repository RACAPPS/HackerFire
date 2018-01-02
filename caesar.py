chars = list("abcdefghijklmnopqrstuvwxyz")
chars2 = chars + chars
flag = "uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}"

for j in range(1, 26, 1):
    mine = list(flag)
    Dic = dict((value, chars2[index + j])for index, value in enumerate(chars))
    for char, rep in Dic.items():
        for indx, lett in enumerate(mine):
            if char == lett:
                mine[indx] = "++" + rep
    mine = ''.join(mine)
    mine = mine.replace("++", "")
    print(mine)
