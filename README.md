Summary
=======

**odoo_backup** is a python script to backup PostgreSQL databases in use with **Odoo**. This script must be run with root privileges.

Usage
=====

    usage: odoo_backup [-h] [-m] [-t] [-f FILENAME] [--version]
    
    optional arguments:
      -h, --help            show this help message and exit
      -m, --monthly         Save output file with monthly format
      -t, --time            Save output file with time format
      -f FILENAME, --environments-file FILENAME
                            JSON file with environments data
      --version             show program's version number and exit

'mailutils' and 'grive' packages are required in order to run this script.
