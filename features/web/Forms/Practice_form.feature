@Forms_practice_forms
Feature: Validamos escenario practice forms

@forms
Scenario: Validar rellenar formulario correctamente del modulo practice forms
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Forms"
    And damos click al boton 'practice forms'
    And ingresamos los datos del formulario del usuario '<forms>'
    And damos click en boton de genero "Male"
    And damos click en el boton hobbies "sports"
    And damos click en el campo date of birth "5/8/23"
    And damos click en el campo select state seleccionamos 'Ncr'
    And damos click en el campo select city seleccionamos 'delhi'
    Then validamos que se envien los datos del formulario correctamente