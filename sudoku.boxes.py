#!/usr/bin/python

import sys

# Create table
table = []
for x in range(0,9):
  table.append([])

# If not right args exit
if len(sys.argv) != 2:
  print "Usage: "+sys.argv[0]+" <table string>"
  sys.exit()
# Test table string then fill table
else:
  if sys.argv[1].isdigit() != True or len(sys.argv[1]) != 81:
    print "Table string must be 81 numerical digits, use 0 for blank spaces"
    sys.exit()
  nein = 0
  box = 0
  for r in sys.argv[1]:
    table[box].append(int(r))
    nein += 1
    if nein == 9:
      box += 1
      nein = 0
last = '0'
line = ''
for y in table:
  for z in y:
    line += str(z)

# Print the table the box way
def printTable():
  global table
  for z in range(0,9,3):
    print '-' * 25
    for a in range(0,9,3):
      for x in range(z,z+3):
        print '|',
        for y in range(a,a+3):
          print table[x][y],
      print '|'
  print '-' * 25

def solve():
  global table
  global line
  global last
  last = ''
  for d in table:
    for e in d:
      last += str(e)
  

printTable()
while line != last:
  if '0' not in line:
    solve()
    printTable()
  else:
    sys.exit()
