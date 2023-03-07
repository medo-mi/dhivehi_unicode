from setuptools import setup, find_packages

VERSION = '1.0.3'
DESCRIPTION = 'Python Dhivehi (Thaana) ASCII, accent to unicode converter'
#LONG_DESCRIPTION = 'Python package to convert Dhivehi (Thaana) ASCII and accent text to Unicode'

# Setting up

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="dhivehi_unicode",
    version=VERSION,
    author="Mohamed Ismail (medo)",
    author_email="<modeissey@gmail.com>",
    description=DESCRIPTION,
    url="https://github.com/medo-mi/dhivehi_unicode",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['Dhivehi', 'Thaana'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)