from setuptools import setup, find_packages

setup(
    name='just_commit',
    version='0.1.0',
    author='EXTREMOPHILARUM',
    author_email='example@example.com',
    description='A Python-based CLI tool designed to enhance the git command line experience',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/EXTREMOPHILARUM/just-commit',
    packages=find_packages(),
    install_requires=[
        'flake8',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
