def linha():
    print('-'*30)

def tipo_de_carga():
    '''Definir qual tipo de carga será ultilizado'''

    print('Qual o tipo de Carga? \n')
    print(''' 1) Resistiva \n 2) Indutiva \n 3) Iluminação \n''')
    
    #Resistiva para transferencia de energia em calor
    #Indutiva para motores que tem um pico de energia

    while True:
        while True:
            try:
                carga=int(input('Digite o número: '))
                break
            except ValueError:
                print('Digite o número correspondente a carga!')
    
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
    ''' Curva do disjuntor'''
    carga = carga.lower()

    if carga in ['iluminacao','iluminação','resistiva']:
        curvatura = 'Curva B'
    elif carga == 'indutiva':
        curvatura = 'Curva C'
    else:
        curvatura = 'Carga desconhecida'
    return curvatura

def receber_informacao(info,tipo = float):
    '''Função padrão para coleta de dados'''
    #Info = Informação necessária
    while True:
        try:
            dados = input(f'Insira {info}: ')
            #Verificação para evitar erro
            if tipo is float:
                dados = dados.replace(',' , '.')    
            informacao = tipo(dados)
            break
        #Para testar se o código está se comportando da maneira esperada
        except Exception as erro:
            print(f'Erro detectado {erro.__class__}')
    return informacao
    

def calculo_dtm(p = 0,i = 0,u = 0):
    '''Cálculo para saber Pôtencia, Corrente, Tensão
      e posterior calculo do disjuntor'''
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