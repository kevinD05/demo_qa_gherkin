@Alerts_frame_Modal_Dialogs
Feature: Validamos escenario modal dialogs

@modal
Scenario:Validar botones de alerta
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Alerts, Frame & Windows"
    And damos click al boton 'modal dialogs' 
    And damos click en el boton 'small modal'
    And cerraremos la alerta emergente
    And damos click en el click 'Large modal'
    And cerraremos la alerta emergente
    Then Validamos que al dar click en los botones la alerta sea visible