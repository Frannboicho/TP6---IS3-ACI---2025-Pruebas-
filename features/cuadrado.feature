Feature: Función cuadrado
  Como usuario
  Quiero calcular el cuadrado de un número
  Para obtener x²

  Scenario: Cuadrado de número positivo
    Given tengo el número 4
    When ejecuto la función cuadrado
    Then el resultado debe ser 16

  Scenario: Cuadrado de número negativo
    Given tengo el número -3
    When ejecuto la función cuadrado
    Then el resultado debe ser 9