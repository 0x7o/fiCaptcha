import os
import pyttsx3

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
                cache_dir: str = "c",
                lang: str = "ru"):
        
        self.bitrate = bitrate
        self.count = count
        self.noise_bg = noise_bg
        self.noise_dir = noise_dir
        self.random_speed = random_speed
        self.cache_dir = cache_dir
        self.dict = dict
        self.captcha = None

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

        engine = pyttsx3.init()
        engine.setProperty('voice', lang) 
        for d in dict:
            engine.save_to_file(f"{d['text']}", f"{self.cache_dir}/{d['num']}.wav")
            engine.runAndWait()

    def generate(self):
        ...