__author__ = 'igis_gzy'

import argparse
import argparse_parent_base

parser = argparse.ArgumentParser(parents=[argparse_parent_base.parser])

parser.add_argument('--local-arg', action="store_true", default=False)

print parser.parse_args()

# python argparse_uses_parent.py -h

