from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="json-to-ndjsonify",
    version="0.1.0",
    author="Mohammad Jaqmaqji",
    author_email="mohjak@gmail.com",
    description="A small package to convert JSON files to NDJSON (Newline Delimited JSON) format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohjak/json-to-ndjsonify",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'json-to-ndjsonify=json_to_ndjsonify.main:entry_point',
        ],
    },
)
