# -*- coding: utf-8 -*-
import sys
import os
import glob
from setuptools import setup, find_packages


_MAJOR               = 0
_MINOR               = 0
_MICRO               = 1
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)

metainfo = {
    'authors': {
        'Cokelaer':('Thomas Cokelaer','thomas.cokelaer@pasteur.fr'),
        },
    'version': version,
    'license' : 'BSD',
    'download_url' : ['http://pypi.python.org/pypi/bioconvert'],
    'url' : ['http://pypi.python.org/pypi/bioconvert'],
    'description':'Access to Biological Web Services from Python' ,
    'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
    "keywords": ["NGS", "bam2bed", "fastq2fasta"],
    'classifiers' : [
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Physics']
    }

with open('README.rst') as f:
    readme = f.read()

#from distutils.core import setup, Extension
#sequence = Extension('sequence', sources=['biokit/sequence/sequence.c'])

setup(
    name             = 'bioconvert',
    version          = version,
    maintainer       = metainfo['authors']['Cokelaer'][0],
    maintainer_email = metainfo['authors']['Cokelaer'][1],
    author           = metainfo['authors']['Cokelaer'][0],
    author_email     = metainfo['authors']['Cokelaer'][1],
    long_description = readme,
    keywords         = metainfo['keywords'],
    description      = metainfo['description'],
    license          = metainfo['license'],
    platforms        = metainfo['platforms'],
    url              = metainfo['url'],
    download_url     = metainfo['download_url'],
    classifiers      = metainfo['classifiers'],

    zip_safe=False,
    packages = find_packages(),
    install_requires = open('requirements.txt').read().split(),

     # This is recursive include of data files
    exclude_package_data = {"": ["__pycache__"]},

    package_data = {
        '': ['*.csv'],
        'bioconvert.data' : ['*'],
        },

    entry_points = {
        'console_scripts':[
           'converter=bioconvert.scripts.bioconvert:main'
        ]
    }

#    ext_modules=[
#        Extension('biokit.sequence.complement', 
#                sources=['biokit/sequence/cpp/complement.c', ],
#                 )
#        
#        ],

    )
