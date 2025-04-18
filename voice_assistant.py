import os
from gtts import gTTS

class VoiceAssistant:
    def __init__(self, word, ID):
        self.word = word
        self.ID = ID
        self.create_voice_file(self.word, ID)

    def create_voice_file(self, word, ID):
        filename = f"voice_database\\voice_{ID}.mp3"

        if os.path.exists(filename):
            self.play_voice(filename)
        else:
            tts = gTTS(word)
            tts.save(filename)
            self.play_voice(filename)

    def play_voice(self, file_path):
        if os.name == "nt":  # For Windows
            os.system(f"start {file_path}")
        elif os.name == "posix":  # For macOS/Linux
            os.system(f"afplay {file_path}" if os.system("which afplay") == 0 else f"mpg123 {file_path}")