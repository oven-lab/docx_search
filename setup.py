from setuptools import find_packages, setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='docx_search',
    packages=find_packages(include=['docx_search']),
    version='1.0.1',
    description='A python library built to search for keywords in .docx files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='docx docx_search search',
    author='WaldemarBjornstrom',
    author_email='Waldemar.bjornstrom@unfnorrbotten.se',
    url='https://pypi.org/project/docx_search/',
    project_urls ={
    "Github": "https://github.com/WaldemarBjornstrom/docx_search",
    "Bug Tracker": "https://github.com/WaldemarBjornstrom/docx_search/issues",
    },

    license='GPL',
    classifiers=[
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
],
)