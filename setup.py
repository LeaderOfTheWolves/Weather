from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='Weather',
    version='1.0.0',
    description='Get Weather Of Your City',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='LeaderOfTheWolves',
    author_email='ImLeaderOfTheWolves@gmail.com',
    url="https://github.com/LeaderOfTheWolves/Weather",
    packages=['weather'],
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ]
)
