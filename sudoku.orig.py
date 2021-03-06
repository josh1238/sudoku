#!/usr/bin/python

import sys

# Create table
table = []
for x in range(0,9):
  table.append([])

# If too many args exit
if len(sys.argv) != 2:
  print "Usage: "+sys.argv[0]+" <table string>"
  sys.exit()
# Test table string then fill table
else:
  if sys.argv[1].isdigit() != True or len(sys.argv[1]) != 81:
    print "Table string must be 81 numerical digits, use 0 for blank spaces"
    sys.exit()
  nein = 0
  row = 0
  for r in sys.argv[1]:
    table[row].append(int(r))
    nein += 1
    if nein == 9:
      row += 1
      nein = 0
last = '0'
line = ''
for y in table:
  for z in y:
    line += str(z)

# For use in solve()
# Check each box for low amount of 0s
def checkBoxes(s,f,d,e):
  global table
  zeroes = []
  na = []
  for x in range(s,f):
    for y in range(d,e):
      if table[x][y] == 0:
        zeroes.append([x,y])    # List of x,y coordinates for 0s
      else:
        na.append(table[x][y])  # Not available, get it? (Value in spot)
  if len(zeroes) == 1:
    for z in range(1,10):
      if z not in na:
        table[zeroes[0][0]][zeroes[0][1]] = z # If only 1 0, set it to missing value
        print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(z)+" checkBoxes 1"
  if len(zeroes) == 2:
    for z in range(1,10):
      if z not in na:
        if zeroes[0][1] != zeroes[1][1]:  # If 0s are in different columns
          for a in zeroes:
            for b in range(0,9):
              if table[b][a[1]] == z: # If missing number is in same column,
                a.append(z)           # Append this value to x,y coords
          if len(zeroes[0]) == 3:
            table[zeroes[1][0]][zeroes[1][1]] = zeroes[0][2]  # Set other 0 to value
            print "["+str(zeroes[1][0])+","+str(zeroes[1][1])+"] = "+str(zeroes[0][2])+" checkBoxes 2 col"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
          if len(zeroes[1]) == 3:
            table[zeroes[0][0]][zeroes[0][1]] = zeroes[1][2]
            print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(zeroes[1][2])+" checkBoxes 2 col"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
        if zeroes[0][0] != zeroes[1][0]:  # If 0s are in different rows
          for a in zeroes:
            for b in range(0,9):
              if table[a[0]][b] == z: # If missing number is in same row,
                a.append(z)           # Append value to x,y coords
          if len(zeroes[0]) == 3:
            table[zeroes[1][0]][zeroes[1][1]] = zeroes[0][2]  # Set other 0 to value
            print "["+str(zeroes[1][0])+","+str(zeroes[1][1])+"] = "+str(zeroes[0][2])+" checkBoxes 2 row"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
          elif len(zeroes[1]) == 3:
            table[zeroes[0][0]][zeroes[0][1]] = zeroes[1][2]
            print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(zeroes[1][2])+" checkBoxes 2 row"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
#    checkBoxes(s,f,d,e)
  if len(zeroes) == 3:
    for z in range(1,10):
      if z not in na:
        # If 0 is alone in column
        if zeroes[0][1] != zeroes[1][1] and zeroes[0][1] != zeroes[2][1]:
          for a in zeroes:
            if a != zeroes[0]:      # Other 0s
              for b in range(0,9):
                if table[b][a[1]] == z: # If value is in column,
                  a.append(z)           # Append value to x,y coords
            else:
              pass
          if len(zeroes[1]) == 3 and len(zeroes[2]) == 3: # If both others matched
            table[zeroes[0][0]][zeroes[0][1]] = z         # Set value
            print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(z)+" checkBoxes 3"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
        if zeroes[1][1] != zeroes[0][1] and zeroes[1][1] != zeroes[2][1]:
          for a in zeroes:
            if a != zeroes[1]:
              for b in range(0,9):
                if table[b][a[1]] == z:
                  a.append(z)
            else:
              pass
          if len(zeroes[0]) == 3 and len(zeroes[2]) == 3:
            table[zeroes[1][0]][zeroes[1][1]] = z
            print "["+str(zeroes[1][0])+","+str(zeroes[1][1])+"] = "+str(z)+" checkBoxes 3"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
        if zeroes[2][1] != zeroes[0][1] and zeroes[2][1] != zeroes[1][1]:
          for a in zeroes:
            if a != zeroes[2]:
              for b in range(0,9):
                if table[b][a[1]] == z:
                  a.append(z)
            else:
              pass
          if len(zeroes[0]) == 3 and len(zeroes[1]) == 3:
            table[zeroes[2][0]][zeroes[2][1]] = z
            print "["+str(zeroes[2][0])+","+str(zeroes[2][1])+"] = "+str(z)+" checkBoxes 3"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
        # If 0 is alone in row
        if zeroes[0][0] != zeroes[1][0] and zeroes[0][0] != zeroes[2][0]:
          for a in zeroes:
            if a != zeroes[0]:
              for b in range(0,9):
                if table[a[0]][b] == z:
                  a.append(z)
            else:
              pass
          if len(zeroes[1]) == 3 and len(zeroes[2]) == 3:
            table[zeroes[0][0]][zeroes[0][1]] = z
            print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(z)+" checkBoxes 3"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
        if zeroes[1][0] != zeroes[0][0] and zeroes[1][0] != zeroes[2][0]:
          for a in zeroes:
            if a != zeroes[1]:
              for b in range(0,9):
                if table[a[0]][b] == z:
                  a.append(z)
            else:
              pass
          if len(zeroes[0]) == 3 and len(zeroes[2]) == 3:
            table[zeroes[1][0]][zeroes[1][1]] = z
            print "["+str(zeroes[1][0])+","+str(zeroes[1][1])+"] = "+str(z)+" checkBoxes 3"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
        if zeroes[2][0] != zeroes[0][0] and zeroes[2][0] != zeroes[1][0]:
          for a in zeroes:
            if a != zeroes[2]:
              for b in range(0,9):
                if table[a[0]][b] == z:
                  a.append(z)
            else:
              pass
          if len(zeroes[0]) == 3 and len(zeroes[1]) == 3:
            table[zeroes[2][0]][zeroes[2][1]] = z
            print "["+str(zeroes[2][0])+","+str(zeroes[2][1])+"] = "+str(z)+" checkBoxes 3"
            print "zeroes ="
            for c in zeroes:
              print c
            print "na ="
            for d in na:
              print d
            printTable()
            raw_input("Press enter to continue...")
            checkBoxes(s,f,d,e)
#    checkBoxes(s,f,d,e)

# For use in vertWork()
# Box, column, value
def compareHorizontal(s,f,y,z):
  global table
  qx = []
  wrong = []
  for c in range(s,f):
    if table[c][y] == 0:  # Collect 0s as possible x value
      qx.append(c)
  if len(qx) == 1:
    table[qx[0]][y] = z   # If 1 0 set as value
    print "["+str(qx[0])+","+str(y)+"] = "+str(z)+" compareHorizontal 1"
  elif len(qx) == 2:
    for d in qx:
      for e in range(0,9):
        if table[d][e] == z:  # For each 0 check row for match
          wrong.append(d)
    if len(wrong) == 2:
      print "You fucked up hard (compHorz)"
    elif len(wrong) == 1:   # If 1 is wrong, set other as value
      for g in qx:
        if g == wrong[0]:
          continue
        else:
          table[g][y] = z
          print "["+str(g)+","+str(y)+"] = "+str(z)+" compareHorizontal 2"
  elif len(qx) == 3:
    for d in qx:
      for e in range(0,9):
        if table[d][e] == z:
          wrong.append(d)
    if len(wrong) == 3:
      print "You fucked up hard (compHorz)"
    elif len(wrong) == 2:
      for g in qx:
        if g in wrong:
          continue
        else:
          table[g][y] = z
          print "["+str(g)+","+str(y)+"] = "+str(z)+" compareHorizontal 3"
    elif len(wrong) == 1:
      pass

# For use in horzWork()
def compareVertical(s,f,x,z):
  global table
  qy = []
  wrong = []
  for c in range(s,f):
    if table[x][c] == 0:
      qy.append(c)
  if len(qy) == 1:
    table[x][qy[0]] = z
    print "["+str(x)+","+str(qy[0])+"] = "+str(z)+" compareVertical 1"
  elif len(qy) == 2:
    for d in qy:
      for e in range(0,9):
        if table[e][d] == z:
          wrong.append(d)
    if len(wrong) == 2:
      print "You fucked up hard (compVert)"
    elif len(wrong) == 1:
      for g in qy:
        if g == wrong[0]:
          continue
        else:
          table[x][g] = z
          print "["+str(x)+","+str(g)+"] = "+str(z)+" compareVertical 2"
  elif len(qy) == 3:
    for d in qy:
      for e in range(0,9):
        if table[e][d] == z:
          wrong.append(d)
    if len(wrong) == 3:
      print "You fucked up hard (compVert)"
    elif len(wrong) == 2:
      for g in qy:
        if g in wrong:
          continue
        else:
          table[x][g] = z
          print "["+str(x)+","+str(g)+"] = "+str(z)+" compareVertical 3"
    elif len(wrong) == 1:
      pass

# For use in solve()
# Look for low # of 0s in row
def horzLine(x):
  global table
  zeroes = []
  na = []
  for y in range(0,9):
    if table[x][y] == 0:
      zeroes.append([x,y])
    else:
      na.append(table[x][y])
  if len(zeroes) == 1:
    for z in range(1,10):
      if z not in na:
        table[zeroes[0][0]][zeroes[0][1]] = z
        print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(z)+" horzLine 1"
  elif len(zeroes) == 2:
    for z in range(1,10):
      if z not in na:
        for a in zeroes:
          for b in range(0,9):
            if table[b][a[1]] == z:
              a.append(z)
        if len(zeroes[0]) == 3:
          table[zeroes[1][0]][zeroes[1][1]] = zeroes[0][2]
          print "["+str(zeroes[1][0])+","+str(zeroes[1][1])+"] = "+str(zeroes[0][2])+" horzLine 2"
        elif len(zeroes[1]) == 3:
          table[zeroes[0][0]][zeroes[0][1]] = zeroes[1][2]
          print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(zeroes[1][2])+" horzLine 2"
  elif len(zeroes) == 3:
    for z in range(1,10):
      if z not in na:
        for a in zeroes:
          for b in range(0,9):
            if table[b][a[1]] == z:
              a.append(z)
        if len(zeroes[0]) == 3 and len(zeroes[1]) == 3:
          table[zeroes[2][0]][zeroes[2][1]] = zeroes[0][2]
          print "["+str(zeroes[2][0])+","+str(zeroes[2][1])+"] = "+str(zeroes[0][2])+" horzLine 2"
        elif len(zeroes[0]) == 3 and len(zeroes[2]) == 3:
          table[zeroes[1][0]][zeroes[1][1]] = zeroes[0][2]
          print "["+str(zeroes[1][0])+","+str(zeroes[1][1])+"] = "+str(zeroes[0][2])+" horzLine 2"
        elif len(zeroes[1]) == 3 and len(zeroes[2]) == 3:
          table[zeroes[0][0]][zeroes[0][1]] = zeroes[1][2]
          print "["+str(zeroes[0][0])+","+str(zeroes[0][1])+"] = "+str(zeroes[1][2])+" horzLine 2"

# For use in solve()
# Look for 2 values horizontally
def horzWork(x,y):
  global table
  if table[x][y] != 0:
    cnt = 1
    z = table[x][y]
    if x < 3:
      s = 0
      f = 3
    elif x > 2 and x < 6:
      s = 3
      f = 6
    elif x > 5:
      s = 6
      f = 9
    for a in range(s,f):
      for b in range(0,9):
        if table[a][b] == z:
          if a == x and b == y:
            continue
          else:
            ax = a
            by = b
            cnt += 1
    if cnt == 2:
      if x == 0:      # Determin row of missing value
        if ax == 1:
          qx = 2
        elif ax == 2:
          qx = 1
      elif x == 1:
        if ax == 0:
          qx = 2
        elif ax == 2:
          qx = 0
      elif x == 2:
        if ax == 0:
          qx = 1
        elif ax == 1:
          qx = 0
      elif x == 3:
        if ax == 4:
          qx = 5
        elif ax == 5:
          qx = 4
      elif x == 4:
        if ax == 3:
          qx = 5
        elif ax == 5:
          qx = 3
      elif x == 5:
        if ax == 3:
          qx = 4
        elif ax == 4:
          qx = 3
      elif x == 6:
        if ax == 7:
          qx = 8
        elif ax == 8:
          qx = 7
      elif x == 7:
        if ax == 6:
          qx = 8
        elif ax == 8:
          qx = 6
      elif x == 8:
        if ax == 6:
          qx = 7
        elif ax == 7:
          qx = 6
      if y < 3:                     # Determine box
        if by > 2 and by < 6:
          compareVertical(6,9,qx,z) # Box, row, value
        elif by > 5:
          compareVertical(3,6,qx,z)
      elif y > 2 and y < 6:
        if by < 3:
          compareVertical(6,9,qx,z)
        elif by > 5:
          compareVertical(0,3,qx,z)
      elif y > 5:
        if by < 3:
          compareVertical(3,6,qx,z)
        elif by > 2 and by < 6:
          compareVertical(0,3,qx,z)

# Print the table
def printTable():
  global table
  tres = 0
  tres2 = 0
  line = ''
  for x in table:
    if tres % 3 == 0:
      print '-' * 25
    for y in x:
      if tres2 % 3 == 0:
        print '|',
      print y,
      tres2 += 1
    print '|'
    tres2 = 0
    tres += 1
    if tres == 9:
      print '-' * 25
  print ''

# Solve with different perspectives
def solve():
  global table
  global line
  global last
  last = ''
  for d in table:
    for e in d:
      last += str(e)
  for x in range(0,9):
    for y in range(0,9):
      vertWork(x,y)
      horzWork(x,y)
  for z in range(0,10,3):
    for a in range(0,10,3):
      if a - z == 3:
        for b in range(0,10,3):
          for c in range(0,10,3):
            if c - b == 3:
              checkBoxes(z,a,b,c)
  for d in range(0,9):
    horzLine(d)
  line = ''
  for d in table:
    for e in d:
      line += str(e)

# For use in solve()
def vertWork(x,y):
  global table
  if table[x][y] != 0:
    cnt = 1
    z = table[x][y]
    if y < 3:
      s = 0
      f = 3
    elif y > 2 and y < 6:
      s = 3
      f = 6
    elif y > 5:
      s = 6
      f = 9
    for a in range(0,9):
      for b in range(s,f):
        if table[a][b] == z:
          if a == x and b == y:
            continue
          else:
            ax = a
            by = b
            cnt += 1
    if cnt == 2:
      if y == 0:
        if by == 1:
          qy = 2
        elif by == 2:
          qy = 1
      elif y == 1:
        if by == 0:
          qy = 2
        elif by == 2:
          qy = 0
      elif y == 2:
        if by == 0:
          qy = 1
        elif by == 1:
          qy = 0
      elif y == 3:
        if by == 4:
          qy = 5
        elif by == 5:
          qy = 4
      elif y == 4:
        if by == 3:
          qy = 5
        elif by == 5:
          qy = 3
      elif y == 5:
        if by == 3:
          qy = 4
        elif by == 4:
          qy = 3
      elif y == 6:
        if by == 7:
          qy = 8
        elif by == 8:
          qy = 7
      elif y == 7:
        if by == 6:
          qy = 8
        elif by == 8:
          qy = 6
      elif y == 8:
        if by == 6:
          qy = 7
        elif by == 7:
          qy = 6
      if x < 3:
        if ax > 2 and ax < 6:
          compareHorizontal(6,9,qy,z)
        elif ax > 5:
          compareHorizontal(3,6,qy,z)
      elif x > 2 and x < 6:
        if ax < 3:
          compareHorizontal(6,9,qy,z)
        elif ax > 5:
          compareHorizontal(0,3,qy,z)
      elif x > 5:
        if ax < 3:
          compareHorizontal(3,6,qy,z)
        elif ax > 2 and ax < 6:
          compareHorizontal(0,3,qy,z)

printTable()
while True:
  if line != last:
    if '0' in line:
      solve()
      printTable()
    else:
      sys.exit()
  else:
    sys.exit()
