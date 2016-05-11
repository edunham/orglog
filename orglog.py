#! /usr/bin/python2

import sys
import os
from github import Github
try:
    from credentials import ghuser, ghpass
except ImportError:
    try:
        ghuser = os.environ['GH_USER']
        ghpass = os.environ['GH_PASS']
    except:
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

ignores = config.ignore_repos if config.ignore_repos else []

for r in org.get_repos(type="sources"):
    if r.name not in ignores:
        repos[r.name] = r.html_url

# Clone all those repos
#TODO: handle error if dir exists
os.mkdir(config.clones_dir)

#TODO: Some of these might already exist. Error handling?
for name in repos:
    where = config.clones_dir + name
    os.system("git clone --bare " + repos[name] + " " + where)
    os.system("git -C " + where + " log >> "+ config.log_path)

if config.destroy_clones:
    os.system("rm -rf " + config.clones_dir)
