def test_get_existing_candidate_returns_json(client):
    response = client.get("/api/candidates/1")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "id": 1,
        "name": "Alice Sharma",
        "email": "alice@example.com",
    }


def test_get_missing_candidate_returns_json_404(client):
    response = client.get("/api/candidates/9999")

    assert response.status_code == 404
    assert response.is_json
    assert response.get_json() == {"error": "candidate not found"}
