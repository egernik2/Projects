# -*- coding: utf-8 -*-
import argparse

def main():
    """example: python argparse_template.py hello 10.1 -or=hello -ca=world"""
    parser = argparse.ArgumentParser(description="description to your program here")
    parser.add_argument("echo", help="echo the string")
    parser.add_argument("number", help="float parameter", type=float)
    parser.add_argument("-co", "--custom_option", help="optional parameter with manually specified name in help", metavar="MANUALLY_SPECIFIED")
    parser.add_argument("-ca", "--custom_attribute", help="optional parameter with manually specified attribute to parse_args result", dest="ca")
    parser.add_argument("--optional", help="optional parameter")
    parser.add_argument("-or", "--optional_required", required=True, help="optional required parameter")
    parser.add_argument("-v", "--verbosity", help="optional parameter with short name")
    parser.add_argument("-c", "--choice", help="optional parameter with choices and fixed type", type=int, choices=[0, 1, 2])
    parser.add_argument("-cd", "--choice_default", help="optional parameter with choices, fixed type and default value", type=int, choices=[0, 1, 2], default=0)
    parser.add_argument("-f", "--flag", help="flag without arguments", action="store_true")
    parser.add_argument("-a", "--addition", help="optional argument with occurance counting", action="count")
    args = parser.parse_args()
    
    print(args.echo, args.number)
    if args.optional:
        print("optional parameter specified: %s"%args.optional)
    else:
        print(args.optional)
    print(args.flag)
    print(args.verbosity)
    print(args.choice)
    print(args.addition)
    print(args.choice_default)
    print(args.optional_required)
    print(args.ca)

    
def main1():

    parser = argparse.ArgumentParser(description="description to your program here")
    
    parser.add_argument("--foo", help="foo requires 2 values", nargs=2)
    parser.add_argument("--bar", help="bar requires one or more values", nargs="+")
    parser.add_argument("--tar", help="tar is tricky: 1) <default> if not specified 2) <const> if option specified without vaule 3) <value> if value specified", nargs="?", default=2, const=3, type=int)
    parser.add_argument("baz", help="baz takes orbitrary number of argumets", nargs="*")
    args = parser.parse_args()
    print(args.foo)
    print(args.bar)
    print(args.baz)
    print(args.tar)
    
    
def action1(arg, kwarg):
    print('Doing action1 with arg={} , kwarg={}'.format(arg, kwarg))
    
    
def action2(arg, kwarg):
    print('Doing action2 with arg={} , kwarg={}'.format(arg, kwarg))
    
    
def main2():
    parser = argparse.ArgumentParser(description='description to your program here')
    parser.set_defaults(func=None)
    subparsers = parser.add_subparsers()

    action1_parser = subparsers.add_parser('action1', help='Action1 parser')
    action1_parser.add_argument('arg', help='Mandatory argument')
    action1_parser.add_argument('-k', '--kwarg', help='Optional argument')
    action1_parser.set_defaults(func=action1)
    
    action2_parser = subparsers.add_parser('action2', help='Action2 parser')
    action2_parser.add_argument('arg', help='Mandatory argument')
    action2_parser.add_argument('-k', '--kwarg', help='Optional argument')
    action2_parser.set_defaults(func=action2)
    
    args = parser.parse_args()
    
    if args.func is not None:
        args.func(args.arg, args.kwarg)
    else:
        parser.print_help()
    
    
    
if __name__ == "__main__":
    main2()
