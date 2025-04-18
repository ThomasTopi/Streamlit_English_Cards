"""File for loading words into voice.mp3 from database"""
from gtts import gTTS
import os
from english_words import get_english_word, data_size

class VoiceAssistant:
    def __init__(self, word, ID):
        self.word = word
        self.ID = ID
        self.create_voice_file(self.word, ID)

    def create_voice_file(self, word, ID):
        filename = f"voice_database\\voice_{ID}.mp3"

        if os.path.exists(filename):
            return
        else:
            tts = gTTS(word)
            tts.save(filename)

def main():
    size = data_size()
    for i in range(1,size+1):
        VoiceAssistant(get_english_word(i), i)
    print(f"All phrases loaded. Full database contains {size} phrases.")

if __name__=="__main__":
    main()