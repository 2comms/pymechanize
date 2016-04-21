from urllib.error import URLError, HTTPError
# ...and from pymechanize
from .auth import HTTPProxyPasswordMgr, HTTPSClientCertMgr
from .debug import HTTPResponseDebugProcessor, HTTPRedirectDebugProcessor
# crap ATM
# # from _gzip import \
# #      HTTPGzipProcessor
from .urllib_fork import (AbstractBasicAuthHandler,
     AbstractDigestAuthHandler, BaseHandler, CacheFTPHandler,
     FileHandler, FTPHandler, HTTPBasicAuthHandler,
     HTTPCookieProcessor, HTTPDefaultErrorHandler,
     HTTPDigestAuthHandler, HTTPErrorProcessor, HTTPHandler,
     HTTPPasswordMgr, HTTPPasswordMgrWithDefaultRealm,
     HTTPRedirectHandler, ProxyBasicAuthHandler, ProxyDigestAuthHandler,
     ProxyHandler, UnknownHandler)
from .http import (HTTPEquivProcessor, HTTPRefererProcessor,
     HTTPRefreshProcessor, HTTPRobotRulesProcessor, RobotExclusionError)

import http.client as httplib
if hasattr(httplib, 'HTTPS'):
    from .urllib_fork import HTTPSHandler

del httplib
from .opener import (OpenerDirector, SeekableResponseOpener,
                     build_opener, install_opener, urlopen)

from .request import Request
