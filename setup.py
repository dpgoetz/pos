from setuptools import setup, find_packages

from pos import __version__ as version

name = "pos"

setup(
    name = name,
    version = version,
    author = "David Goetz",
    author_email = "david.goetz@rackspace.com"
    description = "Poppy On Swift",
    license = "Apache License, (2.0)",
    keywords = "openstack poppy swift middleware",
    url = "http://github.com/dpgoetz/pos",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 0 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[],
    entry_points={
        'paste.filter_factory': [
            'pos=pos.middleware:filter_factory',
            ],
        },
    )
