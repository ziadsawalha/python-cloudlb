# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource, SubResourceManager
from cloudlb.consts import HEALTH_MONITOR_TYPES


class HealthMonitor(SubResource):
    def __repr__(self):
        return "<HealthMonitor: %s>" % (self.type)

    def __init__(self, type=None,
                 delay=None,
                 timeout=None,
                 attemptsBeforeDeactivation=None,
                 path=None,
                 statusRegex=None,
                 bodyRegex=None):

        self.type = type
        self.delay = delay
        self.timeout = timeout
        self.attemptsBeforeDeactivation = attemptsBeforeDeactivation

        if not all([self.type, self.delay,
                    self.timeout, self.attemptsBeforeDeactivation]):
            #TODO: Proper Exceptions
            raise Exception("You need to specify a timeout type" + \
                            " and an attemptsBeforeDeactivation.")

        if not self.type in HEALTH_MONITOR_TYPES:
            raise Exception("%s is an invalid healthmonitor type" % (
                    self.type))

        if self.type in ("HTTP", "HTTPS"):
            self.path = path
            self.statusRegex = statusRegex
            # We're only going to define self.bodyRegex is we've been passed a value for it. 
            if bodyRegex:
                self.bodyRegex = bodyRegex

            if not all([path, statusRegex]):
                raise Exception("You need to specify a path and statusRegex with HTTP(S) monitor")


class HealthMonitorManager(SubResourceManager):
    path = None
    type = "healthMonitor"
    resource = HealthMonitor
