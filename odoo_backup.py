# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from sys import argv, exit
from json import load
from datetime import date, datetime


def parse_args():
    parser = ArgumentParser(
        prog='odoo_backup',
        description="Python script to backup Odoo databases.",
        epilog="'mailutils' package is required in order to run this script."
    )

    parser.add_argument("-m", "--monthly",
                        help="Save output file with monthly format",
                        action="store_true")
    parser.add_argument("-t", "--time",
                        help="Save output file with time format",
                        action="store_true")
    parser.add_argument("-f", "--environments-file",
                        help="JSON file with environments data",
                        dest="filename")
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s 1.0')

    args = parser.parse_args()

    if len(argv) > 4:
        print("\n***ERROR: Many arguments.\n")
        parser.print_help()
        exit()

    if not args.filename:
        print("\n***ERROR: Environments file is required.\n")
        parser.print_help()
        exit()
    else:
        # Generate dictionary with instances information
        with open(args.filename) as f:
            instances = load(f)
            f.close()

    today = date.today()
    now = datetime.now()

    if args.monthly:
        return today.strftime("%d-%m-yy"), instances
    elif args.time:
        return '%s-%shs' % (today.strftime("%d-%m-yy"),
                            now.strftime("%H"),
                            instances)
    else:
        return today.strftime("%d-mm-yy"), instances


if __name__ == "__main__":
    print parse_args()
