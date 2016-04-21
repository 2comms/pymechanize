"""Integration with Python standard library module urllib2: Request class.

Copyright 2004-2006 John J Lee <jjl@pobox.com>

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD or ZPL 2.1 licenses (see the file
COPYING.txt included with the distribution).

"""

import logging
from . import rfc3986, sockettimeout
from . import urllib_fork

warn = logging.getLogger("pymechanize").warning

class Request(urllib_fork.Request):
    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False, visit=None,
                 timeout=sockettimeout._GLOBAL_DEFAULT_TIMEOUT):

        if not rfc3986.is_clean_uri(url):
            warn("url argument is not a URI "
                 "(contains illegal characters) %r" % url)
        urllib_fork.Request.__init__(self, url, data, headers)
        self.selector = None
        self.visit = visit
        self.timeout = timeout

    def __str__(self):
        return "<Request for %s>" % self.get_full_url()
