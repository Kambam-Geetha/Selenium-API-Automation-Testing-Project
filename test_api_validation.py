import requests

def test_api_status():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    assert "userId" in response.json()
