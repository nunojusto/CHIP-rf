from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chip-rf',
    version='0.0.1',
    author='Nuno Justo',
    author_email='nuno@justoweb.com',
    description='This is a port for CHIP from the amazing module rpi-rf for sending and receiving 433/315MHz signals with low-cost GPIO RF modules on a Raspberry Pi',
    long_description=long_description,
    url='https://github.com/nunojusto/chip-rf',
    license='BSD',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=[
        'chip',
        'chip computer',
        'chip ntc',
        'rf',
        'gpio',
        'radio',
        '433',
        '433mhz',
        '315',
        '315mhz'
    ],
    scripts=['scripts/chip-rf_send', 'scripts/chip-rf_receive'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)
