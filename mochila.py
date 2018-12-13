# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity W 

import sys 

def mochila(P, pt, val, n, vet): 
    K = [[0 for x in range(P+1)] for x in range(n+1)] 
   
    for i in range(n+1): 
        for w in range(P+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif pt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-pt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    aux1 = n
    aux2 = P
    while i != 0:
        if K[aux1][aux2] == K[aux1-1][aux2]:
             
            vet = list.append(aux1)
        else:
            aux1 = aux1-1
    return K[n][P] 
  

valorItem = [60, 100, 120,10,20,30,40,50,60,70,80,90,10,20,30,40] 
pesoIten = [10, 20, 30,15,12,14,16,16,12,12,13,14,15,15,15,15,12] 
pesoTotal = 40
vet =  [ ]
n = len(valorItem) 
print(mochila(pesoTotal, pesoIten, valorItem, n, vet))
   