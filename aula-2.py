#Try/Except

# Exemplo que causa TypeError
try:
    resultado = len(3)
except TypeError as e:
    print(e) #Imprime a mensagem de erro
    

# Exemplo que causa TypeError
try:
    resultado = len("Mariana")
except TypeError as e:
    print(e) #Imprime a mensagem de erro
else: 
    print("Tudo ocorreu bem")
    

try:
    resultado = len("Mariana")
except TypeError as e:
    print(e) #Imprime a mensagem de erro
else: 
    print("Tudo ocorreu bem")
finally:
    print("O importante é participar")