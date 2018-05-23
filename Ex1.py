# Passo 1 - criar lista com 5 amigos (strings)
# Passo 2 - pedir ao usuário que digite um nome (salve a resposta)
# Passo 3 - verificar se o nome está na lista de amigos. 
# 		  Se estiver, imprima saudação bem humorada;
# 		  Se não, convide a pessoa para ser sua amiga

amigos = ['Lux', 'Jazz', 'Carolzinha', 'Victor da Nathassia', 
'Nathassia do Victor']

nome = input('Digite seu nome: ')

if nome in amigos:
	print('Oi abiguinho, seja bem-vindo!')
	print(amigos)
else:
	novos_amigos = []
	novos_amigos.append(nome)
	amigos.append(novos_amigos[-1])
	print('Olá, você agora já é beu dovo abiguinho!')
	print("Novos amigos: ", novos_amigos)
	print("Amigos do peito: ", amigos)

# --- Novos passos ---

# Passo 4 - criar uma lista de novos amigos. PS: a lista deve ser vazia
# Passo 5 - adicionar novo amigo à lista
# Passo 6 - verificar se ele(a) está na lista
# Passo 7 - "você é meu novo amigo!"

