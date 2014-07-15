import os

import pytest

import djes


def test_install():
    ns = {}
    settings = djes.Settings()
    settings['KEY'] = 'value'
    settings.install(ns)
    assert 'KEY' in ns
    assert ns['KEY'] == 'value'


def test_force_uppercase():
    ns = {}
    settings = djes.Settings()
    settings['debug'] = True
    settings.install(ns)
    assert 'DEBUG' in ns
    ns = {}
    settings = djes.Settings(force_uppercase=False)
    settings['Debug'] = False
    settings.install(ns)
    assert 'Debug' in ns


def test_mode():
    assert djes.mode('test') == False
    os.environ['DJES_MODE'] = 'test'
    assert djes.mode('test') == True


def test_invalid_mode():
    with pytest.raises(ValueError):
        djes.mode('')


def test_is_local():
    assert djes.is_local() == False
    del os.environ['DJES_MODE']
    assert djes.is_local() == True

