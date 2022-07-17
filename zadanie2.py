def palindrom(slovo):
    # if slovo[::-1].startswith(slovo):
    if slovo[::-1]==slovo:
        return 'палиндром'
    else:
        return 'не палиндром'
slovo=input('Введите слово')
print(palindrom(slovo))