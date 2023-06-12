from setuptools import setup, find_packages
import codecs, os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Get Minecraft Forge download URLs.'
LONG_DESCRIPTION = 'A package to get Forge latest and recommended download URLs.'

setup(
    name="forgepy",
    version=VERSION,
    author="matejmajny",
    author_email="<matejmajny@duck.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["requests", "bs4"],
    keywords=['python', "minecraft", "forge", "API"],
)