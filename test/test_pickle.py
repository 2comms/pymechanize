import pickle
import pymechanize
from pymechanize import response
from pymechanize import testcase


def pickle_and_unpickle(obj, implementation):
    return implementation.loads(implementation.dumps(obj))


def test_pickling(obj, check=lambda unpickled: None):
#     check(pickle_and_unpickle(obj, cPickle))
    check(pickle_and_unpickle(obj, pickle))


class PickleTest(testcase.TestCase):

    def test_pickle_cookie(self):
        cookiejar = pymechanize.CookieJar()
        url = "http://example.com/"
        request = pymechanize.Request(url)
        response = response.test_response(
            headers=[("Set-Cookie", "spam=eggs")],
            url=url)
        [cookie] = cookiejar.make_cookies(response, request)
        check_equality = lambda unpickled: self.assertEqual(unpickled, cookie)
        test_pickling(cookie, check_equality)

    def test_pickle_cookiejar(self):
        test_pickling(pymechanize.CookieJar())


if __name__ == "__main__":
    testcase.main()
