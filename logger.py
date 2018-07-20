#!/usr/bin/python
# -*- coding: utf-8 -*-
#####
# File Name: color_print.py
# Author: alen6516
# Created Time: 2018-07-19
#####

import time
from threading import current_thread

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class logger(object):

    global_log_file = None

    @classmethod
    def set_global_log_file(cls, global_log_file, clear = False):
        
        cls.global_log_file = global_log_file
        if clear:
            open(cls.global_log_file, 'w').write("")
    
    def __init__(self, name = "unknown", thread_name = current_thread().name, *args, **kwargs):
        super(logger, self).__init__()
        self.name = name
        self.thread_name = thread_name
        self.log_file = None 

    def set_log_file(self, log_file, clear = False):
        self.log_file = log_file
        if clear:
            open(self.log_file, 'w').write("")

    def get_format(self):
        get_time = time.strftime("%H:%M:%S")

        return "[ %10s ][ %10s ][ %s ]" % (self.name, self.thread_name, get_time)

    def write_file(self, string):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(self.get_format()+": " + string + "\n")
        if self.global_log_file:
            with open(self.global_log_file, 'a') as f:
                f.write(self.get_format()+": " + string + "\n")

    def debug(self, string):
        print(self.get_format()+": " + string)
        self.write_file(string)

    def info(self, string):
        print(self.get_format()+": " + Color.OKGREEN + string + Color.ENDC)
        self.write_file(string)

    def warning(self, string):
        print(self.get_format()+": " + Color.WARNING + string + Color.ENDC)
        self.write_file(string)

    def error(self, string):
        print(self.get_format()+": " + Color.FAIL + string + Color.ENDC)
        self.write_file(string)
    
            
