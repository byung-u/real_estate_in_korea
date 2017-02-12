"""real_estate_in_seoul trade check command line tool."""
from real_estate_in_seoul import data
#from local_code import is_local_exist
#import argparse

import argparse
import os
import sys
from typing import Any, Dict, List, Mapping, Optional

#def main(script_path: str) -> None:
def main() -> None:
    # Make the help output a little less jarring.
    help_factory = (lambda prog: argparse.RawDescriptionHelpFormatter(
        prog=prog, max_help_position=28))

    parser = argparse.ArgumentParser(prog='real_estate_in_seoul',
                                     fromfile_prefix_chars='@',
                                     formatter_class=help_factory)
    parser.add_argument(
            "-g", "--gu", metavar='gu (Korea district)',
            nargs=1, help="[optional] 구")
    parser.add_argument(
            "-d", "--dong", metavar='dong (Korea district)',
            nargs=1, help="[optional] 동")
    parser.add_argument(
            "-t", "--apt", metavar='apartment',
            nargs=1, help="[optional] APT")

    args = parser.parse_args()

    if args.gu:
        gu = args.gu[0]
        print(gu)

    if args.dong:
        dong = args.dong[0]
        print(dong)

    if args.apt:
        apt = args.apt[0]
        print(apt)

    get_trade_price(gu, dong, apt)

    sys.exit(0)

