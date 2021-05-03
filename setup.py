import os
from codecs import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(
        os.path.join(here, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8"
) as fp:
    long_description = fp.read()

version_contents = {}
with open(os.path.join(here, "accept", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(
    name="paymob.accept",
    version=version_contents["VERSION"],
    description="Python client for the Paymob.accept API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Muhammed Shokr",
    author_email="mohamedshokr@paymob.com",
    url="https://github.com/Shokr/paymob.accept",
    license="MIT",
    keywords="Paymob Accept api payments",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=['requests', ],
    python_requires='>=3',
    project_urls={
        "Documentation": "https://docs.paymob.com/",
        "Source Code": "https://github.com/Shokr/paymob.accept",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
