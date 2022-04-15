import os
import pyttsx3
import uuid

class Captcha():
    def __init__(self,
                bitrate: int = (44000),
                count: int = 3,
                noise_bg: bool = True,
                noise_dir: str = None,
                random_speed: bool = True,
                dict: list = [{'num': 0, 'text': 'ноль'},
                              {'num': 1, 'text': 'один'},
                              {'num': 2, 'text': 'два'},
                              {'num': 3, 'text': 'три'},
                              {'num': 4, 'text': 'четыре'},
                              {'num': 5, 'text': 'пять'},
                              {'num': 6, 'text': 'шесть'},
                              {'num': 7, 'text': 'семь'},
                              {'num': 8, 'text': 'восемь'},
                              {'num': 9, 'text': 'девять'},],
                audio_dir: str = "",
                lang: str = "ru",
                audio_synthesis: bool = False):
        
        self.bitrate = bitrate
        self.count = count
        self.noise_bg = noise_bg
        self.noise_dir = noise_dir
        self.random_speed = random_speed
        self.audio_dir = audio_dir
        self.audio_synthesis = audio_synthesis
        self.dict = dict
        self.captcha = None

        if self.audio_synthesis:
            if not os.path.exists(self.audio_dir):
                os.makedirs(self.audio_dir)

            engine = pyttsx3.init()
            engine.setProperty('voice', lang) 
            for d in dict:
                if not os.path.exists(f"{self.audio_dir}/{d['num']}"):
                    os.makedirs(f"{self.audio_dir}/{d['num']}")
                engine.save_to_file(f"{d['text']}", f"{self.audio_dir}/{d['num']}/{str(uuid.uuid4())}.wav")
                engine.runAndWait()

    def generate(self):
        ...