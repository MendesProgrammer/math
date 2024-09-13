# Tirar raiz quadrada para descobrir se n é primo

from math import trunc
 
# Recebe um número para ver se ele é primo
numero = int(input('Digite um número: '))

# Tira a raiz deste número
raiz = numero ** (1/2)

contador_raiz = contador_primo = 0

# Pega a parte inteira do número
inteiro_raiz = trunc(raiz)

# Listagem da inteiro raiz
# Começa por 2 pois pela definição, todo número é pelo menos divisível por 1 e por ele mesmo
for listagem in range(2, inteiro_raiz+1):

    # Verifica se "listagem" e primo
    for divisor in range(2, listagem+1):
        if listagem % divisor == 0:
            # Se for primo for maior que 1, então ele tem mais divsores do que ele mesmo e 1
            contador_raiz += 1

    # Se o "listagem" for primo
    if contador_raiz == 1:
        # Se contador_primo for maior que zero, numero não é primo
        if numero % listagem == 0:
            contador_primo += 1
            
    # Reinicia para não ser contado duas vezes
    contador_raiz = 0

if contador_primo == 0:
    print('É primo')
else:
    print('Não é primo')