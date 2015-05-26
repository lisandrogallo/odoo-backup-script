# -*- coding: utf-8 -*-

from os import path, makedirs
from errno import EEXIST
from subprocess import Popen, PIPE


def run_command(cmd, output=True):
    try:
        p = Popen(cmd, shell=True, stdout=PIPE)
        out = p.stdout.read().strip()
        if output:
            print '[bash]: %s' % cmd
            return out  # This is the stdout from the shell command
        else:
            return True
    except:
        return False


def file_exists(filename):
    try:
        with open(filename):
            return True
    except IOError:
        return False


def check_path(path):
    try:
        makedirs(path)
    except OSError as exception:
        if exception.errno != EEXIST:
            raise Exception


def check_root():
    if run_command('whoami', False) == 'root':
        return True
    else:
        print("\n***ERROR: This script must be run by root.\n")
        return False


def check_binary(bin_filename, error_on_missing=False):
    """Check if binary exists on system"""
    BIN_DIRS = ['$HOME/Environment/local/bin/',
                '$HOME/bin/',
                '/share/apps/bin/',
                '/usr/local/bin/',
                '/bin/',
                '/usr/bin/']
    for d in BIN_DIRS:
        if path.exists(path.expandvars(path.join(d, bin_filename))):
            return True
    if error_on_missing:
        print "\n***ERROR: '%s' was not found on your system. Please install this package and run the script again." % (bin_filename)
        return False
