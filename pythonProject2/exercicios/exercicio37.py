times = ('corintians', 'palmeiras', 'santos', 'gremio',
         'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
         'ateltico', 'botafogo', 'atretico-PR', 'bahia',
         'sao paulo', 'fluminense', 'sport recife',
         'ec vitoria', 'coritiba', 'avai', 'ponte preta',
         'atletico-GO')
print('-=' * 20)
print(f'lista de times{times} ')
print('-=' * 20)
print(f'os cinco primeiro times são {times[0:5]} ')
print('-=' * 20)
print(f'os 4 ultimos colocados foram {times[-4:]}')
print('-=' * 20)
print(f'times em ordem alfabetica: {sorted(times)} ')
print('-=' * 20)
print(f'o chapecoense esta na {times.index("chapecoense")+1}ª posição')
