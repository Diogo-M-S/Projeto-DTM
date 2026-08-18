dtm = 0
p = i = u = carga = 0

while 1 > dtm: 

    p = int(input('Insira a potência(W) da massa/Eletro-eletrônico : '))

    i = float(input('Insira a corrente(A): '))

    u = float(input('Insira a tensão(V): '))

    carga = input(('''Que tipo de carga será aplicada?
    Ex: Resistiva, indutiva, iluminação: '''))

    print('\n')
    print('-' * 100)
    print("")

    if carga == 'Resistiva' or carga == 'Iluminação':
        carga = 'Curva B'

    elif carga == 'Indutiva':
        carga = 'Curva C'

    if p == 0 and u != 0 and i != 0:
        p = u * i

    elif i == 0 and u != 0 and p != 0:
        i = p / u
            
    elif u == 0 and p != 0 and i != 0:
        u = p / i

    dtm =  i * 1.2

    if 1 > dtm:
        print('Valores inesperados, por favor ultilize valores válidos')
        print()

if dtm <=6:
    dtm = 6

elif dtm <= 10:
    dtm = 10

elif dtm <= 16:
    dtm = 16

elif dtm <=20:
    dtm = 20

elif dtm <= 25:
    dtm = 25

elif dtm <= 32:
    dtm = 32

elif dtm <=40:
    dtm = 40

elif dtm <= 50:
    dtm = 50

elif dtm <= 63:
    dtm = 63


print(f'A potência é de {p}W, a corrente é de {i:.2f}A e Tensão de {u:.2f}V')
print(f'O disjuntor indicado é de {dtm}A, carga do tipo {carga}')

