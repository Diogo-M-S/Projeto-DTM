def linha():
    return print('-'*30)
def tipo_de_carga():
    print('Qual o tipo de Carga?')
    linha
    print('''1 Resistivo \n 2 Indutivo \n 3 Iluminação''')
    while True:
        try:
            carga=int(input('Digite o número: '))
            break
        except ValueError:
            print('Digite o número correspondente a carga')
        
    if carga == 1:
        carga = 'Resistivo'
    elif carga == 2:
        carga = 'Indutivo'
    elif carga == 3:
        carga = 'Iluminação'