def karta(cart):
    return '*'*len(cart[:-4])+cart[-4:]
print(karta('12345678912345678'))