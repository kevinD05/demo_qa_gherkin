@widgets_data_picker
Feature: Validamos data picker

@data
Scenario:Validar data picker
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Widgets"
    And damos click al boton 'data picker'
    And damos click en el campo 'select date'
    And seleccionamos la fecha '08/18/2023'
    And damos click en el campo 'date and time'
    And seleccionamos la fecha y hora 'August 18, 2023 11:30 PM'
    Then Validamos que al seleccionar una hora y fecha se refleje en los campos correspodiente