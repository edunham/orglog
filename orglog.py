#! /usr/bin/python2

from github import Github
try:
    from credentials import ghuser, ghpass
except ImportError:
    raise Exception("You must create credentials.py, defining ghuser and ghpass")

g = Github(ghuser, ghpass)
