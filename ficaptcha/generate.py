import os
import numpy as np
import random
from PIL import Image
from ficaptcha.process import noise

class Captcha():
    def __init__(self,
                size: tuple = (512,512),
                image_dir: str = None,
                background_color: str = "white",
                noise_bg: bool = True,
                noise_im: bool = True,
                rotate_im: bool = True,
                count_images: int = 5):
        self.image_dir = image_dir
        self.size = size
        self.background_color = background_color
        self.noise_bg = noise_bg
        self.noise_im = noise_im
        self.rotate_im = rotate_im
        self.count_images = count_images
        self.captcha = None


    def generate(self):
        cls = os.listdir(self.image_dir)
        class_i = []
        cache = []

        for c in cls:
            ca = os.listdir(f"{self.image_dir}/{c}")
            for p in ca:
                class_i.append([c, f"{self.image_dir}/{c}/{p}"])
        t = random.choice(class_i)

        bg = Image.new('RGBA', self.size, self.background_color)

        if self.noise_bg:
            bg = noise(bg, random.uniform(0.001, 1.0))

        isp = []

        for i in range(self.count_images - 1):
            v = random.choice(class_i)
            if v[0] in isp or v[0] == t[0]:
                pass
            else:
                isp.append(v[0])
                v = Image.open(v[1])
                v = v.resize((random.randint(40, 100), random.randint(40, 100)))

                if self.rotate_im:
                    v = v.rotate(random.randint(-360, 360), expand=True)

                if self.noise_im:
                    v = noise(v, random.uniform(0.001, 0.05))
            
                bg.paste(v, (random.randint(10, self.size[0] - 100), random.randint(10, self.size[1] - 100)))
            
        one = random.randint(10, self.size[0] - 100)
        two = random.randint(10, self.size[1] - 100)
        r = Image.open(t[1])
        r = r.resize((random.randint(40, 100), random.randint(40, 100)))
        if self.rotate_im:
            r = r.rotate(random.randint(-360, 360), expand=True)

        if self.noise_im:
            r = noise(r, random.uniform(0.001, 0.05))
        bg.paste(r, (one, two))
        
        self.captcha = bg

        return {"class": t[0], "file": t[1], "position": (one, two)}

    def save(self, path):
        if self.captcha != None:
            self.captcha.save(path)

"""
    
def add_salt_and_pepper(image, amount):
    output = np.copy(np.array(image))

    # add salt
    nb_salt = np.ceil(amount * output.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(nb_salt)) for i in output.shape]
    output[coords] = 1

    # add pepper
    nb_pepper = np.ceil(amount* output.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(nb_pepper)) for i in output.shape]
    output[coords] = 0

    return Image.fromarray(output)

def p(image):
    image = image.resize((random.randint(70, 180), random.randint(70, 180)))
    image = image.rotate(random.randint(-360, 360))
    return add_salt_and_pepper(image, random.uniform(0.001, 0.05))

bg = Image.new('RGB', (512, 512), 'grey')

v = Image.open("1.jpeg")
v = p(v)
bg = add_salt_and_pepper(bg, random.uniform(0.0, 1.0))
for i in range(5):
    bg.paste(p(v), (random.randint(1, 500), random.randint(1, 500)))
bg.save("2.png")

"""