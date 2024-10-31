# Tacógrafos - Cálculo da Distância Percorrida

## Descrição

Tacógrafos são dispositivos essenciais instalados em veículos de transporte coletivo e carga, que registram informações sobre velocidade, tempo e distância percorrida. A empresa SBC (Sociedade Brasileira dos Caminhoneiros) encomendou uma versão mais simples e acessível dos tacógrafos, que registram apenas intervalos de tempo e velocidades médias. Este programa tem como objetivo calcular a distância total percorrida por caminhões com base nos dados fornecidos pelo tacógrafo.

## Problema

Você deverá escrever um programa que recebe uma série de intervalos de tempo com suas respectivas velocidades médias e calcula a distância total percorrida pelo caminhão.

## Entrada

- A primeira linha contém um inteiro **N** (1 ≤ N ≤ 1000) representando a quantidade de intervalos de tempo registrados no tacógrafo.
- As **N** linhas seguintes descrevem os intervalos de tempo. Cada linha contém dois inteiros:
  - **T** (1 ≤ T ≤ 100): o tempo decorrido em horas.
  - **V** (0 ≤ V ≤ 120): a velocidade média em quilômetros por hora.

## Saída

- O programa deve imprimir uma única linha contendo um único número inteiro representando a distância total percorrida, em quilômetros.

## Cálculo da Distância

A distância percorrida em cada intervalo pode ser calculada utilizando a fórmula:
\[
\text{Distância} = \text{Tempo} \times \text{Velocidade}
\]
A distância total será a soma das distâncias calculadas para cada intervalo.

## Exemplo de Entrada

```
3
2 60
3 80
1 100
```

## Exemplo de Saída

```
440
```

### Explicação do Exemplo

- No primeiro intervalo, a distância é \( 2 \, \text{h} \times 60 \, \text{km/h} = 120 \, \text{km} \)
- No segundo intervalo, a distância é \( 3 \, \text{h} \times 80 \, \text{km/h} = 240 \, \text{km} \)
- No terceiro intervalo, a distância é \( 1 \, \text{h} \times 100 \, \text{km/h} = 100 \, \text{km} \)

Assim, a distância total percorrida é \( 120 + 240 + 100 = 460 \, \text{km} \).

## Restrições

- O número de intervalos **N** não pode ultrapassar 1000.
- O tempo e a velocidade estão dentro dos limites estabelecidos, garantindo que os cálculos sejam válidos.

## Conclusão

Este programa ajudará a SBC a determinar a distância total percorrida pelos caminhões, garantindo que os motoristas possam operar dentro dos limites adequados e contribuindo para a segurança nas estradas.
