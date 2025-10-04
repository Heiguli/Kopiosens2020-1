import codecs

def encode(s):
    MAXSIZE = 200000
    if not isinstance(s,str):
        raise TypeError
    #origlen = len(s)
    #crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > MAXSIZE:
        raise ValueError
    paddeds = s.ljust(MAXSIZE, "0")
    result_chars = []  
    for c in paddeds:
        if c.isalpha() and c.isascii():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            result_chars.append(codecs.encode(c,'rot13'))
        elif c in digitmapping:
            result_chars.append(digitmapping[c])
        elif c == " ":  # allow padding spaces
            result_chars.append(c)
        else:
            raise ValueError
    full_encoded = ''.join(result_chars)
    return full_encoded[:len(s)]

def decode(s):
    #origlen = len(s)
    MAXSIZE = 5
    decoded = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    for c in s:
        if c.isalpha():
            c = c.lower()
            decoded += codecs.decode(c, 'rot13')
        elif c in digitmapping:
            decoded+=digitmapping[c]
        else:
            decoded += c
    return decoded

