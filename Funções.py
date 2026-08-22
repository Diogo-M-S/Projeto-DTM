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

def calculo_dtm(p,i,u):
