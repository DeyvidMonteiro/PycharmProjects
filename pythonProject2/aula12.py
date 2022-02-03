nome = str(input('Qual é o seu nome? '))
if nome == 'Deyvid':
    print('Que nome bonito')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no Brasil')
elif nome in 'ana claudia jessica juliana':
    print('que belo nome feminino')
else:
    print('seu nome é bem normal! ')
print('tenha um bom dia {} !'.format(nome))
