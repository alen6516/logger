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

class Logger(object):

    ''' category '''
    level_di = {
        "DEBUG":   0,
        "INFO":    1,
        "WARNING": 2,
        "ERROR":   3
    }

    glo_file = None

    @classmethod
    def cls_set_glo_file(cls, glo_file, clear = False):
        ''' set global log file ''' 
        cls.glo_file = glo_file
        if clear:
            open(cls.glo_file, 'w').write("")
    
    def __init__(self, name = "unknown", level = "DEBUG", *args, **kwargs):
        super(Logger, self).__init__()
        self.name = name        # name of the logger, same as the caller's class name 
        self.level = level      # logger's level 
        self.loc_file = None    # local log file

    def set_loc_file(self, loc_file, clear = False):
        ''' set the file to write msg '''
        self.loc_file = loc_file

        if clear:
            ''' clear the file content '''
            open(self.loc_file, 'w').write("")

    def _get_format(self):
        ''' get format of the output '''
        ret_time = time.strftime("%H:%M:%S")
        return "[ %10s ][ %10s ][ %s ]" % (self.name, current_thread().name, ret_time)
    
    def _write_file(self, msg, format_, level):
        ''' write the msg to the file set by set_file '''

        msg = format_ + "[ %7s ]" % level +": " + msg + "\n"
        
        ''' write to local log file '''
        if self.loc_file:
            with open(self.loc_file, 'a') as f:
                f.write(msg)

        ''' write to global log file '''
        if self.glo_file:
            with open(self.glo_file, 'a') as f:
                f.write(msg)

    def debug(self, msg):
       
        level = "DEBUG"
       
        ''' do nothing if set_level is higher than this level '''
        if self.level_di[self.level] > self.level_di[level]:
            return

        ret_format = self._get_format()
        print(ret_format + ": " + Color.OKBLUE + msg + Color.ENDC)
        self._write_file(msg, ret_format, "DEBUG")

    def info(self, msg):
       
        level = "INFO"
       
        ''' do nothing if set_level is higher than this level '''
        if self.level_di[self.level] > self.level_di[level]:
            return

        ret_format = self._get_format()
        print(self._get_format()+": " + Color.OKGREEN + msg + Color.ENDC)
        self._write_file(msg, ret_format, "INFO")

    def warning(self, msg):
       
        level = "WARNING"
       
        ''' do nothing if set_level is higher than this level '''
        if self.level_di[self.level] > self.level_di[level]:
            return

        ret_format = self._get_format()
        print(self._get_format()+": " + Color.WARNING + msg + Color.ENDC)
        self._write_file(msg, ret_format, "WARNING")

    def error(self, msg):
       
        level = "ERROR"
       
        ''' do nothing if set_level is higher than this level '''
        if self.level_di[self.level] > self.level_di[level]:
            return

        ret_format = self._get_format()
        print(self._get_format()+": " + Color.FAIL + msg + Color.ENDC)
        self._write_file(msg, ret_format, "ERROR")
    
