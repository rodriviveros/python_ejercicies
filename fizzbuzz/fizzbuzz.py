import math 

def fizzbuzz(num):
    """Devuelve una palabra según la divisibilidad de un entero.

    Evalúa si `num` es 0 o múltiplo de 3 y 5, solo de 3, o solo de 5.
    Si no cumple ninguna condición, devuelve el mismo número.

    Args:
        num (int): Número entero a evaluar.

    Returns:
        str | int: "fizzbuzz" si num es 0 o múltiplo de 3 y 5,
        "fizz" si es múltiplo de 3, "buzz" si es múltiplo de 5,
        o `num` sin modificar en cualquier otro caso.

    Examples:
        >>> fizzbuzz(6)
        'fizz'
        >>> fizzbuzz(10)
        'buzz'
        >>> fizzbuzz(15)
        'fizzbuzz'
        >>> fizzbuzz(0)
        'fizzbuzz'
        >>> fizzbuzz(8)
        8
    """
    if num == 0:
        return "fizzbuzz"
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    return num