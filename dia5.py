# Classes - Orientação a objeto

# def meus_livros(nome):
# 	return [nome]

# def add_livro(livro, biblio):
# 	biblio.append(livro)
# 	print('Adicionei o livro {}'.format(livro))

# biblioteca = meus_livros('Angel')
# print(biblioteca)
# add_livro('Harry Potter', biblioteca)
# add_livro('Dom Casmurro', biblioteca)
# print(biblioteca)

class Biblioteca:

	def __init__(self, nome):
		'''Funções em classes se chamam métodos'''
		self.dono = nome
		self.livros = []

	def add_livro(self, livro):
		self.livros.append(livro)

x = Biblioteca('Rafael') # x é uma instância da classe Biblioteca
# print(x.nome)
print(x.dono)
print(x.livros)	
x.add_livro('123')
print(x.livros)


# class Biblioteca(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, nome):
# 		super(Biblioteca, self).__init__()
# 		self.nome = ''

