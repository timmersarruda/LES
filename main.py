import Les

lista = Les.Les()

if not (lista.estaCheia()):
    lista.inserirFim(1)
if not (lista.estaCheia()):
    lista.inserirFim(2)
if not (lista.estaCheia()):
    lista.inserirFim(3)
if not (lista.estaCheia()):
    lista.inserirFim(4)
if not (lista.estaCheia()):
    lista.inserirFim(1)
if not (lista.estaCheia()):
    lista.inserirFim(6)
print('Lista com insercao dos elementos 1, 2, 3, 4 e 5 no fim da lista e tentativa do 6')
lista.imprimir()

if not (lista.estaVazia()):
     lista.removerFim()
if not (lista.estaVazia()):
     lista.removerFim()
if not (lista.estaVazia()):
    lista.removerFim()
print('Lista com remocao dos 3 ultimos elementos da lista')
lista.imprimir()

print('Quantidade de elementos da lista: ', lista.getQuant())
if not (lista.estaCheia()):
    lista.inserirInicio(0)
if not (lista.estaCheia()):
    lista.inserirInicio(-1)

print('Lista com insercao dos elementos -1, 0, 1, e 2')
lista.imprimir()

if not (lista.estaVazia()):
    lista.removerInicio()
lista.imprimir()
if not (lista.estaVazia()):
    lista.removerInicio()
lista.imprimir()
print('Posicao do elemento 4: ', lista.consultarElemento(4))
print('Posicao do elemento 6: ', lista.consultarElemento(6))
lista.removerFim()
print('Primeiro elemento da lista', lista.getPrim())
print('Ultimo elemento da lista', lista.getUlt())

print('Quantidade de elementos 1 na lista', lista.contarQtdOcorrencias(1))
print('Soma dos elementos da lista', lista.somaElementos())

lista.substituirTodasOcorrencias(1, 2)
lista.imprimir()