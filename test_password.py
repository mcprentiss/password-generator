#!/usr/bin/env python
""" tests for random passwords """
# -*- coding: utf-8 -*-

from password import main
import re

def test_password_len():
    """ test length is long enough"""
    assert len(main()) > 10

def test_password_num():
    """ test password has a numeral"""
    assert re.search('[0-9]', main())

def test_password_letter():
    """ test password has a letter"""
    assert re.search('[A-Za-z]', main())
