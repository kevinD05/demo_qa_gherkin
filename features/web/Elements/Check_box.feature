@Elements_check_box
Feature: Validamos escenario check box

@check_box
Scenario:Validar las check boxes de la pestaña check box
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "check box"
    And damos clic en boton "+"
    And damos click a las check box
    And damos clic en el boton "-"
    Then Validamos que al dar click en las check box estas se muestren seleccionadas
