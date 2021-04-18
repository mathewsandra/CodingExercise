import requests

def test_create_song_check_status_equals_200():
    body = {
	"audioFileType":"song",
	"audioFileMetadata":{
		"songName":"ashiki33",
		"seconds":3
	}

    }
    response = requests.post("http://0.0.0.0:3000/createRecord",json=body)
    print(response)
    assert response.status_code == 200

def test_create_audiobook_check_status_equals_200():
    body = {
	"audioFileType":"audiobook",
	"audioFileMetadata":{
		"audiobookTitle":"sunshine",
		"author":"ar rahman",
		"narrator": "fhg",
		"seconds":3
	}

    }
    response = requests.post("http://0.0.0.0:3000/createRecord",json=body)
    print(response)
    assert response.status_code == 200

def test_create_podcast_check_status_equals_200():
    body = {
	"audioFileType":"podcast",
	"audioFileMetadata":{
		"podcastName":"Life",
		"seconds":3,
		"host": "Jay Shetty",
		"participants": ["Sandra","Mathew"]
	}

    }
    response = requests.post("http://0.0.0.0:3000/createRecord",json=body)
    print(response)
    assert response.status_code == 200

def test_create_record_check_status_equals_400():
    body = {
	"audioFileType":"dance",
	"audioFileMetadata":{
		"podcastName":"Life",
		"seconds":3,
		"host": "Jay Shetty",
		"participants": ["Sandra","Mathew"]
	}

    }
    response = requests.post("http://0.0.0.0:3000/createRecord",json=body)
    print(response)
    assert response.status_code == 400