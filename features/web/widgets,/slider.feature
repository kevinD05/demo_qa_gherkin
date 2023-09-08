@widgets_slider
Feature: Validamos slider

@slider
Scenario:Validar mover el slider
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Widgets"
    And damos click al boton 'slider'
    And damos click al boton del slider
    And moveremos el slider hasta le numero 100
    Then Validamos el numero del recuadro del slider este debe ser 100