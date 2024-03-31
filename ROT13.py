def rot13(message):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' ,'p', 'q', 'r' ,'s', 't', 'u', 'v', 'w' , 'x', 'y', 'z']
    alph_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O' ,'P', 'Q', 'R' ,'S', 'T', 'U', 'V', 'W' , 'X', 'Y', 'Z']
    new_message = ""
    for i in message:
        if i in alph or i in alph_2:
            if i.isupper():
                j = alph_2.index(i)
                if j + 13 > 25:
                    new_message += alph_2[j-13]
                else:
                    new_message += alph_2[j+13]
            else:
                j = alph.index(i)
                if j + 13 > 25:
                    new_message += alph[j-13]
                else:
                    new_message += alph[j+13]
        else:
            new_message += i
    return(new_message)

print(rot13("Hello world!"))


