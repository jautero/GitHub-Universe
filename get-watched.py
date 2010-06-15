#!/usr/bin/env python
# encoding: utf-8
"""
get-watched.py

Created by Juha Autero on 2010-04-19.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

import sys, os
import getopt
from github import github

help_message = '''
Get list of watched repositories. Takes user name as parameter'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def get_github_token_from_git():
    data_dict={"user":None,"token":None}
    data=os.popen("git config github.user").read().strip()
    if data != "":
        data_dict["user"]=data
    data=os.popen("git config github.token").read().strip()
    if data != "":
        data_dict["token"]=data
    return data_dict

def main(argv=None):
    output = sys.stdout
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = file(value,"w")
        if len(args) < 1:
            raise Usage("Missing user name.")
        if len(args) > 1:
            raise Usage("Too many parameters")
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2
    userdata=get_github_token_from_git()
    gh=github.GitHub(**userdata)
    for repo in gh.repos.watched(args[0]):
        print >>output, "%s=%s.git" % (repo.name,repo.url)
        # HACK: API returns URL to repository page, not to the git repository.
        # Hopefully this will work. (See: http://support.github.com/discussions/feature-requests/620-add-the-clone-url-to-repo-info)
        # We should probably build it from owner and name, since in the above link that is promised to be stable, but I can't be bothered.


if __name__ == "__main__":
    sys.exit(main())
