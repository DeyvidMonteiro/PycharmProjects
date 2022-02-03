from exercicios.exercicio64.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve Um ERRO Na Criação do Arquivo! ')
    else:
        print(f'Arquivo {nome} Criado Com Sucesso! ')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler Arquivo! ')
    else:
        cabecalho('PESSOAS CADASTRADAS ')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve Um Erro Na Abertura Do Arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO Na Hora de Escrever Os Dados! ')
        else:
            print(f'Novo Registro De {nome} Adicionado')
