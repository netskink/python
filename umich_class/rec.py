#!/usr/bin/python


import sys
import os.path


def rec(x):
	print x;
	x=x-1;
	if (x==0):
		return;
	rec(x);

## main ##############################

x=5;
rec(x);
