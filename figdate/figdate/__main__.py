from . import date

import argparse
import locale


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

    parser = argparse.ArgumentParser(description='Show date using pyfiglet.')
    parser.add_argument('format', nargs='?', type=str, default='%Y %d %b, %A', help='date format.')
    parser.add_argument('font', nargs='?', type=str, default='graceful', help='pyfiglet font style.')
    args = parser.parse_args()

    date.date(args.format, args.font)
