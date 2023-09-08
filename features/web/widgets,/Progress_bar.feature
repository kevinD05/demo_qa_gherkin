@widgets_Progress_Bar
Feature: Validamos Progress Bar

@progress_bar
Scenario:Validar que la barra de progresso llegue ala mitad
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Widgets"
    And damos click al boton 'Progress Bar'
    And damos click en el boton 'star'
    And esperemos que la barra de progresso llegue ala mitad y damos click en el boton 'stop'
    Then Validamos que la barra de progresso este %50