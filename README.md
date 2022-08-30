# Desafio-SoftFocus

Desafio apresentado pela SoftFocus com o intuito de realizar um CRUD de comunicações de perda, que faz parte do Sistema ProAgro Fácil.

### Tela Inicial

Na tela inicial encontra-se uma listagem das comunicações de perda cadastradas no banco, onde são apresentadas suas principais informações. 

Ao digitar algum valor na barra de pesquisa, serão filtradas apenas as comunicações de perda que contém o CPF do produtor digitado na busca.

Após a listagem encontra-se um botão que deve ser clicado quando se deseja cadastrar uma nova comunicação de perda.

Além disso, ao clicar sobre algum nome de produtor presente na listagem, será aberto um formulário para realizar alterações nos campos da comunicação de perda selecionada.

### Tela de Cadastro

Todos os dados devem ser devidamente preenchidos para proceder com o cadastro de uma nova comunicação de perda. Após o cadastro, o usuário é redirecionado à Tela Inicial.

Há uma situação específica em que a veracidade dos fatos é avaliada, que ocorre quando se deseja inserir uma comunicação e ao menos uma outra já se encontra cadastrada no banco com a mesma data, menos de 10 km entre elas e os eventos são diferentes. Nesse caso, será apresentada uma mensagem indicando tal situação e caso o usuário concorde com a veracidade dos fatos pode salvar a nova comunicação de perda.

### Tela de Atualização

Qualquer campo pode ter seu valor alterado e em seguida, deve ser confirmada a atualização por meio do botão salvar, que irá realizar as devidas alterações no banco de dados e redirecionar o usuário para a Tela Inicial.
Além disso, há um botão para exclusão da atual comunicação de perda, o qual irá redirecionar para uma tela de confirmação.

### Tela de confirmação de exclusão

Os dados da comunicação de perda que se deseja excluir são apresentados e ao clicar no botão Excluir, ela será excluída do banco de dados e o usuário será redirecionado para a Tela Inicial.

### Ambiente de desenvolvimento

As linguagens e frameworks utilizados são:
  - Python
  - Django
  - HTML
  - Bootstrap
  
Após inseridos, os dados são armazenados no SGDB PostgreSQL.
