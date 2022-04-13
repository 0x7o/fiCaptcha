import time
import random
from ficaptcha.generate import Captcha

c = Captcha((256, 256), "images", "grey", count_images=random.randint(2, 5), rotate_im=False)
c.generate()
c.save("t.txt", 'base64')