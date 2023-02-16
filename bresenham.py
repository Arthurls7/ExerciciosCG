def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    line = []

    while x0 != x1 or y0 != y1:
        line.append((x0, y0))
        e2 = 2*err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    line.append((x0, y0))
    return line


# Exemplo de uso:
line = bresenham_line(1, 1, 8, 5)
print(line)
