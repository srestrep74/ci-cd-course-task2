"""
This module provides basic arithmetic operations.
"""


# app/calculadora.py
def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: La suma de los dos números.
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: La resta de los dos números.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        float: El producto de los dos números.
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): El numerador.
        b (float): El denominador.

    Returns:
        float: El cociente de los dos números.

    Raises:
        ZeroDivisionError: Si el denominador es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
