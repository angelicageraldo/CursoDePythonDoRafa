idade = int(input('Qual a sua idade? '))  #input sempre retorna string
#idade = int(idade)

try:
    idade = int(idade)

except ValueError:
    print('Você não merece ver o filme')

    

if idade >= 18:
    print('Você pode assistir Deadpool')
else:
    print('Espere sair no torrent')
