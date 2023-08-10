@widgets_auto_complate
Feature: Validamos auto complate

Scenario:Validar botones de alerta
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Widgets"
    And damos click al boton 'Auto Complete'
    And damos click en el campo multiple color
    And escribiremos dos nombre de un color 'yellow','red'
    And damos click en el campo single color
    And escribiremos un nombre de un color 'blue'
    Then Validamos que al escribir nombres de colores se auto complete