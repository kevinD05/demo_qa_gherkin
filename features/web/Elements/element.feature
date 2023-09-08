Feature: Validamos ingresa a la web Demoqa

    @element
    Scenario: Ingresamos al modulo Elementos de la web Demoqa
        Given Ingresamos a la url "URL_QA" 
        When cargue la pagina, damos click al boton "Elements"
        Then validos que nos mande a las opcions de elementos
