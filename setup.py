import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open("README.rst", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='openspin',
    version='0.0.1',
    description='Spinorama measurements of your speaker',
    long_description=long_description,
    packages=['openspin'],
    url='https://github.com/Pietzaalberg/OpenSpin',
    author='Piet Zaalberg',
    author_email='additaudio@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='frequency impulse response audio spectrum equalizer arduino hardware',
    entry_points={
        'gui_scripts': ['hifiscan=hifiscan.app:main']
    },
    python_requires=">=3.8",
    install_requires=['eventkit', 'numpy', 'PyQt6', 'pyqtgraph',
                      'sounddevice']
)
