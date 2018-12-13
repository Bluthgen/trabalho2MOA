# -*- coding: utf-8 -*-
import math
import itertools
from itertools import combinations
import numpy as np
import sys
import random

pesoMax= 0

def inicializaMochila():    
    peso= []
    valor= []
    global pesoMax
    with open("input1.txt", "r") as arquivo:
        i= -1
        for linha in arquivo:
            if i<0:
                pesoMax= (int (linha))
                i= i+1
                continue
            params= linha.split(",")
            params= (int(params[0]), int(params[1]))
            peso.append(params[0])
            valor.append(params[1])
            i= i+1
    return (peso, valor)

par= inicializaMochila()
peso, custo= par[0], par[1]
n= len(peso)
memo= memo = [[0 for x in range(pesoMax+1)] for x in range(n+1)]

def mochilaBinariaPD(pesoMax, peso, valor, n): 
    global memo
    for i in range(n+1): 
        for p in range(pesoMax+1): 
            if i==0 or p==0: 
                memo[i][p] = 0
            elif peso[i-1] <= p: 
                memo[i][p] = max(valor[i-1] + memo[i-1][p-peso[i-1]],  memo[i-1][p]) 
            else: 
                memo[i][p] = memo[i-1][p] 
    result = np.zeros(n)
    pm = pesoMax
    for j in range(n, 0, -1):
        adicionado = memo[j][pm] != memo[j-1][pm]
 
        if adicionado:
            pt = peso[j-1]
            result[j-1]= 1
            pm -= pt
    return (memo[n][p], result)  

r= mochilaBinariaPD(pesoMax, peso, custo, n)
print(r[0], r[1])
