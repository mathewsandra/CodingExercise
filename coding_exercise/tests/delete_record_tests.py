import requests

def test_delete_song_check_status_equals_200():
    response = requests.delete("http://0.0.0.0:3000/deleteRecord/song/1")
    print(response)
    assert response.status_code == 200

def test_delete_audiobook_check_status_equals_200():
    response = requests.delete("http://0.0.0.0:3000/deleteRecord/audiobook/1")
    print(response)
    assert response.status_code == 200

def test_delete_podcast_check_status_equals_200():
    response = requests.delete("http://0.0.0.0:3000/deleteRecord/podcast/1")
    print(response)
    assert response.status_code == 200

def test_delete_record_check_status_equals_400():
    response = requests.delete("http://0.0.0.0:3000/deleteRecord/dance/1")
    print(response)
    assert response.status_code == 400