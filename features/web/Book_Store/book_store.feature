@book_store
Feature: Validamos registrar

Scenario:Validar rellenar formalario de nuevo usuario
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "book store application"
    And damos click al boton 'book store'
    And damos click al boton 'login'
    And ingresamos el user y password correspondiente '<user>'
    And damos click al boton 'login'
    And damos click al libro con el nombre ' Working Introduction'
    And damos click al boton 'add to your collection'
    And damos click al libro con el nombre 'Harnessing the Power of the Web'
    And damos click al boton 'add to your collection'
    Then Validamos que los libros se guarden en nuestro perfil
