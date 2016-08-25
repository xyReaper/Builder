#!/usr/bin/python
import sys
import subprocess
import time
import os
import getopt
import traceback

#to send a file of gcode to the printer

from printrun.printcore import printcore
from printrun import gcoder
from printrun.utils import setup_logging

if __name__ == '__main__':
	
	loud = True
	work = "/home/flyprint/Desktop/Printrun/Brick_test"
	os.chdir(work)
	filename = "left" 
	cmd = "slic3r" + " " + filename + ".stl" + " --load v1.ini --print-center -60,0" + " --output" + " " + filename + ".gcode"
	print cmd
	subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

	time.sleep(1) 
	
	from printrun.printcore import __version__ as printcore_version
	p = printcore('/dev/ttyACM2',115200) 
	p.loud = True
	time.sleep(2)
	gcode = [i.strip() for i in open(filename + ".gcode")] # or pass in your own array of gcode lines instead of reading from a file
	gcode = gcoder.LightGCode(gcode)
	
	
	p.startprint(gcode) # this will start a print
	statusreport = True
	if statusreport:
	  p.loud = False
       	  sys.stdout.write("Progress: 00.0%\r")
       	  sys.stdout.flush()
	while p.printing:
       	  time.sleep(1)
          if statusreport:
	       	progress = 100 * float(p.queueindex) / len(p.mainqueue)
       		sys.stdout.write("Progress: %02.1f%%\r" % progress)
               	sys.stdout.flush()
	p.disconnect()
	sys.exit(0)

