# Exercício de CG - Algoritmo de Bresenham

### Exemplificando com o ponto (1,1) e (8,5)

#### Calculando as diferenças: 

dx = 8 - 1 = 7

dy = 5 - 1 = 4

#### Os incrementos de x e y são 1, já que dx e dy são ambos positivos.
#### O erro inicial é: err = dx - dy = 3.

# Para cada pixel na linha, repetimos:

a) Desenhamos o pixel com as coordenadas (1, 1) que correspondem a -> x0, y0.

b) Calculamos o erro: e2 = 2*err = 6.

c) Como e2 > -dy = -4, atualizamos o erro err -= dy = -1 e adicionamos o incremento de x, que é 1, ao x atual, x0 += 1. O ponto atual é agora (2, 1).

d) Como e2 < dx = 7, atualizamos o erro err += dx = 5 e adicionamos o incremento de y, que é 1, ao y atual, y0 += 1. O ponto atual é agora (2, 2).

e) Desenhamos o pixel com as coordenadas (2, 2).

Repetimos esse processo até que x0 = xy e y0 = y1
