**Para rodar o programa instale os requerimentos contidos em requeriments.txt**

Para criar o back-end usei o Flask

Para iniciar, primeiro inicialize o banco de dados do teste 4 localizado na pasta 'Database' no servidor local.

O app esta configurado para usar o root e nenhuma senha, para alterar basta modificar a linha 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:'Senha Aqui'@localhost/teste_4' caso o root possua alguma senha de acesso

Com o database carregado e inicializado rode o app.py

Apos rodar o app.py e iniciar o servidor, digite 'cd frontend' para irmos para pasta frontend

Apos isso digite 'npm run serve'

Isso fara com que a pagina Vue seja inicializada.

A pagina possui uma home page,

Um método Get para pegar todo o banco de dados,

E um metodo post para enviar uma busca textual pelo banco de dados, retornando qualquer semelhança em qualquer coluna com a palavra digitada.

**Caso o servidor do banco de dados nao estiver ativo, as consultas nao funcionarão**

A coleção no postman será compartilhada com o mesmo email que enviarei o link para o github.
