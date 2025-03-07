# OpenAPI_Test

Esse arquivo aqui tem como objetivo a informar os passos que foram realizados para conseguir instalar o Swagger e executar ele a fim de gerar a documentação de forma automática com base no código fonte analisado pela ferramenta.

## Etapa Principal

1. Instalação do módulo com o comando `pip3 install flasgger`.
2. Instanciação, existem duas formas de se utilizar o flasgger, uma delas é com o módulo Swagger e a outra é a swag_from.
    1. Caso seja escolhida a forma do Swagger, a documentação será através de docstrings dentro do método/função da api.
    2. Caso a forma escolhida seja o swag_from, deve ser criado um dacorator antes do método.
    3. Em ambos os casos, no nosso documento main.py tem exemplos para eles.
3. Após isto, e iniciarmos nossa API, poderemos acessar nossa documentação através da url http://localhost:3030/apidocs