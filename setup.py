from setuptools import find_packages, setup

setup(
    name='cleanmydata',
    packages=find_packages(include=['cleanmydata']),
    version='1.0.3',
    description='Library for data cleaning operations',
    author='Pranav Bapat',
    keywords=['python', 'data cleaning', 'clean data'],
    license='MIT',
    install_requires=['pandas'],
)