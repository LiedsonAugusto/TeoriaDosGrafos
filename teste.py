from concurrent.futures.process import _ExceptionWithTraceback
from re import A
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import MeuGrafo
from sys import maxsize
#python -m unittest grafo_test.TestGrafo.test_bfs


def dijkstra_drone(self, vi, vf):
        # CRIAÇÃO DOS DICIONÁRIOS
        beta = {x: maxsize if x != vi else 0 for x in self.N}
        alpha = {x: 0 if x != vi else 1 for x in self.N}
        omega = {x: "Nulo" if x == vi else "" for x in self.N}

        # VARIÁVEIS QUE CONTROLAM O FLUXO DA FUNÇÃO
        percurso = vi
        destino = vf

        # PERCORRER TODOS OS VERTICES ATÉ ELE CHEGAR EM SEU DESTINO
        while percurso != destino:
            
            # LISTA COM OS VÉRTICES ADJACENTES AO PERCURSO
            verticesAdjacntes = list(self.arestas_sobre_vertice(percurso))

            #PERCORRER A LISTA
            for x in verticesAdjacntes:
                # VERIFICAR SE O V1 DAQUELA ARESTA É IGUAL AO PERCURSO, PARA O BETA DO VÉRTICE OPOSTO SER ALTERADO
                if self.A[x].getV1() == percurso:
                    #VERIFICA SE O PESO DESSA ARESTA É MENOR QUE O PESO QUE JA ESTÁ NESSA CHAVE NO BETA
                    if beta[self.A[x].getV2()] > self.A[x].getPeso() and alpha[self.A[x].getV2()] == 0:
                        # ATRIBUIÇÃO DO NOVO VALOR DE BETA CASO A CONDIÇÃO ACONTEÇA
                        beta[self.A[x].getV2()] = self.A[x].getPeso() + beta[self.A[x].getV1()]
                        omega[self.A[x].getV2()] = self.A[x].getV1()
                # MESMO PROCESSO PARA O V2
                else:
                    if beta[self.A[x].getV1()] > self.A[x].getPeso() and alpha[self.A[x].getV1()] == 0:
                        beta[self.A[x].getV1()] = self.A[x].getPeso() + beta[self.A[x].getV2()]
                        omega[self.A[x].getV1()] = self.A[x].getV2()

            alpha[percurso] = 1
            menorBeta = maxsize
            #PERCORRER A LISTA DE VERTICES
            for y in self.N:
                # VERIFICA SE O MENOR BETA NÃO É O INICIAL (QUE E SEMPRE 0), SE AQUELE VERTICE JA FOI VISITADO E SE ELE É MENOR QUE O MENOR BETA
                if alpha[y] != 1 and beta[y] < menorBeta:
                    menorBeta = beta[y]
                    percurso = y
        # IMPRESSAO DA LISTA COM OS VERTICES QUE INDICAM O MENOR CAMINHO
        listaFinal = dijkstraImpressao(self, omega, destino)
    
        return listaFinal 

def dijkstraImpressao(self, omega, destino):
    #RECEBE O FINAL DO CAMINHO
    percurso2 = destino
    #ADICIONA ELE
    listaFinal = [percurso2]
    #PERCORRE OS CAMINHOS DE OMEGA
    while percurso2 != "Nulo":
        #ADICIONA O ANTECESSOR DE PERCURSO
        listaFinal.append(omega[percurso2])
        #ATUALIZA VALOR DE RECURSO
        percurso2 = omega[percurso2]
    listaFinal.pop()
    return listaFinal
        
            

            
            
            

MeuGrafo3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
MeuGrafo3.adicionaAresta('a1', 'J', 'C')
MeuGrafo3.adicionaAresta('a2', 'C', 'E')
MeuGrafo3.adicionaAresta('a3', 'C', 'E')
MeuGrafo3.adicionaAresta('a4', 'P', 'C')
MeuGrafo3.adicionaAresta('a5', 'P', 'C')
MeuGrafo3.adicionaAresta('a6', 'T', 'C')
MeuGrafo3.adicionaAresta('a7', 'M', 'C')
MeuGrafo3.adicionaAresta('a8', 'M', 'T')
MeuGrafo3.adicionaAresta('a9', 'T', 'Z')


Meugrafo2 = MeuGrafo(['A', 'B', 'C', 'D'])
Meugrafo2.adicionaAresta('a1', 'A', 'B')
Meugrafo2.adicionaAresta('a2', 'B', 'C')
Meugrafo2.adicionaAresta('a3', 'C', 'D')


MeuGrafo2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
MeuGrafo2.adicionaAresta('a1', 'A', 'B', 1)
MeuGrafo2.adicionaAresta('a2', 'B', 'E', 1)
MeuGrafo2.adicionaAresta('a3', 'A', 'C', 2)
MeuGrafo2.adicionaAresta('a4', 'C', 'D', 2)
MeuGrafo2.adicionaAresta('a5', 'D', 'F', 2)

abc = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
abc.adicionaAresta('a1', 'A', 'B', 1)
abc.adicionaAresta('a2', 'A', 'C', 2)
abc.adicionaAresta('a3', 'C', 'D', 1)
abc.adicionaAresta('a4', 'B', 'D', 4)
abc.adicionaAresta('a5', 'D', 'E', 1)

print(dijkstra_drone(MeuGrafo2, 'A', 'F'))

# string = "0123456789012345678901234567890123456789012345678901234567890123456789"
# lista = [string[v:v+10] for v in range(len(string)) if v % 10 == 0]

# retorno = '.'.join(lista)
# print(retorno)

