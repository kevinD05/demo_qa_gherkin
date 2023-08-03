@Elements_text_box
Feature: Validamos escenario text box

  @test_text_box
  Scenario: Ingresar modulo text box y que se guarden los datos del formulario
    Given ingresamos a la url
    When cargue la pagina, damos click al boton text box
    And mande el formulario de la text box
    And ingresar full name "usuario123"
    And ingresar email "usuario@example.com"
    And ingresar current address
    And ingresar permanent address
    And dar click en el boton submit
    Then validamos que se envien los datos del formulario correctamente


  @test_text_box_1
  Scenario Outline: Validar enviar los datos del formulario correctamente del modulo Text Box
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "Text Box"
    And ingresamos los datos del formulario del usuario "<user>"
    Then validamos que se envien los datos del formulario correctamente
    Examples:
      | user  |
      | Kevin |
      | Luis  |
      | Pepe  |



  @test_text_box_2
  Scenario: Validar enviar los datos incorrectos en el formulario del modulo Text Box
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "Text Box"
    And ingresamos los datos incorrectos en el formulario
    Then validamos que al enviar datos incorrectos estos no se muestren en el mensaje de la consola