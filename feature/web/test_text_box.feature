Feature: Validamos escenario text box

 @test_text_box
    Scenario: ingresar al modulo text box 
       Given ingresamos a la url 
       When cargue la pagina, damos click al boton text box
       Then validar que nos mande el formulario de la text box


@test_text_box2
   Scenario: Rellenar un formulario
      Given que estoy en la página de registro
      When ingresar full name "usuario123"
      And ingresar email "usuario@example.com"
      And ingresar current addres 
      And ingresar permanet addres
      and dar clic en el boton submit
      Then esperar que todo se haya aguardado