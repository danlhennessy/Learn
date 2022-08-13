from setuptools import setup

setup(
    name='helloworld',  #  The name used when pip installing (pip install helloworld)
    version='0.0.1',
    description='Test say hello func',
    py_modules=["helloworld"],
    package_dir={'': 'src'}
)