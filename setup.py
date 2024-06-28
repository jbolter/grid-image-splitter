from setuptools import setup
setup(
    name='splitter',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'splitter=splitter:main'
        ]
    }
)