#!/usr/bin/python

import os
import time
from subprocess import Popen, PIPE
from enum import Enum


class status(Enum):
    ok = 0
    warning = 1
    critical = 2
    unknown = 3

# TODO: factory pattern should work here?


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
    kwargs = None
    serial = None
    command = None
    description = ''

    def __init__(self, name, **kwargs):
        self.name = name
        self.description = '{Name: ' + self.name
        if 'serial' in kwargs:
            self.serial = kwargs['serial']
            os.environ['ANDROID_SERIAL'] = self.serial
            self.description = ", Serial: " + self.serial
        if 'command' in kwargs:
            self.command = kwargs['command']
            self.description = ", Command: " + self.command
        self.kwargs = kwargs

    def __str__(self):
        print(self.description)

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
            banana.update(self._work())
            banana['name'] = self.name
            banana['serial'] = self.serial
            banana['status'] = status.ok
            banana['timestamp'] = time.time()
            if self.command:
                banana['command'] = self.command
        except Exception as e:
            print(e)
            banana['status'] = status.critical
            banana['err_msg'] = e.message()
        self.banana = banana
        return banana

    def report(self):
        '''
        TODO: if we use shinken or other framework they provide full
        stack of featureinterface for emitting state to file, DB,
        or other storage
        Parameters: None
        Return: True if emitting successfully
        '''
        print("test")
        return True

    def _output(self):
        '''
        Default output to files with timestamp
        '''
        try:
            # TODO: parameter file path from config
            with open('target') as fp:
                print fp
        except Exception as e:
            print(e.message)
            return False
        return True


class ShellMinion(Minion):
    '''
    Minion for running shell command
    '''
    def _work(self):
        if self.command:
            return shell_cmd(self.command)
        return shell_cmd("adb shell b2g-ps")
