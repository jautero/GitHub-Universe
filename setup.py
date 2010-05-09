#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Setup GitHub Universe.
Created by Juha Autero on 2010-05-09.
Copyright (c) 2010 Juha Autero. All rights reserved.

This script will ask few questions and use it to configure your GitHub Universe Makefiles.
"""

import sys
import os

def convert_file(watched,filename):
    infile=open(filename)
    data=infile.readlines()
    infile.close()
    outfile=open(filename,"w")
    for line in data:
        if (line.find("gituser:=")==0):
            line="gituser:=%s\n" % watched
        outfile.write(line)
    outfile.close()

print __doc__

watched_user=raw_input("Username for watched projects: ")
convert_file(watched_user,"projects.make")
