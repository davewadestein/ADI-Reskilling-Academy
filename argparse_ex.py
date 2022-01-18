import argparse

parser = argparse.ArgumentParser(description='argparse example')

parser.add_argument('-a', action="store_true",
                    default=False, help='the a option')
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)
parser.add_argument('--version', action='version', 
                    version='%(prog)s 2.0')
parser.add_argument('-v', action='version', 
                    version='%(prog)s 2.0')

# parse args from command line, which won't work in the notebook
args = parser.parse_args()

#args = parser.parse_args(['-b', 'foo', '-c', '0'])

print(args)

if args.a:
    print("-a was passed")
if args.b:
    print("-b", args.b, "was passed")
if args.c != None:
    print("-c", args.c, "was passed (int)")
