"""Django Easier Settings."""

import os
import warnings


ENVIRONMENT_VARIABLE = 'DJES_MODE'


def mode(name):
    if not name:
        raise ValueError('Invalid mode name')
    return os.environ.get(ENVIRONMENT_VARIABLE) == name


def is_local():
    return ENVIRONMENT_VARIABLE not in os.environ


class Settings(object):

    def __init__(self, force_uppercase=True):
        self._settings = {}
        self._force_uppercase = force_uppercase

    def __setitem__(self, key, value):
        self._settings[key] = value

    def __getitem__(self, key):
        return self._settings[key]

    def __iter__(self):
        return self._settings.iteritems()

    def install(self, namespace, flush=False):
        """Install settings in a given namespace."""
        for key, value in self:
            if self._force_uppercase:
                key = key.upper()
            if key in namespace:
                warnings.warn('Duplicating key: %s' % key, Warning)
            namespace[key] = value
        if flush:
            self._settings = {}

