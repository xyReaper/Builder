#!/usr/bin/env python
import cmd
import glob
import os
import time
import threading
import sys
import shutil
import subprocess
import codecs
import argparse
import locale
import logging
import traceback
import re

from serial import SerialException
#from printrun.printcore import printcore
from printrun.pronsole import pronsole

from printrun.utils import install_locale, run_command, get_command_output, \
    format_time, format_duration, RemainingTimeEstimator, \
    get_home_pos, parse_build_dimensions, parse_temperature_report, \
    setup_logging
from printrun.settings import Settings, BuildDimensionsSetting
from printrun.power import powerset_print_start, powerset_print_stop
from printrun import gcoder
from printrun.rpc import ProntRPC


install_locale('pronterface')

def builder(something):
	
	def eta():
		progress = int(1000 * float(shit.p.queueindex) / len(shit.p.mainqueue)) / 10
                sys.stdout.write("Progress: %02.1f%%\r" % progress)
                sys.stdout.flush()
	

	shit = pronsole()
        shit.load_default_rc()
	shit.do_disconnect('')
	time.sleep(.2)
	shit.do_connect('')
	time.sleep(.2)
	shit.p.send_now('M106') #always turn fan on
	shit.do_load(something)
	time.sleep(1)
	shit.do_print('')
	print "Printing Started"
	sys.stdout.write("Progress: 00.0%\r")
        sys.stdout.flush()

	while shit.p.printing:
		time.sleep(1)
		eta()
	print 'done printing'
	shit.do_exit('')

def loop(self):
        try:
            stop = None
            while not stop:
		line = 'M114'
                line = self.precmd(line)
                stop = self.onecmd(line)
		print 'going to pause'
		time.sleep(15)
        finally:
	    print 'in finally'
            
def drop(leap):
	a = pronsole()
	a.preloop()
	a.load_default_rc()
#	logger = logging.getLogger()
#	logger .setLevel(logging.DEBUG)
	a.do_disconnect('')
	time.sleep(.2)
	a.do_connect('')
	time.sleep(3)
	a.p.loud = True
	a.p.send_now('G21')	#mm mode
        a.p.send_now('G90')	#absolute coordinates
	a.p.send_now('G28')	#home
	time.sleep(.25)
	a.p.send_now('G92 Z0')	#set z at top to be zero
	position = 'G1 Z' + str(leap)
	a.p.send_now(position)
	#a.p.send_now('') #add something wen sensor integration is done
	a.p.send_now('G92 z0')
	#print a.p.send_now('M114')
	time.sleep(2)
	stop = None
	#a.parse_cmdline(sys.argv[1:])	
	setup_logging(sys.stdout, a.settings.log_path, True)
	loop(a)

#	while (True):
#	
#		print "in loop"
#		time.sleep(1)
#		sys.stdout.write("please wait\r")
 #             	time.sleep(1)
#	#	a.p.send_now('M114')
#		a.p._send('M114')
#		#a.p._listen()
#		#a.write_prompt()
	#	print  a.p.abs_pos
	print 'floor calibrations complete' 

if __name__ == '__main__':
	

	safeheight = 10	#mm above plate
	#remember that the zero is the top initially so go down by the safeheight
	safeheight = - (100 - safeheight)
	drop(safeheight)
	#builder('tiny.gcode')
	
	sys.exit(0)


