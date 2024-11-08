from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ],
    },
    install_requires=install_requires,
    author="Adrian Ebert",
    author_email="adrian.ebert@fau.de",
    description="A simple math quiz game.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AdrianEbert-tensora/dsss_homework_2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
