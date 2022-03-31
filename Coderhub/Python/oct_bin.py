# تحويل رقم ثماني إلى رقم ثنائي
# oct > hex
# hex > bin


def oct_to_bin(octal):
    vhex = hex(int(str(octal), 8))
    # end_length = len(vhex) * 4
    hex_as_int = int(vhex, 16)
    hex_as_binary = str(bin(hex_as_int))
    # padded_binary = str(hex_as_binary[2:].zfill(end_length))
    #vbin = padded_binary[padded_binary.find('1'):]
    return hex_as_binary[2:]


print(oct_to_bin(1000)) # --> "1000000000"
print(oct_to_bin(234)) # --> "10011100"

