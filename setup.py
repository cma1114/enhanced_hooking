from setuptools import setup, find_packages

setup(
    name='enhanced_hooking',
    version='0.1',
    py_modules=['enhanced_hooking'],
    description='Custom transformer hooks',
    long_description=open('README.md').read(),
    author='Christopher Ackerman',
    url='https://github.com/cma1114/enhanced_hooking',
    install_requires=[
        'torch>=2.2.0'
    ],
)