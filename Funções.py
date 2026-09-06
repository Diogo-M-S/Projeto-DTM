def linha():
    print('-'*30)

def tipo_de_carga():
    print('Qual o tipo de Carga? \n')
    print(''' 1) Resistiva \n 2) Indutiva \n 3) Iluminação \n''')
    while True:
        while True:
            try:
                carga=int(input('Digite o número: '))
                break
            except ValueError:
                print('Digite o número correspondente a carga')
    
        if carga == 1:
            carga = 'Resistiva'
            break
        elif carga == 2:
            carga = 'Indutiva'
            break   
        elif carga == 3:
            carga = 'Iluminação'
            break
        else:
            print('Escolha uma das opções existentes')
    return carga

def curva_da_carga(carga):
    if carga in ['Iluminação','Resistiva']:
        curvatura = 'Curva B'
    elif carga == 'Indutiva':
        curvatura = 'Curva C'
    return curvatura

def receber_informacao(info):
    while True:
        try:
            informacao = int(input(f'Insira a {info}: '))
            break
        except ValueError:
            print('Informe apenas números, sem "."')
    return informacao

def calculo_dtm(p = 0,i = 0,u = 0):
    calculo = {}

    if p == 0 and u != 0 and i != 0:
        p = u * i

    elif i == 0 and u != 0 and p != 0:
        i = p / u
                   
    elif u == 0 and p != 0 and i != 0:
        u = p / i
    else:
        return {'erro': 'Falta de informação (Forneça dois valores)'}
        

    dtm = i * 1.2 

    calculo['Potencia'] = p
    calculo['Tensão'] = u
    calculo['Corrente'] = i
    calculo['Dtm'] = dtm
    return calculo

TABELA_AMPACIDADE = [
    (15.5, 1.5),
    (19.5, 2.5),
    (26.0, 4.0),
    (34.0, 6.0),
    (46.0, 10.0),
    (61.0, 16.0),
    (80.0, 25.0),
    (101.0, 35.0),
    (126.0, 50.0),
    (153.0, 70.0),
    (196.0, 95.0),
    (226.0, 120.0),
    (263.0, 150.0),
    (300.0, 185.0),
]
BITOLA_MINIMA = {
    'Iluminação': 1.5,
    'Resistiva': 2.5,
    'Indutiva': 2.5,
}