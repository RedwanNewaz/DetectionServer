import setuptools
import pathlib

import pkg_resources
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="detection_server",
    version="0.0.1",
    author="RedwanNewaz",
    author_email="redwan06me@gmail.com",
    description="A simple flask server to communicate with deep learning module",
    long_description="Send some input images to your deep learning module via http network and return high level information",
    long_description_content_type="text/markdown",
    url="https://github.com/RedwanNewaz/DetectionServer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=install_requires,
)