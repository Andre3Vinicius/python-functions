
'''
def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 6)
boas_vindas('André', 6)
boas_vindas('Ronaldo', 6)


# PARAMETROS --> ARGUMENTO
#DEFAULT= AQUELE QUE VOCÊ DEFINE O VALOR NO PARAMETRO
#NO-DEFAULT = AQUELE QUE VOCê NAO DEFINE O VALOR NO PARAMETRO

#Regra- default os parametros com valores sempre tem que ir para os parametros finais.

def boas_vindas(nome, quantidade =6):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', )
boas_vindas('André', )
boas_vindas('Ronaldo', )


#TIPOS DE FUNÇÕES
#REALIZAM TAREFAS
#RETORNA UM VALOR


def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('maria')
y= cliente2('jose')

print(x)
print(y)


#CRIAR UMA FUNÇÃO QUE SOMA VARIOS NÚMEROS
#ARGUMENTOS AINDA NÃO DEFINIDOS!


def soma (*numeros):
    resultado =0
    for num in numeros:
        resultado += num
    return resultado

x= soma (2,3,4,8)

print(x)


#1) um astesristico você consegue com um parametro colocar varios argumentos, mas eles não serão definidos
#ex print(agencia('gol', 'azul', '2025')

#2) dois asteristico você consegue com um parametro colocar varios argumentos e eles serão definidos.
#exemplo abaixo

def agencia(**carro):
    return carro

print(agencia(marca='gol', cor ='prata', ano='2025'))
print(agencia(marca='gol', cor ='azul', ano='2010'))

'''
#importando um modúlo para achar o fatorial do numero selecionado.
import math

print(math.factorial(4))