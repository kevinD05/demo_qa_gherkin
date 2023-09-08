@Alerts_frame_alerst
Feature: Validamos escenario Alerts

@alert
Scenario:Validar botones de alerta
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Alerts, Frame & Windows"
    And damos click al boton 'Alerts'
    And damos click en el boton 'click button to see alert'
    And damos click en el boton 'alert will appear after 5 seconds'
    And damos click en el boton 'confirm box will appear'
    And damos click en el boton 'prompt box will appear'
    Then Validamos que al dar click en los botones surgan las alertas correspondiente
