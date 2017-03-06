"""real_estate_in_korea trade check command line tool."""

from real_estate_in_korea.options import Options
from real_estate_in_korea.local_code import local_code_db_create
from real_estate_in_korea.data import get_trade_price

import argparse
import datetime
import sys
from typing import List

MAX_MONTH_LIMIT = 144  # 12 year (12 month * 12)


def date_str_validate(date_text: str) -> bool:
    try:
        datetime.datetime.strptime(date_text, '%Y%m')
        return True
    except ValueError:
        return False


def process_options(args: List[str]) -> Options:
    options = Options()
    # Make the help output a little less jarring.
    help_factory = (lambda prog: argparse.RawDescriptionHelpFormatter(
        prog=prog, max_help_position=28))

    parser = argparse.ArgumentParser(prog='real_estate_in_korea',
                                     fromfile_prefix_chars='@',
                                     formatter_class=help_factory)
    parser.add_argument(
            "-g", "--gu", metavar='gu Korea district',
            nargs=1, help="[optional] 구")
    parser.add_argument(
            "-d", "--dong", metavar='dong Korea district',
            nargs=1, help="[optional] 동")
    parser.add_argument(
            "-t", "--apt", metavar='apartment',
            nargs=1, help="[optional] APT")
    parser.add_argument(
            "-m", "--month-range", metavar='checking month range',
            nargs=1, help="[optional] month")
    parser.add_argument(
            "-s", "--size", metavar='apt size', type=float,
            help="[optional] size")
    parser.add_argument(
            "-S", "--start-month", metavar='start month', 
            nargs=1, help="[optional] start month")

    parser.add_argument('--rent', action='store_true')
    parser.add_argument('--text', action='store_true')

    args = parser.parse_args()

    if args.gu:
        options.gu = args.gu[0]

    if args.dong:
        options.dong = args.dong[0]

    if args.apt:
        options.apt = args.apt[0]

    if args.month_range:
        options.month_range = int(args.month_range[0])
        if options.month_range > MAX_MONTH_LIMIT:
            options.month_range = MAX_MONTH_LIMIT

    if args.size:
        options.size = args.size
        # print(options.size)

    if args.start_month:
        if date_str_validate(args.start_month[0]) is False:
            options.start_month = 0
        else:
            options.start_month = args.start_month[0]

    if args.rent:
        options.mode = 1

    if args.text:
        options.text = True

    if options.gu is None:
        print('''use -g option(MUST), default: 마포구 대흥동 자이''')
        options.gu, options.dong, options.apt = '마포구', '대흥동', '자이'

    return options


def main() -> None:
    options = process_options(sys.argv[1:])

    local_code_db_create()  # if not exist

    get_trade_price(options)

    sys.exit(0)
