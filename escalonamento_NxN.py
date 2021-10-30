#Esse código faz o escalonamento de uma matriz A quadrada NxN e ao lado uma matriz identidade também NxN, que retornará a matriz inversa da matriz A.
#Os passos são feitos pelo próprio usuário
#Feito para a disciplina de Álgebra Linear - 2021 - 5952036 - Profa. Katia Azevedo
import numpy as np
from fractions import Fraction

def switch_case():
    option = int(input("O que você gostaria de fazer em sua matriz? (Digite o numero correspondente a opção desejada)\n"
          "1. Multiplicar uma linha por um numero\n"
          "2. Multiplicar uma linha por um número e somar em outra linha\n"
          "3. Trocar a posição de duas linhas\n"
          "4. Dividir uma linha por um numero\n"
          "5. Finalizar\n"))
    return option

n = int(input("Digite a dimensão N da matriz: "))
print("Matriz",n,"x",n)
n2 = n*n
#print(type(n))

id = np.identity(n) #gera a matriz identidade com as mesmas dimensoes do input
#print(id)

print("Entre com os elementos no sentido das linhas separados por espaço: ")
elementos = list(map(float, input().split()))

# Printando a matriz
if(len(elementos) == n2):
    matriz_i = np.array(elementos).reshape(n, n)
    print("Sua matriz está da seguinte forma:")
    print(matriz_i)
    print("A matriz identidade de sua matriz é:")
    print(id)
    matriz = np.concatenate((matriz_i, id), axis=1)
    print("Vamos realizar as operações na seguinte matriz:")
    print(matriz)
    opcao = switch_case()
else:
    print("Não foram inseridos todos os elementos necessários, para que funcione, voce deve digitar",n2,"elementos")

while opcao != 5:
    if opcao==3:
        linhas = list(map(int, input("Insira o número das linhas as quais você quer trocar, considerando o número da primeria linha sendo igual a zero: ").split()))
        print("Linhas",linhas)
        ref = matriz[linhas[0]].copy()
        matriz[linhas[0]] = matriz[linhas[1]]
        matriz[linhas[1]] = ref
        print("sua nova matriz ficou da seguinte forma:\n", np.round(matriz, 2))
    elif opcao==2:
        lin_mult = int(input("Qual linha que será multiplicada? "))
        num_mult = Fraction(input("Por qual número você gostaria de multiplicar a linha acima? "))
        sum_mult = int(input("Por qual linha você gostaria de somar a linha multiplicada acima? "))
        aux_mult = matriz[lin_mult].copy() * num_mult
        matriz[sum_mult] = matriz[sum_mult] + aux_mult
        print("Sua matriz ficou assim:\n", np.round(matriz, 2))
    elif opcao==1:
        lin_mult = int(input("Qual linha que será multiplicada? "))
        num_mult = Fraction(input("Por qual número você gostaria de multiplicar a linha acima? "))
        matriz[lin_mult] = matriz[lin_mult] * num_mult
        print("Sua matriz ficou assim:\n",np.round(matriz, 2))
    elif opcao==4:
        lin_div = int(input("Qual linha que será dividida? "))
        num_div = Fraction(input("Por qual número você gostaria de dividir a linha acima? "))
        matriz[lin_div] = matriz[lin_div] / num_div
        print("Sua matriz ficou assim:\n", np.round(matriz, 2))
    opcao = switch_case()

if opcao==5:
    print("Sua matriz final ficou assim:\n", np.round(matriz, 2))
    matriz_final = np.round(np.hsplit(matriz, 2), 2)
    print("A matriz inversa da matriz inicial é:\n", matriz_final[1])



# if(matriz[0][0]==1):
#      print(oi)
# else:
#      diag = matriz[0][0]
#      for j in range(0,n):
#          matriz[0][j] = matriz[0][j]/diag
#          id[0][j] = id[0][j]/diag
#      for f in range(0,n):
#          matriz[1][f] = matriz[0][0] * (-matriz[1][f]) + matriz[1][f]
#          id[1][f] = id[0][0] * (-matriz[1][f]) + id[1][f]

#print(matriz)
#print(id)
