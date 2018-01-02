def doXOR(phrase, phhkey):
    for index, binaryValue in enumerate(phrase):
        if binaryValue != phhkey[index]:
            phrase[index] = "1"
        elif binaryValue != " ":
            phrase[index] = "0"
    phrase = ''.join(phrase)
    return phrase


def doHexAndXOR(msg, key):
    msgsplit = list(msg)
    keysplit = list(key)
    hexa = list("0123456789abcdef")
    hexTrans = "0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111".split(",")
    Dic = dict((value, hexTrans[index])for index, value in enumerate(hexa))

    for hexal, binary in Dic.items():
        for indx, lett in enumerate(msgsplit):
            if lett == hexal:
                msgsplit[indx] = "++" + binary
        for indx, lett in enumerate(keysplit):
            if lett == hexal:
                keysplit[indx] = "++" + binary
    msgsplit = ''.join(msgsplit)
    msgsplit = msgsplit.replace("++", " ")
    keysplit = ''.join(keysplit)
    keysplit = keysplit.replace("++", " ")
    # print(msgsplit)
    # print(keysplit)

    phrase = list(msgsplit)
    phhkey = list(keysplit)

    phrase = doXOR(phrase, phhkey)
    return phrase

# msg = "1f20ec615facefaeff58204690ac56cf9cab8657b1b96306f91ca647b296f3"
# key = "794c8d06249f97cd932d532fe6c522b6c39ff208d8cd56599f75c874c1e28e"
# print(doHexAndXOR(msg, key))
