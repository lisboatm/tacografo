# Lendo o número de intervalos
N = int(input())

# Inicializando a distância total
distancia_total = 0

# Processando cada intervalo
for _ in range(N):
    # Lendo o tempo e a velocidade
    T, V = map(int, input().split())
    
    # Calculando a distância percorrida neste intervalo
    distancia_intervalo = T * V
    
    # Somando a distância do intervalo à distância total
    distancia_total += distancia_intervalo

# Imprimindo a distância total percorrida
print(distancia_total)
