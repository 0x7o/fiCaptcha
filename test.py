import time
from ficaptcha.generate import Captcha

c = Captcha((256, 256), "images", "grey", count_images=0, rotate_im=False)