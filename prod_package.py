#! /usr/bin/env python
from __future__ import print_function

import sys
import json
import argparse
import elm_package


def load_package_from_file(path):
    with open(path) as f:
        dict = json.load(f)
    return elm_package.ProductionPackage(dict)


def main():

    parser = argparse.ArgumentParser(description='Elm package, but for production code.')
    #parser.add_argument('--elm-location', help='specify the location of elm, e.g node_modules/.bin', default='')

    parser.add_argument('--package-file', help='specify a package file to use', default='prod_elm_package.json')
    parser.add_argument('--tests', help='compile the tests', action='store_true', default=False)
    parser.add_argument('--app', help='compile the app', action='store_true', default=False)



    args = parser.parse_args()

    package = load_package_from_file(args.package_file)

    if args.app:
        package.app_package.compile()

    if args.tests:
        package.test_package.compile()


if __name__ == '__main__':
    main()
