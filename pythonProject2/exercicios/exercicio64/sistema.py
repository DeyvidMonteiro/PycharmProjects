from exercicios.exercicio64.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver Pessoa Cadastrada ', 'Cadastrar Nova Pessoa', 'Sair Do Sistema '])
    if resp == 1:
        # opção de listar um arquivo!
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Nova Cadastro ')
        nome = str(input('Nome: '))
        idade = int(input('idade: '))
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo Do Sistema... Até Logo! ')
        break
    else:
        print('\033[31mERRO! Digite Uma Opção Valida \033[m')
    sleep(1)
