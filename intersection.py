def intersection(x1, y1, x2, y2, x3, y3, x4, y4) -> int:
    """Первая функция на нахождение пересечения."""

    left = max(x3, x1)
    bottom = max(y2, y4)
    right = min(x4, x2)
    top = min(y1, y3)

    width = right - left
    height = top - bottom

    if width <= 0 or height <= 0:
        return 0
    else:
        return width * height