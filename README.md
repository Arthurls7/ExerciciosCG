# ExerciciosCG

Calcule as diferenças dx = 8 - 1 = 7 e dy = 5 - 1 = 4.

Os incrementos de x e y são 1, já que dx e dy são ambos positivos.

O erro inicial é err = dx - dy = 3.

Para cada pixel na linha, faça:

a) Desenhe o pixel com as coordenadas (1, 1).

b) Calcule o erro e2 = 2*err = 6.

c) Como e2 > -dy = -4, atualize o erro err -= dy = -1 e adicione o incremento de x, que é 1, ao x atual, x0 += 1. O ponto atual é agora (2, 1).

d) Desenhe o pixel com as coordenadas (2, 1).

e) Calcule o erro e2 = 2*err = -2.

f) Como e2 < dx = 7, atualize o erro err += dx = 5 e adicione o incremento de y, que é 1, ao y atual, y0 += 1. O ponto atual é agora (2, 2).

g) Desenhe o pixel com as coordenadas (2, 2).

Repetimos esse algoritmo até que x0 = xy e y0 = y1
