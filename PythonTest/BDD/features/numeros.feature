# Archivo: numeros.feature

Feature: Determinar si un número es par o impar

  Scenario: Verificar si un número par retorna True
    Given un número par como entrada
    When evaluando si es par
    Then el resultado debería ser True

  Scenario: Verificar si un número impar retorna False
    Given un número impar como entrada
    When evaluando si es par
    Then el resultado debería ser False
