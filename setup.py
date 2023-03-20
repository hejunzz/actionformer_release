from setuptools import setup, find_packages

setup(name='actionformer', 
        version='0.1', 
        packages=find_packages(exclude=('configs', 'data', 'ckpt')))
