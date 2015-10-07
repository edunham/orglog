#! /usr/bin/python2

import sys
from github import Github
try:
    from credentials import ghuser, ghpass
except ImportError:
    raise Exception("You must create credentials.py, defining ghuser and ghpass")
import config

# Auth to the API.
# TODO: Figure out how pygithub does API tokens
# https://github.com/PyGithub/PyGithub
g = Github(ghuser, ghpass)

# Get the org
if len(sys.argv) < 2:
    orgname = config.org
else:
    orgname = sys.argv[1]

# Retrieve the org object
org = g.get_organization(orgname)

#TODO: Detect and handle to failure to get the organization

repos = {}

for r in org.get_repos(type="sources"):
    repos[r.name] = r.ssh_url

print repos
