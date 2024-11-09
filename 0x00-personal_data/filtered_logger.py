#!/usr/bin/env python3
import logging
import re

""" basic logging module """


def filter_datum(fileds: list[str], redaction: str, message: str, separator: str) -> str:
    """returns the log obfuscated message"""
    for field in fileds:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
