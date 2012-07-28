#! /usr/bin/python

import sys

def main():

    if len(sys.argv) <2:
	print "Usage: "+ sys.args[0].strip()
	sys.exit(0)

    path   = sys.argv[1]
    f = open(path,'r')
    TAB="\t";
    SPACE=" ";
    c = 0
    for line in f:
	sys.stdout.write(str(c)+TAB+line)
	c = c + 1

    f.close()
    sys.stdout.flush()

if __name__ == '__main__':
    main()

