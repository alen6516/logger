#!/usr/bin/python
# -*- coding: utf-8 -*-
#####
# File Name: test.py
# Author: alen6516
# Created Time: 2018-07-19
#####

import logger
import threading
import random
import time

class foo(threading.Thread):
    
    def __init__(self, name):
        super(foo, self).__init__(name = name)
<<<<<<< HEAD
        self.logger = logger.Logger(name)
        self.logger.cls_set_glo_file("global.log", clear = True)
=======
        self.logger = logger.Logger(name, "DEBUG")
        self.logger.cls_set_glo_file("global.log", clear = False)
>>>>>>> ce4e9dcfd3e1c74b8aa5edd77dd1bb1d62b4870f
        self.logger.set_loc_file("%s.log" % name, clear = True)

    def run(self):
        while True:
            time.sleep(random.randint(1,5))
            self.logger.info(self.logger.name)
            self.logger.warning(self.logger.level)
    


foo1 = foo("foo1")
foo2 = foo("foo2")

foo1.setDaemon(True)
foo2.setDaemon(True)

foo1.start()
foo2.start()

time.sleep(10)
