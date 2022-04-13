from setuptools import setup

setup(name='ficaptcha',
      version='1.0',
      description='Simple captcha generation',
      packages=['ficaptcha'],
      author_email='me@0x7o.link',
      install_requires=['numpy', 'pillow'],
      zip_safe=False)