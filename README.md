# Desafio Galeria de Fotos de Casamento

https://app-casamento-renan.herokuapp.com/login

Esse codigo foi desenvolvido para resolver a seguinte situação

## Galeria de Amigos

*Você recebeu um pedido de um amigo para criar uma galeria para seu casamento onde seus amigos poderão fazer upload de suas fotos e ele terá uma galeria unificada com todas as fotos de amigos.
Ele deseja aprovar as fotos antes de ficarem visíveis para todos. Ele e sua esposa devem ser os únicos capazes de aprovar novas fotos.
Os usuários devem ser capazes de curtir fotos e adicionar comentários às fotos.
Por favor, crie um site que atenda às suas necessidades. Você deve usar python no back-end, com qualquer framework de sua escolha, bem como para o front-end.*

*Detalhes da solução*
1. *A resolução deve ser uma aplicação web responsiva.*
2. *Deve-se fornecer todas as informações necessárias para testar a aplicação.*
3. *A aplicação precisa rodar.*
4. *O código precisa ser hospedado em seu repositório de código preferido.*
5. *Você precisa hospedar a aplicação em um servidor de sua escolha e nos fornecer um link para acessar e usar o aplicativo.*
6. *Você deve fornecer evidências suficientes de que sua solução está completa, indicando, no mínimo, que ela funciona corretamente em relação aos requisitos.*


Backend construido em Python utilizando o framework Flask.

Frontend HTML e CSS com Bootstrap 4.

Banco de Dados flask_sqlalchemy Sqlite.

Aplicação responsiva para dispositivos móveis.


## Informação para testar a aplicação

### Usuários no Banco de dados, todos com a senha **12345**
1. *ana.gomes* (admin)
2. *pedro.gomes* (admin)
3. *joao.silva*
4. *renan.aquino*

Podem ser criados novos usuário.

Podera rodar diretamente no navegador, hospedado na plataforma Heroku:
https://app-casamento-renan.herokuapp.com/login
ou poderar clonar esse repositório e rodar localmente.


1. Caso o usuário não possua cadastro ele pode se registrar informando nome, nome de usuário e senha, o nome de usuário deve ser único e será usado para fazer o login.
2. Na página principal o usuário pode ver as fotos já aprovadas pelos noivos, comentar e curtir, há opção de enviar uma nova foto onde deve ser selecionada uma imagem no formato png, jpg ou jpeg.
3. Ao submeter uma imagem ela é salva no banco de dados mas não fica visivel até a aprovação de um dos administradores.
4. Se quem compartilha a imagem for um dos noivos a imagem é automaticamente postada.
5. Os noivos podem a qualquer momento ocultar uma imagem.
6. Todos os usuários podem curtir e retirar sua curtida da foto.
7. Todos os usuários podem comentar e apagar o seu comentário.
8. Caso usuário não esteja autenticado e deseje acessar a página principal é exibido um template personalizado com link para a pagina de login.
9. Caso seja digitado uma rota inexistente é exibido um template personalizado com link para a pagina inicial.

## CAPTURAS DE TELA WEB
![01](https://user-images.githubusercontent.com/49573650/134098132-21eb1183-64e4-44fc-a9f1-a7c018a27628.JPG)
![02](https://user-images.githubusercontent.com/49573650/134098135-05ebf29a-56e8-48d1-8548-1149e4ad68cc.JPG)
![03](https://user-images.githubusercontent.com/49573650/134098138-4cf29c23-849b-44c2-8312-9bfb8a6fdcae.JPG)
![04](https://user-images.githubusercontent.com/49573650/134098141-382ac0b2-722b-4b0c-9e73-5dd60e5e1de8.JPG)


## CAPTURAS DE TELA SMARTPHONE
![01 (1)](https://user-images.githubusercontent.com/49573650/134098148-66790709-964c-4841-a971-46fe093f4642.jpg)
![01 (2)](https://user-images.githubusercontent.com/49573650/134098146-54861691-988c-47fb-a24e-16cd3ac462b0.jpg)
![01 (3)](https://user-images.githubusercontent.com/49573650/134098147-3ed95f04-f220-4a27-b988-98602bc118e7.jpg)
![01 (4)](https://user-images.githubusercontent.com/49573650/134098311-da6e6ec0-3517-4e9e-815b-ea7b98f78909.jpg)

