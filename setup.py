from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='Various pre-commit hooks',
    url='https://github.com/jeremylow/pre-commit-hooks',
    version='0.0.1',

    author='Jeremy Low',
    author_email='jeremy@iseverythingstilltheworst.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        # None so far
    ],
    entry_points={
        'console_scripts': [
           'check-inline-doc-spacing = hooks.check_inline_doc_spacing:main',
        ],
    },
)
