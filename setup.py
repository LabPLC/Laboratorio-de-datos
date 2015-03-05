from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-labplc',
    version=version,
    description="Open data for Laboratorio para la Ciudad at Mexico",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='No\xc3\xa9 Dom\xc3\xadnguez Porras',
    author_email='noe@codeandomexico.org',
    url='https://github.com/LabPLC/Laboratorio-de-datos',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.labplc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.labplc.plugin:PluginClass
        ckanext-labplc=ckanext.labplc.plugin:labplcPlugin
        labplc_controller = ckanext.labplc.controller:LabplcController

    ''',
)
