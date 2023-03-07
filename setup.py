from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = 'Python Dhivehi (Thaana) ASCII, accent to unicode converter'
LONG_DESCRIPTION = 'Python package to convert Dhivehi (Thaana) ASCII and accent text to Unicode'

# Setting up
setup(
    name="dhivehi_unicode",
    version=VERSION,
    author="Mohamed Ismail (medo)",
    author_email="<modeissey@gmail.com>",
    description=DESCRIPTION,
    url="git@github.com:medo-mi/dhivehi_unicode.git"
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
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