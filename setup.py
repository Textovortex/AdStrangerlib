from os.path import abspath, dirname, join
from setuptools import setup
from adventurelib import __version__


ROOT = abspath(dirname(__file__))


with open(join(ROOT, "README.md")) as fd:
    README = fd.read()

setup(
    name='adstrangerlib',
    description='Easy text adventures',
    long_description=README,
    long_description_content_type="text/markdown",
    version=__version__,
    author='Daniel Pope and LEHAtupointow',
    author_email='mauve@mauveweb.co.uk/pezleha@gmail.com',
    url='https://github.com/leha-code/adstrangerlib',
    project_urls={
        'Documentation': 'https://adventurelib.readthedocs.io/'
    },
    py_modules=['adstrangerlib'],
    extras_require={
        ':python_version < "3.3"': [
            'backports.shutil_get_terminal_size>=1.0.0',
        ],
    },
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ]
)
