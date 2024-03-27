#!/usr/bin/env python3
""" A Module that effects an expiring web cache and tracking """
from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Number of times a request
    has been made counted"""

    @wraps(method)
    def wrapper(url):
        """ Decorator functionality wrapper """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ HTML content of a particular URL obtained
    and returned.
    """
    req = requests.get(url)
    return req.text
