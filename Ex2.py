''' Criar uma classe Pessoa
Ela deve ter um nome e uma lista de amigos
- O nome é fornecido na inicialização
- A lista de amigos deve ser vazia inicialmente
Criar 3 métodos
- Cria uma saudação do tipo:
	x = Pessoa('Rafael')
	x.ola()
	Olá! Eu sou Rafael
- Adicionar um amigo à lista de amigos:
	x = Pessoa('Juca')
	x.add_friend('Olaf')
	x.add_friend('Marcos')
- Imprimir na tela a sua lista de amigos:
	x.show_friends()
	['Olaf', 'Marcos']
'''

class Pessoa:
	def __init__(self, nome):
		self.eu = nome
		self.amigos = []
		self.ola = 'Olá, {}'.format(self.eu)
		
	def add_amigos(self, amigo):
		self.amigos.append(amigo)
		print('Seus amigos são: ', self.amigos)

	def ola_amigos(self):
		print('Beijos', end=' ')
		for amigo in self.amigos:
			# print('Beijos {}'.format(self.amigos))
			print(amigo, end = ', ')


x = Pessoa('Angel')
print(x.ola)
x.add_amigos('Lux')
x.add_amigos('Jazz')
x.add_amigos('Rafa')
x.ola_amigos()