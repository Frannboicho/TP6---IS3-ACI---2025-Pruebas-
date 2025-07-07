# features/steps/math_steps.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from behave import given, when, then
from math_functions import suma, cuadrado, cuadrado_binomio

# Steps para suma
@given('tengo los números {a:d} y {b:d}')
def step_given_numeros(context, a, b):
    context.a = a
    context.b = b

@when('ejecuto la función suma')
def step_when_suma(context):
    context.resultado = suma(context.a, context.b)

# Steps para cuadrado
@given('tengo el número {x:d}')
def step_given_numero(context, x):
    context.x = x

@when('ejecuto la función cuadrado')
def step_when_cuadrado(context):
    context.resultado = cuadrado(context.x)

# Step común
@then('el resultado debe ser {esperado:d}')
def step_then_resultado(context, esperado):
    assert context.resultado == esperado