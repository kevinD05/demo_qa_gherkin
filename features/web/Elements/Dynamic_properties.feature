@Elements_Dynamic_properties
Feature: Validamos escenario Dynamic_properties

@dynamic
Scenario:Validar dar click en los links
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "Dynamic properties"
    And damos click al boton "color change"
    And esperaremos 5 segundos hasta que el boton 'will enable 5 seconds sea visible y daremos click'
    And damos click en el boton "visible after 5 seconds" despues de 5 segundos
    Then Validamos que al dar click en los botones el cortono cambie
