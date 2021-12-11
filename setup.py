from setuptools import setup
from setuptools import find_packages

import pyetf.etfdb
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyetfdb",
    version="0.1.0",
    author="Jakub Pluta",
    author_email="plutakuba@gmail.com",
    description="ETF screening tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JakubPluta/pyetf/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "requests",
        "pytest",
        "bs4",
        "pandas",
        "aiohttp",
        "async_retrying",
        "aiohttp-retry"

    ],
)