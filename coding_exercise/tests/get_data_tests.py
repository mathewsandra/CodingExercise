import requests

def test_get_specific_song_check_status_equals_200():
    response = requests.get("http://0.0.0.0:3000/getData/song/4")
    print(response)
    assert response.status_code == 200

def test_get_song_check_status_equals_200():
    response = requests.get("http://0.0.0.0:3000/getData/song")
    print(response)
    assert response.status_code == 200

def test_get_specific_audiobook_check_status_equals_200():
    response = requests.get("http://0.0.0.0:3000/getData/audiobook/3")
    print(response)
    assert response.status_code == 200

def test_get_audiobook_check_status_equals_200():
    response = requests.get("http://0.0.0.0:3000/getData/audiobook")
    print(response)
    assert response.status_code == 200

def test_get_specific_podcast_check_status_equals_200():
    response = requests.get("http://0.0.0.0:3000/getData/podcast/2")
    print(response)
    assert response.status_code == 200

def test_get_podcast_check_status_equals_200():
    response = requests.get("http://0.0.0.0:3000/getData/podcast")
    print(response)
    assert response.status_code == 200

def test_get_specific_record_check_status_equals_400():
    response = requests.get("http://0.0.0.0:3000/getData/dance/1")
    print(response)
    assert response.status_code == 400

def test_get_record_check_status_equals_400():
    response = requests.get("http://0.0.0.0:3000/getData/dance")
    print(response)
    assert response.status_code == 400