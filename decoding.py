import binascii

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    if n < 65:
        n += 65

    if ((n > 90 and n < 97) or (n > 122)):
        n -= 15

    return int2bytes(n).decode()
