# Funções com argumentos nomeados, e argumentos padrão

def saudacao(nome, tipo='comum'):
	if tipo == 'comum':
		print('Olá {}'.format(nome))
		#cout << olá << nome
	elif tipo == 'top':
		print('Salve, salve {}'.format(nome))
	else:
		print('Po {}... passe um tipo que existe'.format(nome))