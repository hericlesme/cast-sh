import os

from setuptools import find_packages
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_requirements(req_file):
    """Read requirements file and return packages and git repos separately"""
    requirements = []
    dependency_links = []
    lines = read(req_file).split("\n")
    for line in lines:
        if line.startswith("git+"):
            dependency_links.append(line)
        else:
            requirements.append(line)
    return requirements, dependency_links


REQ_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")
core_reqs, core_dependency_links = get_requirements(
    os.path.join(REQ_DIR, "requirements.txt")
)
dev_extras = read(os.path.join(REQ_DIR, "dev_requirements.txt")).split("\n")
tests_require = ["pytest", "flake8"]


setup(
    name="cast",
    version="0.1.0",
    author="Héricles Emanuel",
    description=("An instance of your terminal in your browswe"),
    license="Apache-2.0",
    keywords=("shell terminal browser" "web web-shell"),
    packages=find_packages(exclude=["docs", "examples", "dist"]),
    include_package_data=True,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/tunl/cast-sh",
    install_requires=core_reqs,
    extras_require={
        "dev": dev_extras,
    },
    dependency_links=core_dependency_links,
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["cast-sh=cast.__main__:main"]},
    package_data={
        "cast": ["login.html", "404.html", "app.css", "app.js", "index.html"]
    },
    tests_require=tests_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
