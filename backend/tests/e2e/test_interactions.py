import httpx

def test_get_interactions_returns_200(client: httpx.Client) -> None:
    # Добавляем / в конце, чтобы избежать 307 редиректа
    response = client.get("/interactions/") 
    assert response.status_code == 200

def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
    # Добавляем / в конце
    response = client.get("/interactions/")
    assert isinstance(response.json(), list)