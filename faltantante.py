def encontrar_faltante(lista):
    n = 5 
    soma_total = n * (n + 1) // 2  
    soma_lista = sum(lista)  
    return soma_total - soma_lista  


entrada = [1, 3, 4, 5]
print(encontrar_faltante(entrada))  

## Resolvido utilizando uma formula matematica, N representa a quantidade de numero faltando na lista incluindo o faltante, por isso o +1 é inserido nele. Com isso sempre
