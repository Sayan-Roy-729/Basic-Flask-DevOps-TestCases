from app import app

def test_get_api_endpoint():
    with app.test_client() as c:
        response = c.get("/api/DemoApiEndpoint")
        json_response = response.get_json()
        assert json_response == {"message": "This is a response from a GET request."}
        assert response.status_code == 200

def test_post_api_endpoint():
    with app.test_client() as c:
        response = c.post("/api/DemoApiEndpoint", json={
            "name": "Sayan"
        })
        json_response = response.get_json()
        assert json_response == {"message": "Nice to meet you, Sayan!"}
        assert response.status_code == 200