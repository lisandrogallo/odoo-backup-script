# -*- coding: utf-8 -*-

import os
import errno
import subprocess
from sys import exit


def check_if_root():
    """Check if the script is running with root privileges"""
    if not os.geteuid() == 0:
        print("\n***ERROR: This script must be run by root.\n")
        exit()


def run_bash(cmd):
    """Takes Bash commands and returns them"""
    try:
        print "~$: %s" % cmd
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read().strip()
        return out  # This is the stdout from the shell command
    except:
        return False


def file_exists(filename):
    try:
        with open(filename):
            return True
    except IOError:
        return False


def path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def check_binary(bin_filename, error_on_missing=False):
    """Check if binary exists on system"""
    BIN_DIRS = ['$HOME/Environment/local/bin/',
                '$HOME/bin/',
                '/share/apps/bin/',
                '/usr/local/bin/',
                '/bin/',
                '/usr/bin/']
    for d in BIN_DIRS:
        p = os.path.expandvars(os.path.join(d, bin_filename))
        if os.path.exists(p):
            return p
    if error_on_missing:
        print "\n***ERROR: '%s' was not found on your system. \
        Please install this package and run the script again." % (bin_filename)
        return False
