@Elements_web_tables
Feature:Validamos escenario radio button

@web_table
Scenario: Validar que se envien los datos del formulario, editar datos del formulario, eliminar datos del formulario
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "Elements"
    And damos click al boton "web tables"
    And daremos click en el boton 'add'
    And ingresamos los datos del formulario del usuario
    And daremos click en el boton "submit"
    And daremos click en el espacio de busqueda 
    And ingresamos el nombre que asignamos al guarda los datos del formulario
    And daremos click en el boton editar
    And editaremos el formulario
    And daremos click en el submit
    And daremos click en el boton eliminar
    Then Validamos que se envien los datos del formulario y que tambien se editen y se eliminen