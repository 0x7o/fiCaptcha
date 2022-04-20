import os
import pyttsx3
import random
import wave
from pydub import AudioSegment
import uuid

def audio_plus_audio(infiles, outfile):
    '''
    This function takes in a list of files and adds them together to form a single file.
    :param infiles: A list of files to be added together.
    :param outfile: The file to which the output is to be written.
    :return: The name of the file to which the output is written.
    '''
    data = []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

    return outfile

def noise_aud(audio, noise, out, rate):
    '''
    Adds noise to an audio file.
    :param audio: The audio file.
    :param noise: The noise file.
    :param out: The output file.
    :param rate: The frame rate of the audio file.
    :return: The output file.
    '''
    audio1 = AudioSegment.from_file(audio, frame_rate=rate)
    noise1 = AudioSegment.from_file(noise, frame_rate=rate)

    combined = audio1.overlay(noise1)
    combined.export(out, format='wav')

    return out

class Captcha():
    def __init__(self,
                rate: int = (44000),
                count: int = 3,
                noise_bg: bool = True,
                noise_dir: str = None,
                tmp_dir: str = "tmp",
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
        
        '''
        Initializes the class with the given parameters.
        :param rate: The sampling rate of the audio.
        :param count: The number of digits in the captcha.
        :param noise_bg: Whether to add background noise or not.
        :param noise_dir: The directory containing the background noise.
        :param tmp_dir: The directory to store temporary files.
        :param dict: The dictionary containing the mapping of numbers to words.
        :param audio_dir: The directory to store the audio files.
        :param audio_synthesis: Whether to generate audio files or not.
        '''

        self.rate = rate
        self.count = count
        self.noise_bg = noise_bg
        self.noise_dir = noise_dir
        self.tmp_dir = tmp_dir
        self.audio_dir = audio_dir
        self.audio_synthesis = audio_synthesis
        self.dict = dict
        self.captcha = None

        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)

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
        '''
        Generates a random captcha from the dictionary of possible characters.
        :return: A dictionary containing the captcha and its corresponding string.
        '''
        captchs = []
        for u in range(self.count):
            captchs.append(random.choice(self.dict)['num'])

        cls = os.listdir(self.audio_dir)
        aud = {}
        for cl in cls:
            if cl != self.noise_dir:
                aud[cl] = os.listdir(f"{self.audio_dir}/{cl}")

        files = []
        res = ""
        for cap in captchs:
            res += str(cap)
            files.append(f"{self.audio_dir}/{cap}/{random.choice(aud[str(cap)])}")
        
        step = audio_plus_audio(files, f"{self.tmp_dir}/{str(uuid.uuid4())}.wav")

        if self.noise_bg:
            noisef = []
            for i in os.listdir(f"{self.audio_dir}/{self.noise_dir}"):
                noisef.append(i)
            noisef = random.choice(noisef)

            h = noise_aud(step, f"{self.audio_dir}/{self.noise_dir}/{noisef}", f"{self.tmp_dir}/{str(uuid.uuid4())}.wav", self.rate)
        
        self.captcha = h
        return {'num': res}

    def save(self, path, format):
        '''
        Saves the captcha as a wav file.
        :param path: The path where the file is to be saved.
        :param format: The format of the file to be saved.
        :return: The path where the file is saved.
        '''
        sound = AudioSegment.from_file(self.captcha, frame_rate=self.rate)
        sound.export(path, format=format)
        
        try:
            os.remove(self.tmp_dir)
        except PermissionError:
            pass

        self.captcha = None
        return path