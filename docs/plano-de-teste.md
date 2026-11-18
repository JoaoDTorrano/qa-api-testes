# Plano de teste

## Objetivo

Verificar se o recurso `/posts` da JSONPlaceholder responde conforme o esperado para consultas, criação, atualização e remoção, e registrar qualquer divergência encontrada.

## Escopo

**Dentro do escopo**

- `GET /posts`, `GET /posts/{id}` e `GET /posts?userId={id}`
- `GET /posts/{id}/comments`
- `POST /posts`, `PUT /posts/{id}` e `DELETE /posts/{id}`

**Fora do escopo**

- Outros recursos da API (`/users`, `/albums`, `/todos`, `/photos`)
- Testes de carga e de segurança
- Persistência dos dados, porque a API não grava as alterações

## Tipos de teste

| Tipo | O que verifica |
|---|---|
| Funcional | Status e dados devolvidos em cada operação |
| Contrato | Campos esperados e formato JSON |
| Negativo | Comportamento com id inexistente |
| Desempenho básico | Tempo de resposta da listagem abaixo de 2 segundos |

## Ferramentas

- pytest e requests, para a automação
- Postman e Newman, para os testes exploratórios e a coleção

## Ambiente

API pública `https://jsonplaceholder.typicode.com`, acessada pela internet. O endereço pode ser trocado com a variável `API_BASE_URL`.

## Critérios

**Entrada:** a API responde ao acesso e as dependências estão instaladas.

**Saída:** todos os casos executados, com os que falharam registrados no modelo de relato de bug.

## Riscos

| Risco | Tratamento |
|---|---|
| API pública fora do ar ou lenta | Repetir a execução e registrar o horário da falha |
| Resultado de tempo de resposta variar com a rede | Usar um limite folgado e tratar falhas isoladas com cuidado |
| Dados de exemplo mudarem | Manter as verificações no contrato, não em textos específicos |

## Entregáveis

- Casos de teste em `docs/casos-de-teste.md`
- Testes automatizados em `tests/`
- Coleção do Postman em `postman/`
- Relatos de bug, quando houver, seguindo `docs/modelo-relato-de-bug.md`
