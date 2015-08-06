#!/usr/bin/python

from subprocess import Popen, PIPE
from enum import Enum


class status(Enum):
    ok = 0
    warning = 1
    critical = 2
    unknown = 3


def shell_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    out = p.communicate()
    return {'stdout': out[0], 'stderr': out[1]}


class Minion(object):
    # An abtract class for spawning status collectors and emitters
    # 2 types of minions used
    # 1. periodical:
    #       parameter: interval
    #       will periodically trigger job
    #       ex: b2g-info, b2g-ps
    # 2. continuous:
    #       parameter: None
    #       will spawn subprocess
    # 2 func types:
    #       if func is string, run it as a system command
    name = None

    def __init__(self, name, **kwargs):
        self.name = name

    def _work(self, **kwargs):
        '''
        Abtract private interface
        Return dict with status code if work is done successfully
        '''
        raise NotImplementedError(
            "%s's worker function is not yet implemented." % (self.__class__)
            )

    def collect(self):
        '''
        interface for collecting information from monitored target
        Parameters: None
        Return: dict{}
        '''
        banana = {}
        try:
            self._work()
        except:
            
        self.banana = banana
        return banana

    def report(self):
        '''
        TODO: if we use shinken or other framework they provide full stack of feature
        interface for emitting state to file, DB, or other storage
        Parameters: None
        Return: True if emitting successfully
        '''
        print("test")
        return True


class DemoMinion(Minion):
    '''
    Demo minion for running b2g-ps
    '''
    def _work(self, serial):
        ret = shell_cmd("adb devices")
