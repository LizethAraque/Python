# Archivo: steps.py

from behave import given, when, then
from numeros import es_numero_par

@given('un número par como entrada')
def step_un_numero_par(context):
    context.numero = 4

@given('un número impar como entrada')
def step_un_numero_impar(context):
    context.numero = 5

@when('evaluando si es par')
def step_evaluando_si_es_par(context):
    context.resultado = es_numero_par(context.numero)

@then('el resultado debería ser True')
def step_verificar_si_es_par(context):
    assert context.resultado is True

@then('el resultado debería ser False')
def step_verificar_si_es_impar(context):
    assert context.resultado is False
