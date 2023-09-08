@book_store_login
Feature: Validamos registrar nuevo usuario

@login
Scenario:Validar rellenar formalario de nuevo usuario
    Given Ingresamos a la url "URL_QA"
    When cargue la pagina, damos click al boton "book store"
    And damos click al boton 'login'
    And damos click al boton 'new user'
    And ingresamos los datos del formalario '<login>'
    And damos click al boton registrar
    And validamos que usuario este ingresado