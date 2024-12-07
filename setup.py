from setuptools import setup, find_packages

setup(
    name="ds_toolkit",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package implementing core data structures and algorithms.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ARAVIND281/ds_toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
