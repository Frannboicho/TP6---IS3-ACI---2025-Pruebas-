# test_math_functions.py
import pytest
from math_functions import suma, cuadrado, cuadrado_binomio

# PRUEBAS UNITARIAS - FUNCIÓN SUMA (Integrante 1)
def test_suma_numeros_positivos():
    assert suma(2, 3) == 5

def test_suma_numeros_negativos():
    assert suma(-2, 3) == 1

# PRUEBAS UNITARIAS - FUNCIÓN CUADRADO (Integrante 2)  
def test_cuadrado_numeros_positivos():
    assert cuadrado(2) == 4

def test_cuadrado_numeros_negativos():
    assert cuadrado(-3) == 9

# PRUEBAS UNITARIAS - FUNCIÓN CUADRADO_BINOMIO (Integrante 3)
def test_cuadrado_binomio_basico():
    assert cuadrado_binomio(2, 3) == 25

def test_cuadrado_binomio_con_negativos():
    assert cuadrado_binomio(-2, 3) == 1

# PRUEBA DE INTEGRACIÓN
def test_integracion_cuadrado_binomio():
    """Verifica que cuadrado_binomio usa correctamente suma y cuadrado"""
    a, b = 3, 4
    resultado = cuadrado_binomio(a, b)
    esperado = suma(suma(cuadrado(a), cuadrado(b)), 2 * a * b)
    assert resultado == esperado
    assert resultado == 49