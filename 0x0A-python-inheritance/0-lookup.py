#!/usr/bin/python3
"""
Module 0-lookup
Contains method lookup that returns list of object's attribute and methods
"""

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
