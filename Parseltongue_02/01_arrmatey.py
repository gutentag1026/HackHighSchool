import sys

arguments = len(sys.argv) - 1

position = 0
while (arguments >= position):
    print ("Argv of %i is %s" % (position, sys.argv[position]))
    position = position + 1

argv_array = sys.argv
argv_array.sort(reverse=True, key=len)

for i in argv_array:
    print (i)
