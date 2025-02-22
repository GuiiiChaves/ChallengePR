def separar_par_impar(array):
    pares = []
    impares = []
    
    for numeros in array:
        if numeros % 2 == 0:
            pares.append(numeros) 
        else:
            impares.append(numeros) 
    
    
    return pares + impares


entrada = [1, 3, 4, 2, 9, 8, 7, 6]
saida = separar_par_impar(entrada)
print(saida) 

## Utilizar o % para descobrir se o numero é par ou impar, logo após ele vai fazer as separações por eles baseado no seu "tipo (par) ou (impar)" e retornar eles de forma concatenada.
