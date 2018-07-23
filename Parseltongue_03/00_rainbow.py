#!/usr/bin/env python3

# IDK
# By yhuang

import sys
BOLD = 1
FG_GREEN = 32
BG_DARKBLUE = 44

def print_colorful_text(string, style, foreground, background):
	s1 = ''
	format = ';'.join([str(style), str(foreground), str(background)])
	s1 += '\x1b[%sm %s \x1b[0m' % (format, string)
	if (string != "RAINBOW" or string != "W"):
		print (s1, end = "")
	else:
		print (s1)

def main(argv):
	print_colorful_text("R ", 0, 31, 40)
	print_colorful_text("A ", 0, 37, 40)
	print_colorful_text("I ", 0, 33, 40)
	print_colorful_text("N ", 0, 32, 40)
	print_colorful_text("B ", 0, 36, 40)
	print_colorful_text("O ", 0, 34, 40)
	print_colorful_text("W", 0, 35, 40)
	print_colorful_text("RAINBOW", BOLD, FG_GREEN, BG_DARKBLUE)
	print ("\n")

main(sys.argv)
