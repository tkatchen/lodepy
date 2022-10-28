from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Fully python multi-node automation project'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="lodepy",
        version=VERSION,
        author="Tyler Katchen",
        author_email="tkatchen7@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'ci', 'cd'],
        classifiers= [
            "Programming Language :: Python :: 3",
        ]
)
