# c =  yellow = clock, outputs 1, 0
# d = blue = data,
# q = green = output

# code = SN74LVC1G8O

clock = "000101001001010101010010010010010101010010010100100100100100101001001001001010010101001010101010010101001001001010010010100101001010101010010100101010010010100101010010010010101001001010100101001001010010100100100100100100100101001001010010100100101001001010010100100101010010010010010010100100101010010010101001010010100100101001010010010101010100100101010100101001010010010101010100101001001010100101010101001010010010101010101001001010010101010100100100101001001001001001010010010101010010101010101001"
data =  "011010101010100011100001001000010001010010011111101000000110110101110110011111100101110011011000110010001111011010100010000010110111110111111100010011110000010010110000000111000100001001011101111010110101010101101000000111010111100000111101111110011011110001010101101010111111100111100000000110011101011111111011100101000100001111110100100110010010001110110011000000000100001110110111011111100000001010101110000011100000110010101000101100111000101001110001000001100000011111001110000011001110111010010000"

#clock = "00010100"
#data =  "01101110"

output = ""
memory = '0'

for i in range(len(clock)):
    if clock[i - 1] == '0' and clock[i] == '1':
        memory = data[i]
    output += memory
    #print(clock[i], data[i], memory, output)

print((len(output)))
print(output)
