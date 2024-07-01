from setuptools import setup, find_packages

setup(
    name='just_commit',
    version='0.1.0',
    author='EXTREMOPHILARUM',
    author_email='example@example.com',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'just_commit = just_commit.main:main',
        ],
    },
)
