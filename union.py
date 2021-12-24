def union(x1, y1, x2, y2, x3, y3, x4, y4) -> int:
    """Вторая функция на нахождение объединения."""

    left = max(x3, x1)
    bottom = max(y2, y4)
    right = min(x4, x2)
    top = min(y1, y3)

    width = right - left
    height = top - bottom

    square_first = (y1-y2)*(x2-x1)
    square_second = (y3-y4)*(x4-x3)
    square_intersection = (width * height)

    if width <= 0 or height <= 0:
        return 0
    else:
        return square_first + square_second - square_intersection