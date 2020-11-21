#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Extension
import sys


with open('README.rst') as readme_file:
    readme = readme_file.read()


requirements = ['cffi', 'numpy', 'pandas', 'matplotlib']
setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest']


ext_modules = []

if '--with-extension' in sys.argv:
    ext_modules.append(Extension(
        'darshan.extension',
        #optional=True,
        sources=['darshan/extension.c'],
        library_dirs=['/usr/lib64/atlas/', '/usr/lib/atlas'],
        include_dirs=['/usr/include'],
        libraries=['darshan-util']
        ))
    sys.argv.remove('--with-extension')



#ext_modules.append(Extension(
#    'darshan.extension',
#    #optional=True,
#    sources=['darshan/extension.c'],
#    library_dirs=['/usr/lib64/atlas/', '/usr/lib/atlas'],
#    include_dirs=['/usr/include'],
#    libraries=['darshan-util']
#    ))




setup(
    author='',
    author_email='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
#        'Programming Language :: Python :: 3.4',
#        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Python tools to interact with darshan log records of HPC applications.",
    #long_description=readme,
    long_description="PyDarshan",

    #options={"bdist_wheel": {"universal": False}},
    
    
    ext_modules = ext_modules,
    
    install_requires=requirements,
    include_package_data=True,
    keywords='darshan',
    name='darshan',
    packages=find_packages(include=['darshan*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://www.mcs.anl.gov/research/projects/darshan/',
    version='0.0.2',
    zip_safe=False,
)
