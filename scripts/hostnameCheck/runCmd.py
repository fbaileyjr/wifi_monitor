#!/usr/bin/python -tt

from subprocess import *

#function to run a command
def run_cmd(cmd):
                p = Popen(cmd, shell=True, stdout=PIPE)
                output = p.communicate()[0]
                return output



