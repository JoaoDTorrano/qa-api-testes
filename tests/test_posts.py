import pytest

CAMPOS_DO_POST = {"userId", "id", "title", "body"}

NOVO_POST = {"title": "Post de teste", "body": "Conteudo do post de teste", "userId": 1}


def test_tc01_listar_posts_retorna_200_e_100_itens(api):
    resp = api.get("/posts")
    assert resp.status_code == 200
    assert len(resp.json()) == 100


def test_tc02_listar_posts_responde_em_json(api):
    resp = api.get("/posts")
    assert "application/json" in resp.headers["Content-Type"]


def test_tc03_buscar_post_existente_tem_os_campos_esperados(api):
    resp = api.get("/posts/1")
    assert resp.status_code == 200
    corpo = resp.json()
    assert set(corpo) == CAMPOS_DO_POST
    assert corpo["id"] == 1


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_tc04_buscar_post_devolve_o_id_pedido(api, post_id):
    resp = api.get(f"/posts/{post_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == post_id


def test_tc05_buscar_post_inexistente_retorna_404(api):
    resp = api.get("/posts/9999")
    assert resp.status_code == 404


def test_tc06_filtrar_por_usuario_retorna_so_posts_dele(api):
    resp = api.get("/posts", params={"userId": 1})
    assert resp.status_code == 200
    posts = resp.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


def test_tc07_comentarios_do_post_pertencem_ao_post(api):
    resp = api.get("/posts/1/comments")
    assert resp.status_code == 200
    comentarios = resp.json()
    assert len(comentarios) > 0
    assert all(comentario["postId"] == 1 for comentario in comentarios)


def test_tc08_criar_post_retorna_201_e_devolve_os_dados_enviados(api):
    resp = api.post("/posts", json=NOVO_POST)
    assert resp.status_code == 201
    corpo = resp.json()
    assert "id" in corpo
    for campo, valor in NOVO_POST.items():
        assert corpo[campo] == valor


def test_tc09_atualizar_post_retorna_200_e_devolve_os_dados_enviados(api):
    dados = {"id": 1, **NOVO_POST}
    resp = api.put("/posts/1", json=dados)
    assert resp.status_code == 200
    corpo = resp.json()
    assert corpo["id"] == 1
    assert corpo["title"] == NOVO_POST["title"]


def test_tc10_remover_post_retorna_200(api):
    resp = api.delete("/posts/1")
    assert resp.status_code == 200


def test_tc11_listagem_responde_em_menos_de_2_segundos(api):
    resp = api.get("/posts")
    assert resp.elapsed.total_seconds() < 2
