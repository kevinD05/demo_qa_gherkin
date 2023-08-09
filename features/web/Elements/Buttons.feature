@Elements_buttons
Feature:Validamos escenario Buttons

Scenario: Validar botones del Radio button
  Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "Buttons"
    And daremos doble click en el boton 'double click me'
    And daremos click derecho en el boton ' right click'
    And daremos click en el boton 'click me'
    Then Validaremos los mensaje de la consola 