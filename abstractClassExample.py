import itertools as it
import sys
import traceback
import uuid
from abc import ABCMeta, abstractmethod

import requests

from es import ESSchedule
from api import APIConnector
import config


class Dispatcher(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, batch_size):
        self.batch_size = batch_size

    def _dispatch(self, cids, nomad_job_id):
         print "_dispatch"

    @abstractmethod
    def dispatch(self, cids):
        pass


class BulkDispatcher(Dispatcher):

    def __init__(self, batch_size):
        super(BulkDispatcher, self).__init__(batch_size)

    def dispatch(self, cids):
         print "BulkDispatcher dispatch"


class ScheduledDispatcher(Dispatcher):

    def __init__(self, batch_size):
        super(ScheduledDispatcher, self).__init__(batch_size)

    def dispatch(self, cids):
        print "ScheduledDispatcher dispatch"

    def _dispatch_scheduled_queries(self, scheduled_queries):
        print "ScheduledDispatcher _dispatch_scheduled_queries"        

    def _dispatch_scheduled_assets(self, scheduled_assets):
        """ Dispatch the given assets and yield assets that were dispatched
        print "ScheduledDispatcher _dispatch_scheduled_assets"