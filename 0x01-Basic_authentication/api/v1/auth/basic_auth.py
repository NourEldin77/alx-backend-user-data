#!/usr/bin/env python3


""" basic auth module for the API
"""


from api.v1.auth.auth import Auth
from typing import TypeVar
from flask import request


class BasicAuth(Auth):
    """ BasicAuth class
    """
    pass


auth = BasicAuth()
