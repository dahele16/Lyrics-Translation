import deepl
import api_keys

def main():
    ...


def get_lyrics_translated(lyrics, language):
    translated_lyrics = ""
    auth_key = api_keys.deepl_key
    translator = deepl.Translator(auth_key)
    translated_lyrics = translator.translate_text(lyrics, target_lang=language)
    print(translated_lyrics)
    #for original, translated in zip(lyrics, translated_lyrics):
        #print(f"Original: {original} | Translated: {translated}")


if __name__ == "__main__":
    main()
