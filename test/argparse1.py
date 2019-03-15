__author__ = 'igis_gzy'

import argparse

def par1():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store', dest='simple_value',
            help='Store a simple value')

    parser.add_argument('-c', action='store_const', dest='constant_value',
            const='value-to-store',
            help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=False,
            dest='boolean_switch',
            help='Set a switch to true')
    parser.add_argument('-f', action='store_false', default=False,
            dest='boolean_switch',
            help='Set a switch to false')

    parser.add_argument('-a', action='append', dest='collection',
            default=[],
            help='Add repeated values to a list')

    parser.add_argument('-A', action='append_const', dest='const_collection',
            const='value-1-to-append',
            default=[],
            help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection',
            const='value-2-to-append',
            help='Add different values to list')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()
    print 'simple_value     =', results.simple_value
    print 'constant_value   =', results.constant_value
    print 'boolean_switch   =', results.boolean_switch
    print 'collection       =', results.collection
    print 'const_collection =', results.const_collection

def par2():
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('-a', action="store_true", default=False)
    parser.add_argument('-b', action="store", dest="b")
    parser.add_argument('-c', action="store", dest="c", type=int)
    print parser.parse_args(['-a', '-bval', '-c', '3'])

def par3():
    parser = argparse.ArgumentParser(description='Change the option prefix charaters',
        prefix_chars='-+/')
    parser.add_argument('-a', action="store_false", default=None,
            help='Turn A off')
    parser.add_argument('+a', action="store_true", default=None,
            help='Turn A on')
    parser.add_argument('//noarg', '++noarg', action="store_true", default=False)
    print parser.parse_args()

def par4():
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('--optional', action="store_true", default=False)
    parser.add_argument('positional', action="store")
    print parser.parse_args()


#run python argparse1.py -h
if __name__ == "__main__":
    # par1()
    # par2()
    # par3()
    par4()

