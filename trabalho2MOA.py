# -*- coding: utf-8 -*-
import math
import itertools
from itertools import combinations
import numpy as np
import sys
import random

class Vertice:
    def __init__(self, nome:int, coords:tuple):
        self.nome= nome
        self.x, self.y= coords
        self.tipo= ""

    #Cálculo da distancia entre dois Vértices - peso da aresta
    @staticmethod
    def distance(v1, v2):
            return math.hypot(v2.x - v1.x, v2.y - v1.y)
        
    def __repr__(self):
        return f'{self.nome}'

#Classe do Grafo
class GrafoCartesiano:
    def __init__(self):
        self.vertices= []
        
    #Adicionar um vértice ao Grafo    
    def add(self, v):
        if isinstance(v, Vertice):
            self.vertices.append(v)
            

def c(grafo):
    S= grafo.vertices.copy()
    n= len(S)
    Custos= np.zeros((n,n), dtype=np.int64)
    #S1= S.copy()
    #S1.remove(grafo.vertices[0])
    for k in range(2, n):
        for Sk in combinations(S, k):
            #Sk.insert(0, grafo.vertices[0])
            if not grafo.vertices[0] in Sk:
                continue
            Custos[k][1]= sys.maxsize - 1
            for j in range(1, n):
                possibilidades= []
                for i in Sk:
                    if i != j:
                        possibilidades.append(Custos[k-j][i.nome-1] + Vertice.distance(i, grafo.vertices[j]))
                #print(Custos)
                #print(possibilidades)
                #print(min(possibilidades))
                Custos[k][j]= min(possibilidades)
    respostas= []
    for j in S:
        respostas.append(Vertice.distance(j, grafo.vertices[0]) + Custos[n-1][j.nome - 1])
    return min(respostas)

def inicializaCartesiano():    
    grafo= GrafoCartesiano()
    with open("input1.txt", "r") as arquivo:
        i= 0
        for linha in arquivo:
            coords1= linha.split(",")
            coords= (float(coords1[0]), float(coords1[1]))
            grafo.add(Vertice(i, coords))
            i= i+1
    return grafo

grafo= inicializaCartesiano()
n= len(grafo.vertices)
custos= np.zeros((2<<n, n), dtype=np.int64)
caminho= np.zeros(n)
for i in range(n):
    caminho[i]= -1
for i in range(2<<n):
    for j in range(n):
        custos[i][j]= -1
    


def tsp(grafo, visitados, pos):
    #print("Visitados: ", visitados)
    #print("Pos: ", pos)
    #x= 0
    #print("Distancia: ", Vertice.distance(grafo.vertices[pos], grafo.vertices[0]))
    #print("Visitados: ", visitados, "Todos: ", (1<<n -1))
    if visitados == ((1<<n) -1):  #Todos os vértices foram visitados
        return Vertice.distance(grafo.vertices[pos], grafo.vertices[0])
    #print("Matriz: ", custos[visitados][pos])
    if custos[visitados][pos] > -1:  #Resposta já calculada
        return custos[visitados][pos]
    resposta= sys.maxsize
    prox= -1
    for v in grafo.vertices:
        if visitados&(1<<v.nome) == 0:  #Se o vértice ainda não foi visitado
            #input(x)
            r= Vertice.distance(grafo.vertices[pos], v) + tsp(grafo, visitados|(1<<v.nome), v.nome)
            #possibilidades= [resposta, r]
            #print(possibilidades)
            #resposta= min(possibilidades)
            if r < resposta:
                resposta= r
                prox= v.nome
    custos[visitados][pos]= resposta
    caminho[pos]= prox
    return resposta

print(tsp(grafo, 1, 0))
print(caminho)