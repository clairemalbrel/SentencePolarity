from setuptools import find_packages
from setuptools import setup
REQUIRED_PACKAGES = [
    'gcsfs==0.6.0',
    'google-cloud-storage==1.26.0',
    'pandas==0.24.2',
    'stemming',
    'nltk',
    'setuptools',
    'scrapy',
    'vaderSentiment',
    'scikit-learn']
PACKAGE_NAME='SentencePolarity'                        # model folder name
PACKAGE_DESCRIPTION='SentencePolarity python 3 claire'     # model folder name
setup(name=PACKAGE_NAME,
    version='1.0',
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.data", "*.csv", "*.txt", "*.tff", "*.classifier", 'lexicon'],
        # And include any *.msg files found in the "hello" package, too:
        #"hello": ["*.msg"],
    },
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description=PACKAGE_DESCRIPTION)
