def notas(*n, sit=False):
    """
    ->função para analizar notas e situação de alunos.
    :param n: uma ou varios notas dos alunos (aceita varias)
    :param sit: valor opciaonal indicando se deve ou nao adicionar a situação.
    :return: Dicionario com varias informaçoes da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if r['media'] >= 7:
        r['situação'] = 'Boa'
    elif r['media'] >= 5:
        r['situação'] = 'Razoavel'
    else:
        r['situação'] = 'Ruim'
    return r


resp = notas(9, 10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
