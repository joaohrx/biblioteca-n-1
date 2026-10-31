# Biblioteca n+1
Componentes:
- Edson Félix dos Santos
- João Pedro de Oliveira Silva
- João Victor Rocha dos Santos

Dividimos nossas responsabilidades de acordo com o modelo MVC. Edson será responsável pela seção de Controller, João Pedro pelo Model e João Victor pelo View.

A Biblioteca n+1 é um website com um sistema moderno de gerenciamento de livros, permitindo que usuários cadastrados realizem empréstimos e devoluções de livros. Além disso, é possível cadastrar, editar e excluir novos livros, bem como visualizar seus livros emprestados e o nome de usuário no Perfil.

## Sistema, entidades e relacionamentos

### Sistema

A Biblioteca n+1 é uma aplicação web desenvolvida em Flask, organizada segundo o padrão MVC. O sistema permite o gerenciamento de livros e autores, além do cadastro de leitores e da realização de empréstimos e devoluções.
Entre suas funcionalidades estão autenticação de usuários, consulta ao acervo, visualização de detalhes, cadastro, edição e exclusão de livros e visualização de perfil.

### Entidades e atributos

O banco de dados possui três entidades principais:

**Livro**

| Atributo | Tipo | Restrição |
|---|---|---|
| `id` | Integer | PK |
| `titulo` | String(50) | — |
| `ano` | Integer | — |
| `emprestado` | Boolean | Default: False |
| `genero` | String(50) | — |
| `descricao` | String(100) | — |
| `autor_id` | Integer | FK de `autores.id` |

**Autor**

| Atributo | Tipo | Restrição |
|---|---|---|
| `id` | Integer | PK |
| `nome` | String(50) | UNIQUE |

**Leitor**

| Atributo | Tipo | Restrição |
|---|---|---|
| `id` | Integer | PK |
| `nome` | String(100) | UNIQUE |
| `email` | String(100) | UNIQUE |
| `senha_hash` | Text | — |

### Relacionamentos

**Autor–Livro (1:N)**
Um autor pode possuir vários livros, enquanto cada livro está associado a um único autor. A relação é implementada pela chave estrangeira `autor_id`, presente na tabela `livros`, que referencia `autores.id`.

**Leitor–Livro (N:N)**
Um leitor pode estar associado a vários livros, assim como um livro pode estar associado a vários leitores. A relação é implementada por uma tabela associativa:

**Tabela `leitores_livros`**
| Atributo | Tipo | Restrição |
|---|---|---|
| `leitor_id` | Integer | PK composta; FK para `leitores.id` |
| `livros_id` | Integer | PK composta; FK para `livros.id` |

A chave primária composta (`leitor_id`, `livros_id`) impede a duplicação de uma mesma associação entre leitor e livro.

## Instruções para instalar dependências
Para instalar as dependências, abra o terminal do projeto, crie um ambiente virtual usando `python -m venv venv`e em seguida digite `venv\Scripts\Activate.ps1`.
Após isso, instale as dependências com `pip install -r requirements.txt`.

## Instruções para criar o banco
Para criar o banco de dados e popular o sistema com os livros pré-definidos, execute o comando `python init_db.py`.

## Instruções para executar o sistema
Tendo seguido os passos anteriores, para executar o sistema digite no terminal o comando `python app.py` e abra o endereço indicado pelo Flask no navegador.

## Declaração de autoria e uso de IA
Declaro que desenvolvi este projeto compreendendo o código entregue e que sou capaz de explicar e modificar suas partes principais.
Uso de IA:
[ ] Não utilizei IA generativa.
[X] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.
Descrição do uso, se houver:
Utilizamos a IA pontualmente na estilização das páginas (CSS) e na resolução de dúvidas gerais na programação.