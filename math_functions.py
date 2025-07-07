# math_functions.py
def suma(a, b):
    """Suma dos valores enteros."""
    return a + b

def cuadrado(x):
    """Calcula el cuadrado de un valor entero."""
    return x * x

def cuadrado_binomio(a, b):
    """Calcula el cuadrado de un binomio: (a + b)² = a² + 2*a*b + b²"""
    return suma(suma(cuadrado(a), cuadrado(b)), 2 * a * b)