pymechanize: Stateful web browsing and scrapping in python
==========================================================

About
-----

`pymechanize` is python3 enabled version of John Lee's python2 mechanize project. `pymechanize` is a simple pythonic programmatic web browsing in Python, after Andy Lester’s Perl module `WWW::Mechanize`.

`pymechanize.Browser` and `pymechanize.UserAgentBase` implement the interface of `urllib.OpenerDirector` therefore any URL can be opened not just http.
`pymechanize.UserAgentBase` offers easy dynamic configuration of user-agent features like protocol, cookie, redirection and robots.txt handling,
without having to make a new OpenerDirector each time, e.g. by calling build_opener().
* Easy HTML form filling.
* Convenient link parsing and following.
* Browser history (.back() and .reload() methods).
* The Referer HTTP header is added properly (optional).
* Automatic observance of robots.txt.
* Automatic handling of HTTP-Equiv and Refresh.

## Example ##

.. code-block:: python

    import re
    import pymechanize

    br = pymechanize.Browser()
    br.open("http://www.example.com/")

    # follow second link with element text matching regular expression
    response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
    assert br.viewing_html()
    print br.title()
    print response1.geturl()
    print response1.info()  # headers
    print response1.read()  # body

    br.select_form(name="order")

    # Browser passes through unknown attributes (including methods)
    # to the selected HTMLForm.
    br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)

    # Submit current form.  Browser calls .close() on the current response on
    # navigation, so this closes response1
    response2 = br.submit()

    # print currently selected form (don't call .submit() on this, use br.submit())
    print br.form

    response3 = br.back()  # back to cheese shop (same data as response1)

    # the history mechanism returns cached response objects
    # we can still use the response, even though it was .close()d
    response3.get_data()  # like .seek(0) followed by .read()
    response4 = br.reload()  # fetches from server

    for form in br.forms():
        print form
        # .links() optionally accepts the keyword args of .follow_/.find_link()

    for link in br.links(url_regex="python.org"):
        print link
        br.follow_link(link)  # takes EITHER Link instance OR keyword args
        br.back()

You may control the browser’s policy by using the methods of `pymechanize.Browser’s` base class, `pymechanize.UserAgent`.
For example:

.. code-block:: python

    br = pymechanize.Browser()

    # Explicitly configure proxies (Browser will attempt to set good defaults).
    # Note the userinfo ("joe:password@") and port number (":3128") are optional.
    br.set_proxies({
        "http": "joe:password@myproxy.example.com:3128",
        "ftp": "proxy.example.com",
    })

    # Add HTTP Basic/Digest auth username and password for HTTP proxy access.
    # (equivalent to using "joe:password@..." form above)
    br.add_proxy_password("joe", "password")

    # Add HTTP Basic/Digest auth username and password for website access.
    br.add_password("http://example.com/protected/", "joe", "password")

    # Don't handle HTTP-EQUIV headers (HTTP headers embedded in HTML).
    br.set_handle_equiv(False)

    # Ignore robots.txt.  Do not do this without thought and consideration.
    br.set_handle_robots(False)

    # Don't add Referer (sic) header
    br.set_handle_referer(False)

    # Don't handle Refresh redirections
    br.set_handle_refresh(False)

    # Don't handle cookies
    br.set_cookiejar()

    # Supply your own pymechanize.CookieJar (NOTE: cookie handling is ON by
    # default: no need to do this unless you have some reason to use a
    # particular cookiejar)
    br.set_cookiejar(cj)

    # Log information about HTTP redirects and Refreshes.
    br.set_debug_redirects(True)

    # Log HTTP response bodies (ie. the HTML, most of the time).
    br.set_debug_responses(True)

    # Print HTTP headers.
    br.set_debug_http(True)

    # To make sure you're seeing all debug output:
    logger = logging.getLogger("pymechanize")
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.INFO)

Adjusting bad HTML response headers:

.. code-block:: python

    response = br.response()  # this is a copy of response
    headers = response.info()  # currently, this is a mimetools.Message
    headers["Content-type"] = "text/html; charset=utf-8"
    response.set_data(response.get_data().replace("<!---", "<!--"))
    br.set_response(response)

`pymechanize` exports the complete interface of `urllib` therefore when using `pymechanize`,
anything you would normally import from `urllib` should be imported from `pymechanize` instead.

.. code-block:: python

    import pymechanize
    response = pymechanize.urlopen("http://www.example.com/")
    print response.read()


Requirements
------------

- Python >= 3.3
- For Python >= 2.6 use `https://github.com/jjlee/mechanize`_ mechanize.

Installation
============
You can install this package using pypi: `pip install pymechanize`
alternatively you can clone or download the project tarball and run
`python setup.py install`.

Tests
=====
To run the test suite, ensure you are running a local copy of `pymechanize`
and run: `python setup.py nosetests`.

To run the test suite on Python3, PyPy3 versions and `lxml>=3.4.4`, `BeautifulSoup4>=4.4.1` you can use `tox`.

.. code-block:: python

    # Install tox
    $ pip install tox
    # Run the test suites
    $ tox

To run a single or selected test suits, use the nosetest convention. E.g.

.. code-block:: python

    $ python setup.py nosetests --tests tests/example_test.py:ExampleTestClass.example_test_method

Contributing
============
We welcome contributions! see  the `Contribution guidelines <https://github.com/2comms/pymechanize/blob/master/CONTRIBUTING.rst>`_

License
-------

All the code with the exception of `gzip.py` is covered under either the BSD-style license. See the bundled `LICENSE <https://github.com/2comms/pymechanize/blob/master/LICENSE>`_ file for more details.

