#!/usr/bin/python3
"""Consists of a class to JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation with simple data structure."""
    return obj.__dict__
