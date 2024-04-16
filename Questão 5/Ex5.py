def inverter_string(s):
    str_invertida = ''
    for i in range(len(s) - 1, -1, -1):
        str_invertida += s[i]
    return str_invertida

# Testando a função
s = "Olá, Mundo!"
print("String Original: ", s)
print("String Invertida: ", inverter_string(s))
