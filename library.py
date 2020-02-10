# mac - bak och fram
# big book - ceasar
# thin book - https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso

# space, no commas!
# "sometimes combine all of the three" (probably ceasar first)


#communique
inp = "1: Fgerff, 2: fvyji, 3: etilE, 2: tsmvra, 3: spihC, 3: sekacnaP, 3: sneilA, 1: Uhyx, 3: noitanimreT, 3: dnekeeW, 1: Ybyyvcbc, 3: kcalB, 2: epfiezanb, 2: yhgkszq, 3: gnidduP, 1: Zhava, 3: roxXah, 1: Nezntrqqba, 1: Uhtva, 2: xsmki, 2: evpcmxgc, 3: sllabtaeM, 1: Tbireazrag, 2: ihme, 1: Onpba, 3: yrotcaF, 3: niaP, 2: epfiezanb, 3: niaP, 2: mlvdmvsgwtn, 1: Ybtna, 1: Jrrxraq, 1: Ryvgr, 1: Xvex, 1: Fgerff, 2: fvsdmv, 2: ipgrwag, 2: lwetiazvd, 2: kvqrr, 3: sananaB, 2: abpb, 2: ipgrvl, 3: tnemnrevoG, 2: ahbosz, 2: evpcmxgc, 2: epfiezanb, 3: sneilA, 1: Ryvgr, 1: Ibvq, 1: Ebzna, 2: lwetiazvd, 2: flekfidyg, 3: erutinruF, 2: dpvb, 1: Oynpx, 2: ybvembmes, 3: namtaB, 1: Thaf, 2: ipgrwag, 1: Nonggbve, 3: noitcefnI, 3: yrotcaF, 2: ovmu, 2: ihme, 3: ssertS, 3: nimooM, 2: lavvwa, 3: kriK, 1: Nyvraf, 1: Gbvyrg, 2: ldiih, 2: phv, 3: yenruoJ, 3: sekacnaP, 1: Oynpx, 2: vomgw, 3: nairarbiL, 1: Ibvq, 1: Snpgbel, 1: Ibvq, 3: etilE, 2: kvyxi, 3: pihsecapS, 3: sdiordnA, 2: vomgw, 1: Jne, 1: Cerfvqragvny, 1: Xvex, 2: kvffxa, 1: Zbbzva, 2: kvffxa, 1: Nonggbve, 2: ahbosz, 1: Xvex, 2: ahbosz, 3: niaP, 3: etilE, 1: Gbvyrg, 2: lwetiazvd, 3: sekacnaP, 3: kcalB, 2: dpvb, 1: Onpba, 1: Uhyx, 2: evpcmxgc, 1: Uhtva, 1: Xraary, 3: stoboR, 3: popilloL, 2: vomgw, 2: useto, 2: fvyji, 1: Yvoenevna, 1: Onpba, 1: Gbvyrg, 2: ovmu, 3: nimooM, 2: zvzvvverby"

ceasar_input = []
battista_input = []
mac_input = []

replaced = inp.replace(': ', ':')
separated = replaced.split(' ')

def resolve_ceasar(word):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for char in word:
        place = alphabet.find(char)
        result += alphabet[place + 13]
    return result

def decrypt(ciphertext):
    key = 'thereisnofatebutwhatwemake'
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

def backward(word):
    result = ''.join(list(reversed(word)))
    return result

resulting_thingy = ''

for word in separated:
    if word[0] == '1':
        resulting_thingy += resolve_ceasar(word.lower()[2:].replace(',', '')) + ' '
    elif word[0] == '2':
        resulting_thingy += decrypt(word.lower()[2:].replace(',', '')) + ' '
    else:
        resulting_thingy += backward(word.lower()[2:].replace(',', '')) + ' '

print(resulting_thingy)

