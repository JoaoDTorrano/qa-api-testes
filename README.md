# qa-api-testes

Testes de API feitos com **pytest** e **Postman** sobre uma API pública de exemplo, a [JSONPlaceholder](https://jsonplaceholder.typicode.com). É um projeto de estudo de QA: o objetivo é praticar planejamento, escrita de casos de teste, automação e relato de defeitos.

## O que é testado

O recurso `/posts` e os comentários de um post (`/posts/{id}/comments`):

- listagem, busca por id, filtro por usuário e id inexistente;
- criação, atualização e remoção;
- formato da resposta (JSON e campos esperados) e tempo de resposta.

A lista completa está em [docs/casos-de-teste.md](docs/casos-de-teste.md).

> A JSONPlaceholder simula escrita: `POST`, `PUT` e `DELETE` respondem como se funcionassem, mas nada é gravado. Por isso os testes de escrita verificam o contrato da resposta (status e dados devolvidos), não a persistência.

## Como rodar

Pré-requisitos: Python 3.10 ou superior.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

No Windows, ative o ambiente com `.venv\Scripts\activate`.

Para testar outro ambiente da mesma API, defina a variável `API_BASE_URL`:

```bash
API_BASE_URL=http://localhost:3000 pytest
```

### Postman

1. Importe `postman/jsonplaceholder-posts.postman_collection.json`.
2. Rode a coleção pelo Collection Runner, ou pelo terminal com o [Newman](https://www.npmjs.com/package/newman):

```bash
npx newman run postman/jsonplaceholder-posts.postman_collection.json
```

## Estrutura

```
tests/       testes automatizados em pytest
postman/     coleção do Postman com os mesmos cenários
docs/        plano de teste, casos de teste e modelo de relato de bug
```

## Documentação

- [Plano de teste](docs/plano-de-teste.md)
- [Casos de teste](docs/casos-de-teste.md)
- [Modelo de relato de bug](docs/modelo-relato-de-bug.md)

## Status

Em andamento. Próximos passos: testes de interface com Selenium e testes de front-end com Jest.
