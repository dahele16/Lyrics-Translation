import GeniusAPI
from Song import Song
import Scraper
import translator
class System:
    def __init__(self):
        pass
    def run(self): 
        song_name = input("Do a search: ")
        songs = GeniusAPI.find_song(song_name)
        print("Choose an option from 1 to 5")
        for i,song in enumerate(songs, start=1):
            print(f"{i} {song.title}")
        print("0.Do another search?")
        option = int(input())
        print(option)
        if option in range(1,6):
            print(songs[option - 1])
            language = input("Input code language: ")
            path = "https://genius.com" + songs[option - 1].lyrics_path
            print(path)
            lyrics = Scraper.get_lyrics(path)
            print(lyrics)
            translated_lyrics = translator.get_lyrics_translated(lyrics, language)
            print(translated_lyrics)

