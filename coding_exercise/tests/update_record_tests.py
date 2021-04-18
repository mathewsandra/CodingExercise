import requests

def test_update_song_check_status_equals_200():
    body = {
		"songName":"HarryPotterMusic",
		"seconds":120
	}

    response = requests.patch("http://0.0.0.0:3000/updateRecord/song/4",json=body)
    print(response)
    assert response.status_code == 200

def test_update_audiobook_check_status_equals_200():
    body = {

		"audiobookTitle":"sunshine",
		"author":"AR Rahman",
		"narrator": "Junior",
		"seconds":60
	
    }
    response = requests.patch("http://0.0.0.0:3000/updateRecord/audiobook/3",json=body)
    print(response)
    assert response.status_code == 200

def test_update_podcast_check_status_equals_200():
    body = {

		"podcastName":"Life",
		"seconds":180,
		"host": "Jay Shetty",
		"participants": ["Sandra","Mathew"]
	}


    response = requests.patch("http://0.0.0.0:3000/updateRecord/podcast/2",json=body)
    print(response)
    assert response.status_code == 200

def test_update_record_check_status_equals_400():
    body = {
		"podcastName":"Life",
		"seconds":3,
		"host": "Jay Shetty",
		"participants": ["Sandra","Mathew"]
	}

    response = requests.patch("http://0.0.0.0:3000/updateRecord/dance/1",json=body)
    print(response)
    assert response.status_code == 400