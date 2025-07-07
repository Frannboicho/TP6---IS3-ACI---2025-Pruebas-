Feature: Función suma
  Como usuario
  Quiero sumar dos números
  Para obtener el resultado correcto

  Scenario: Sumar números positivos
    Given tengo los números 2 y 3
    When ejecuto la función suma
    Then el resultado debe ser 5

  Scenario: Sumar números negativos
    Given tengo los números -2 y 3
    When ejecuto la función suma
    Then el resultado debe ser 1