# Steps para suma
@given('tengo los números {a:d} y {b:d}')
def step_given_numeros(context, a, b):
    context.a = a
    context.b = b

@when('ejecuto la función suma')
def step_when_suma(context):
    context.resultado = suma(context.a, context.b)
