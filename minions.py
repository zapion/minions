#!/usr/bin/python


class Minions(object):
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
    interval = None
    variant = None

    def __init__(self, variant="periodical", interval=300, func=None, name):
        self.name = name
        self.variant = variant
        if variant == 'periodical':
            if interval <= 0:
                raise ValueError("inverval should be greater than 0")
            self.interval = interval

    def _work(self):
        '''
        Abtract private interface
        Return True if work is done successfully
        '''
        raise NotImplementedError("%s's worker function is not yet implemented." % (self.__class__))
    def collect(self):
        '''
        interface for collecting information from monitored target
        Parameters: None
        Return: dict{}
        '''
        banana = {}
        self.banana = banana
        return banana

    def report(self):
        '''
        interface for emitting state to file, DB, or other storage
        Parameters: None
        Return: True if emitting successfully
        '''
        return True
