# Casos de teste

Os IDs correspondem aos nomes dos testes em `tests/test_posts.py` e aos itens da coleção do Postman.

| ID | Cenário | Passos | Resultado esperado | Automação |
|---|---|---|---|---|
| TC01 | Listar posts | `GET /posts` | Status 200 e 100 itens | pytest e Postman |
| TC02 | Formato da listagem | `GET /posts` | Cabeçalho `Content-Type` com `application/json` | pytest e Postman |
| TC03 | Buscar post existente | `GET /posts/1` | Status 200, campos `userId`, `id`, `title` e `body`, com `id` igual a 1 | pytest e Postman |
| TC04 | Buscar posts de ids diferentes | `GET /posts/{id}` com id 1, 50 e 100 | Status 200 e `id` igual ao pedido | pytest |
| TC05 | Buscar post inexistente | `GET /posts/9999` | Status 404 | pytest e Postman |
| TC06 | Filtrar por usuário | `GET /posts?userId=1` | Status 200 e todos os posts com `userId` igual a 1 | pytest e Postman |
| TC07 | Comentários de um post | `GET /posts/1/comments` | Status 200 e todos os comentários com `postId` igual a 1 | pytest e Postman |
| TC08 | Criar post | `POST /posts` com título, corpo e `userId` | Status 201, `id` presente e dados enviados devolvidos | pytest e Postman |
| TC09 | Atualizar post | `PUT /posts/1` com os dados completos | Status 200 e dados enviados devolvidos | pytest |
| TC10 | Remover post | `DELETE /posts/1` | Status 200 | pytest e Postman |
| TC11 | Tempo de resposta | `GET /posts` | Resposta em menos de 2 segundos | pytest e Postman |

## Ideias para ampliar

- Enviar `POST` sem campos obrigatórios e observar a resposta.
- Enviar `PUT` para um id inexistente.
- Testar `GET /posts?userId=` com valor inválido.
- Comparar o comportamento da API com a documentação do site.
