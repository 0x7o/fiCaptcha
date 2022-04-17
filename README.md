# fiCaptcha
Module for image-captcha generation

## Install
Build from source
```bash
git clone https://github.com/0x7o/fiCaptcha
cd fiCaptcha
pip install .
```

Python pip install
```bash
pip install ficaptcha
```
## Usage
#Image Captcha
Create a folder with images for captcha:
```bash
├── images
│   ├── toy
│       ├── toy1.png
│       ├── toy2.png
│       └── ...
│   └── fox
│       ├── fox1.png
│       ├── fox2.png
│       └── ...
```
Import the library and create a class
- ```size=(256, 256)``` - Captcha size in pixels
- ```image_dir="images"``` - Image folder for captcha
- ```background_color="white"``` - Background Color
- ```noise_bg=True``` - Background Color
```python

```
