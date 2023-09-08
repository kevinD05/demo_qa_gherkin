@Elements_Radio_button
Feature:Validamos escenario radio button

@radio_button
Scenario: Validar botones del Radio button
  Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "Radio button"
    And daremos click en el boton "yes"
    And daremos click en el boton "Impressive"
    Then Validamos que al dar click en los botones estos se muestren en el mensaje de la consola