def doXOR(char1, char2):
    for index, binaryValue in enumerate(char1):
        if binaryValue != char2[index]:
            char1[index] = "1"
        elif binaryValue != " ":
            char1[index] = "0"
    char1 = ''.join(char1)
    return char1


def HextToBin(hexaChar):
    hexasplit = list(hexaChar)
    hexa = list("0123456789abcdef")
    hexTrans = "0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111".split(",")
    Dic = dict((value, hexTrans[index])for index, value in enumerate(hexa))

    for hexal, binary in Dic.items():
        for indx, lett in enumerate(hexasplit):
            if lett == hexal:
                hexasplit[indx] = "++" + binary
    hexasplit = ''.join(hexasplit)
    hexasplit = hexasplit.replace("++", "")
    return hexasplit


def dameL(pos, phrase, resL):
    msgs = """
00000000000000000000000000000000000000000000000000000000000000,
29044d472f1c0d4538161405017f0b0301532a1a1f3a4b0109570600061b51,
2e09410f1a1048113a0a551f0d30111c041d0a4f193a05554f3f3a4f19110f,
050404035b0000003244001b452b0b4f111b0b4f00301b4e00117f1b1c155d,
0e050d0b5754290b3b441d0e4532051d061b0b0b542b030b02573b00031e5d,
070b000e155a48243100551c0d3a0a4f111b0b1654280e1c0a572a1f585009,
0e0918470c111a007f110547451e0a0b4504060a1a7f1f060a0e7f18110218,
46080e101558481137010c4b123a160a451701181a734b2f01137f181c1513,
4618090202541f002d0155040b331d4f0d12020959280a174f022f43542415,
031541101e060d4531011c1f0d3a164f10034e011b2d4b0a00003141543f36
""".replace("\n", "").split(",")
    Phrase = msgs[phrase]
    toCollideCharBin = HextToBin(Phrase[pos * 2 - 2:pos * 2])
    lBin = HextToBin(resL.encode("hex"))
    myL = doXOR(list(toCollideCharBin), list(lBin))
    return hex(int(myL, 2))

# Change from 1 to 30 depending of the character you are attmepting to obtain
# Change from 1 to 9 depending of the phrase in wich it is the character
# Change the guess character you are trying to obtain in each position
print(dameL(30, 5, " "))
