from setuptools import setup, find_packages

setup(
    name='echorose',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'readability-lxml',
        'pyttsx3',
        # Add your other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'echorose=echorose.app:main',
        ],
    },
)
