import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read contents of a text file
    >>> read("health_stream", "VERSIONS")
    '0.0.1'
    >>> read("README.md")
    ...
    """
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


setup(
    name="health_stream",
    version="0.1",
    author="himanshu.singh@nyu.edu",
    description="Health stream",
    long_description=read("README.md"),
    long_description_content_type="text/md",
    packages=find_packages(exclude=["tests", ".github"]),
)
