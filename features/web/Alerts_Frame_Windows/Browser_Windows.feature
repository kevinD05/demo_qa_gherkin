@alert_frame_windows
Feature: Validamos escenario browser windows

@browser
Scenario:Validar botones de new tab, new windows, new windows message
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Alerts, Frame & Windows"
    And damos click al boton 'Browser Windows'
    And damos click en el boton 'New tab'
    And damos click en el boton 'new windows'
    And damos click en el boton 'New windows message'
    Then Validamos que al darle click en los botones seamos rediccionadosa una nueva ventana
