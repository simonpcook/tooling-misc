#!/usr/bin/env python2

###### dejaproperties.py - DejaGNU to Properties file #######################
##
##  Copyright (C) 2014 Simon Cook
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
###############################################################################
##
##  Script for converting DejaGNU results to Java Properties files.
##
###############################################################################

import sys

if len(sys.argv) != 3:
  sys.stderr.write("Usage: %s input output\n" % sys.argv[0])
  sys.exit(1)

_input = file(sys.argv[1], 'r')

# This is a stripped down, single shot version of MFrameTest to parse summary
# pass, fail, xpass, xfail, unresolved, untested, unsupport
result = [0, 0, 0, 0, 0, 0, 0]
for line in _input:
  if 'of expected passes' in line:
    result[0] = int(line.replace('# of expected passes',''))
  elif 'of unexpected failures' in line:
    result[1] = int(line.replace('# of unexpected failures',''))
  elif 'of unexpected successes' in line:
    result[2] = int(line.replace('# of unexpected successes',''))
  elif 'of expected failures' in line:
    result[3] = int(line.replace('# of expected failures',''))
  elif 'of unresolved testcases' in line:
    result[4] = int(line.replace('# of unresolved testcases',''))
  elif 'of untested testcases' in line:
    result[5] = int(line.replace('# of untested testcases',''))
  elif 'of unsupported tests' in line:
    result[6] = int(line.replace('# of unsupported tests',''))

file('%s-passes.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[0])
file('%s-failures.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[1])
file('%s-xpass.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[2])
file('%s-xfail.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[3])
file('%s-unresolved.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[4])
file('%s-untested.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[5])
file('%s-unsupported.properties' % sys.argv[2],'w').write('YVALUE=%i\n' % result[6])
