import time
import random
from ficaptcha.audio import Captcha

c = Captcha(audio_synthesis=False, audio_dir="audio", count=5, noise_dir="noise")
c.generate()
c.save("1.wav", "wav")