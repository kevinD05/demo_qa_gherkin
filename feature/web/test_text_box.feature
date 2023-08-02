Feature: Validamos escenario text box

  @test_text_box
  Scenario: Ingresar al módulo text box y Rellenar formulario
    Given ingresamos a la url
    When cargue la pagina, damos click al boton text box
    And mande el formulario de la text box
    And ingresar full name "usuario123"
    And ingresar email "usuario@example.com"
    And ingresar current address
    And ingresar permanent address
    And dar clic en el boton submit
    Then validar modulo text box y Rellenar formulario
