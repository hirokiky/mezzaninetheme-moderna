import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


setup(
    name='mezzaninetheme-moderna',
    version='1.0',
    url='https://github.com/hirokiky/mezzaninetheme-moderna',
    description='Mezzanine CMS themes: Moderna',
    long_description=README,
    author='Hiroki Kiyohara',
    author_email='hirokiky@gmail.com',
    license='MIT',
    packages=['moderna'],
)
