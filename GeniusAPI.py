import requests
import api_keys
import json
from Song import Song 

my_token = api_keys.genius_key

def main():
    term = input("song: ")
    songs = find_song(term)
    for song in songs:
        print(song)

def find_song(search_term):
    #Do api request
    songs_found = []
    genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={my_token}"
    response = requests.get(genius_search_url)
    json_data = response.json()
    #print(json.dumps(response.json(), indent=2))
    if json_data["meta"]["status"] == 200:
        hits = json_data["response"]["hits"]
        for hit in hits[:5]:
            song_info = hit["result"]
            song = Song(
                            id=song_info["id"],
                            title=song_info["full_title"],
                            artist=song_info["artist_names"],
                            lyrics_path=song_info["path"],  # Assuming path to lyrics on Genius
                            picture_path=song_info["header_image_url"]
                        )
            songs_found.append(song)
                # Print or store the information        
        return songs_found
    else:
        return {}


if __name__ == "__main__":
    main()