'''oracle_eloqua'''

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='oracle_eloqua',
    version='0.0.2',
    description='Python hooks for Oracle Eloqua API',
    long_description=readme,
    packages=find_packages(),
    author='Nick Gryga',
    author_email='nickolasgryga@gmail.com'
)


