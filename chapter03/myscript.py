def my_add(x, y):
    """두 수를 더한다."""
    out = x + z # 버그 : 변수 z가 정의되지 않았다.
    return out + y
