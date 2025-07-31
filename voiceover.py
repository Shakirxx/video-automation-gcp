import os
from gtts import gTTS

def generate_voiceover(script_text):
    output_path = "voice.mp3"
    tts = gTTS(script_text)
    tts.save(output_path)
    return output_path

