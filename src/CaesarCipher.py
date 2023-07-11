def caesarCipher(s, k):
    result = ""
    for c in s:
        if c.isalpha():
            n = ord(c) + k
            if n > 122 and c.islower():
                n = (n - 97) % 26 + 97
            elif n > 90 and c.isupper():
                n = (n - 65) % 26 + 65
            result += chr(n)
        else:
            result += c
    return result


print(caesarCipher('abcdefghijklmnopqrstuvwxyz', 3))
