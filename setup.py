from setuptools import setup, find_packages

setup(
    name="cleanmydata",  # Name of the package
    version="0.1.0",     # Initial version
    description="A data cleaning library for text processing",
    long_description=open('README.md').read(),  # Readme file
    long_description_content_type="text/markdown",
    url="https://github.com/pranavnbapat/cleanmydata",  # GitHub repository URL
    author="Pranav Bapat",
    author_email="pranav.g33k@gmail.com",
    license="MIT",  # License type
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "numpy==2.0.2",
        "pandas==2.2.3",
        "spacy==3.8.2",
        "langdetect==1.0.9",
        "bs4==0.0.2",
        "lxml==5.3.0",
    ],
    python_requires="==3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
