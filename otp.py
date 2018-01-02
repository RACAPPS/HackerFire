from xor import doHexAndXOR


def decode_binary_string(s):
    return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))


def collide(l1, l2):
    return decode_binary_string(doHexAndXOR(l1, l2))


leng = 31
msgs = """
666c61677b7468655f64756b655f646f65736e6f745f6b6e6f775f6f74707d,
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
resAscii = []
for indx, hexa in enumerate(msgs):
    for indx2, hexa2 in enumerate(msgs):
        if indx2 > indx:
            if indx == 0:
                # print("Collision between " + str(indx) + " and " + str(indx2) +" returns: " + doHexAndXOR(hexa, hexa2))
                print("------------------------------------\n" + str(indx2) + ". " + (decode_binary_string(doHexAndXOR(hexa, hexa2).replace(" ", "")))[:leng])
                # resAscii.append(list(doHexAndXOR(hexa, hexa2).replace(" ", ""))))


# Nothing to see below
'''for j in range(0, len(resAscii[0]) - 1, 1):
    for i, v in enumerate(resAscii):
        for i2, v2 in enumerate(resAscii):
            if i2 > i:
                if v[j] == v2[j]:
                    print(v[j])
    print("END OF COMPARISIONS OF CHAR " + str(j))
'''
'''
flag = "01010100010010000100010101001110"
flaglen = len(flag)
cipherPhraseLen = 248
for i, v in enumerate(resAscii):
    cipherPhrase = v
    # for j in range(0, cipherPhraseLen - flaglen, 1):
    #cipherPhrase = list(resAscii[0])
    flagy = flag
    for l in range(0, 14 * 8, 1):
        flagy = "0" + flagy
    for k in range(0, cipherPhraseLen - len(flagy), 1):
        if len(flagy) < cipherPhraseLen:
            flagy = flagy + "0"
    print("------------------\n" + decode_binary_string((doXOR(cipherPhrase, list(flagy)))))

'''
'''
collisions = {}
for indx, txt in enumerate(resAscii):
    for indx2, txt2 in enumerate(resAscii):
        tmptxt = list(txt)
        tmptxt2 = list(txt2)
        for indx3, txt3 in enumerate(tmptxt):
            for indx4, txt4 in enumerate(tmptxt2):
                if txt3 == txt4:
                    exist = False
                    collisionindex = str(indx) + str(indx3) + str(indx2) + str(indx4)
                    print(collisionindex)
                    for i in enumerate(collisions):
                        if i == collisionindex:
                            exist = True
                    if exist:
                        collisions[collisionindex] = collisions[collisionindex] + 1
                    else:
                        collisions[collisionindex] = 1
print(collisions)
'''
