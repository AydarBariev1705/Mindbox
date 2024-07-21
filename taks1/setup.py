from setuptools import setup, find_packages

setup(
    name='shapes',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    tests_require=['unittest'],
    test_suite='tests',
    description='Library for calculating the area of shapes',
    author='Aydar Bariev',
    author_email='a_bariev@internet.ru',
)
