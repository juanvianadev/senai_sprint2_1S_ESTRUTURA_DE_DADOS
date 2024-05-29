# -*- coding: utf-8 -*-
"""senai_python_aula9_FILA_LISTA_PILHA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BOPqT3HmbF8zHEQkbijq72GucPdPJQyg

## Fila
FIFO

Primeiro a entrar e o primeiro a sair
"""

fila = []

def enfileirar(elemento):
  fila.append(elemento)
  print(f"Ëlemento {elemento} foi enfileirado")

def desenfileirar():
  if len(fila) > 0:
    primeiroElemento = fila.pop(0)
    print(f"Ëlemento {primeiroElemento} foi desenfileirado")
  else:
    print("A fila esta vazia")

enfileirar(3)
enfileirar(5)
enfileirar(9)
enfileirar(3)
enfileirar(5)
enfileirar(9)
print(fila)
print(len(fila))

desenfileirar()
print(fila)
print(len(fila))

desenfileirar()
print(fila)
print(len(fila))

desenfileirar()
print(fila)
print(len(fila))

"""## Pilha

FIFO

Ultimo e o primeiro a sair
"""

pilha = []

def empilhar(elemento):
  pilha.append(elemento)
  print(f"Elemento {elemento} foi emplilhado"
  )

def desenpilhar():
  if len(pilha) > 0:
    topo = pilha.pop()
    print(f"Ëlemento {topo} foi desenpilhado")
  else:
    print("A pilha esta vazia")

empilhar(3)
empilhar(5)
empilhar(9)
print(pilha)
print(len(pilha))

desenpilhar()
print(pilha)
print(len(pilha))

"""## Lista
LIFO
"""

listaFrutas = ['laranja', 'maca', 'pera', 'banana', 'kiwi']

primeiraFruta = listaFrutas[0]
print(primeiraFruta)

ultimaFruta = listaFrutas[-1]
print(ultimaFruta)

listaFrutas.append('Abacaxi')
print(listaFrutas)

listaFrutas.remove('maca')
print(listaFrutas)

if 'banana' in listaFrutas:
  print('Tem banana!')
print(listaFrutas)

tamanhoLista = len(listaFrutas)
print(tamanhoLista)

for fruta in listaFrutas:
  print(f'Fruta: {fruta}')

frutasMaiusculo = [f.upper() for f in listaFrutas]
print(frutasMaiusculo)

generoFilmes = ['comedia', 'acao', 'romance', 'terror', 'suspense']

def enfileirarFilmes(filmes):
  print(f'Genero {filmes}')
  print(f"Genero {filmes} foi enfileirado")

def desenfileirarFilmes():
  if len(generoFilmes) > 0:
    primeiroElemento = generoFilmes.pop(0)
    print(f"Genero {primeiroElemento} foi desenfileirado")
  else:
    print("A fila esta vazia")

def enpilharFilmes(filmes):
  print(f'Genero {filmes}')
  print(f"Genero {filmes} foi enpilhado")

def desenpilharFilmes():
  if len(generoFilmes) > 0:
    topo = generoFilmes.pop()
    print(f"Ëlemento {topo} foi desenpilhado")
  else:
    print("A pilha esta vazia")

enfileirarFilmes(generoFilmes)
print(generoFilmes)
print(len(generoFilmes))

desenfileirarFilmes()
print(generoFilmes)
print(len(generoFilmes))

enpilharFilmes(generoFilmes)
print(generoFilmes)
print(len(generoFilmes))

desenpilharFilmes()
print(generoFilmes)
print(len(generoFilmes))