#!/usr/bin/env python3
""" returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
    all fields in the log line (message)
    """
    textSplit = message.split(separator)
    for field in fields:
        for info in textSplit:  # info is <info>=<infoValue> example name=bob
            if re.search(field, info):
                message = re.sub(info.split("=")[1], redaction, message)
    return message
