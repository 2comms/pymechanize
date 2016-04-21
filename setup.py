import os
from setuptools import setup

DESC_1 = """Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize."""

DESC_2 = """
pymechanize is python3 enabled version of John Lee's python2 mechanize project.
pymechanize.Browser implements the urllib.OpenerDirector interface.  Browser
objects have state, including navigation history, HTML form state, cookies,
etc.  The set of features and URL schemes handled by Browser objects is
configurable.  The library also provides an API that is mostly compatible with
urllib: your urllib program will likely still work if you replace "urllib"
with "pymechanize" everywhere.

Features include: ftp:, http: and file: URL schemes, browser history, hyperlink
and HTML form support, HTTP cookies, HTTP-EQUIV and Refresh, Referer [sic]
header, robots.txt, redirections, proxies, and Basic and Digest HTTP
authentication.

Much of the code originally derived from Perl code by Gisle Aas (libwww-perl),
Johnny Lee (MSIE Cookie support) and last but not least Andy Lester
(WWW::Mechanize).  urllib was written by Jeremy Hylton.

"""

VERSION = open(os.path.join("pymechanize", "version.py")).\
    readlines()[0].strip(' "\n')

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: BSD License
License :: OSI Approved :: Zope Public License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Internet
Topic :: Internet :: File Transfer Protocol (FTP)
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Browsers
Topic :: Internet :: WWW/HTTP :: Indexing/Search
Topic :: Internet :: WWW/HTTP :: Site Management
Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Testing
Topic :: Software Development :: Testing :: Traffic Generation
Topic :: System :: Archiving :: Mirroring
Topic :: System :: Networking :: Monitoring
Topic :: System :: Systems Administration
Topic :: Text Processing
Topic :: Text Processing :: Markup
Topic :: Text Processing :: Markup :: HTML
Topic :: Text Processing :: Markup :: XML
"""

test_requirements = ['nose', 'rednose', 'coverage']

setup(
    name="pymechanize",
    version=VERSION,
    license="BSD",  # or ZPL 2.1
    platforms=["any"],
    classifiers=[c for c in CLASSIFIERS.split("\n") if c],
    install_requires=['lxml>=3.4.4', 'BeautifulSoup4>=4.4.1'],
    author="John J. Lee",
    author_email="jjl@{nospam}pobox.com",
    maintainer="Bright Dadson",
    maintainer_email="brightdadson@{nospam}gmail.com",
    description=DESC_1,
    long_description="{0}\n{1}".format(DESC_1, DESC_2),
    url="https://github.com/2comms/pymechanize",
    packages=["pymechanize"],
    tests_require=test_requirements,
    setup_requires=test_requirements,
    test_suite='nose.collector',
)
