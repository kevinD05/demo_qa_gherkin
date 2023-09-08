@Elements_Links
Feature: Validamos escenario Links

@links
Scenario:Validar dar click en los links
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "Links"
    And daremos click a todos los links 
    Then Validaremos el mensaje de la consola despues de a ver dado click en los links