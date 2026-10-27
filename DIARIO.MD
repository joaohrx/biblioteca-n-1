# Diário - Biblioteca n+1

### Data: 13/10

**O que foi feito:** Estruturação básica: pastas, registro de Blueprints no Flask, arquivos.

**Dificuldade encontrada:** Nenhuma. Estruturação básica.

**Como resolvi:** Não houve dificuldade.

**Próximo passo:** CRUD básico.

---

### Data: 15/10 e 18/10

**O que foi feito:** Primeiras rotas de adicionar e buscar livro. Rotas de login, cadastro e logout

**Dificuldade encontrada:** Não informada.

**Como resolvi:** Não informado.

**Próximo passo:** Não informado.

---

### Data: 20/10 e 21/10

**O que foi feito:** A criação básica do banco de dados, com a criação das tabelas livros, autores e leitores. A tabela leitores_livros foi criada e todos os `relationship` foram feitos, com todos os relacionamentos. O arquivo `seed.py` foi deletado, pois não há utilidade para ele. Rotas de cadastro, login e logout também foram feitas.

**Dificuldade encontrada:** as tabelas não estavam sendo criadas.

**Como resolvi:** usei a função criar_banco no init.db.

**Próximo passo:** criar o crud e organizar os arquivos.

---

### Data: 21/10 (durante a aula)

**O que foi feito:** Um pequeno início da classe declarative (`Base`) e foi feita a classe `Usuario` e `Livro` com seus relacionamentos e atributos como nome, id, email, titulo, usuario_id etc.

**Dificuldade encontrada:** nenhuma.

**Como resolvi:** Não informado.

**Próximo passo:** estruturar o crud.

---

### Data: 22/10

**O que foi feito:** O arquivo `crud.py` foi criado e todos os testes foram feitos.

**Dificuldade encontrada:** nenhuma.

**Como resolvi:** Não informado.

**Próximo passo:** estruturar o crud.

---

### Data: 22/10

**O que foi feito:** Estruturação dos templates, criação do template-base, organização das rotas, integração com o Banco por meio do merge. No banco, o arquivo `crud.py` foi criado e todos os testes foram feitos. O arquivo `.gitignore` foi criado.

**Dificuldade encontrada:** Conflitos ocasionados pelo Merge e erros nos Blueprints.

**Como resolvi:** Corrigi o nome dos Blueprints e adaptei o código das rotas para se adequar à nomenclatura do Banco.

**Próximo passo:** Fazer os templates individuais e as consultas do CRUD.

### Data: 23/10

**O que foi feito:** funções de filtragem, adição e busca dentro do aquivo crud.py

**Dificuldade encontrada:** nenhuma.

**Como resolvi:** .

**Próximo passo:** terminar as outras filtagrem e buscas.


### Data: 27/10

**O que foi feito:** todas as buscas, filtragen, adição e edição foram adicionadas e testadas
**Dificuldade encontrada:** apagar o as informações da tabela auxiliar.

**Como resolvi:**  para resolver o problema, foi necessario usar o remove, pois como leitor armazena uma lista de livros
                    é necessario remover apenas aquele var para desfazer o relacionamento

**Próximo passo:** terminar as rotas.