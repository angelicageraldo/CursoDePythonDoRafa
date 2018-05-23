#Listas, tuplas, dicionarios e sets

#lista

x=[]
print(x)
x.append(1)
print(x)
x.insert(0, -15)        #índice, valor
print(x)

#tupla

y=(5,6,4)   #é imutável e mais rápida que lista

#sets

meu_set = {1,2,3}
seu_set = {4,5,1}

if 1 in meu_set:
    print('Deu boa')
meu_set.add(1)  #não repete elementos
sou_sexy = meu_set & seu_set    #intersecção
nao_sou_sexy = meu_set | seu_set    #união

#dicionário

notas = {'Fis':9.5, 'Qui':8.0, 'Mat':5.0}
print(notas['Fis']  #retorna 9.5
print(notas['Qui']  #retorna 8.0
notas['Por'] = 7.0  #adicionar chave "Por com valor 7.0"
