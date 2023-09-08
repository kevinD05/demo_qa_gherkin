@Elements_text_box
Feature: Validamos escenario text box

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



