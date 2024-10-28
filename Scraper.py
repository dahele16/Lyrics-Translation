from bs4 import BeautifulSoup
import requests 
import json

def main():
    print("Entering Scraper main")
    response = requests.get('https://genius.com/Adele-hello-lyrics') 
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser') 
    lyrics_div = soup.find_all("div", {"data-lyrics-container": "true"})
    # Extract the lyrics text
    lyrics = ''
    for div in lyrics_div:
        lyrics += div.get_text(separator='\n')
    print(lyrics)



def get_lyrics(path):
    lyrics = ""
    response = requests.get(path)
    if response.status_code == 200: 
        print(response)
        soup = BeautifulSoup(response.content, 'html.parser') 
        lyrics_div = soup.find_all("div", {"data-lyrics-container": "true"})
        # Extract the lyrics text
        for div in lyrics_div:
            lyrics += div.get_text(separator='\n')
        return lyrics
    else:
        return lyrics
if __name__ == "__main__":
    main()