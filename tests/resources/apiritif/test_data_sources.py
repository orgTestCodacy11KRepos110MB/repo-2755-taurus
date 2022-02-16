# coding=utf-8

import logging
import random
import string
import sys
import unittest
from time import time, sleep

import apiritif

reader_1 = apiritif.CSVReaderPerThread('first-file.csv', loop=True)
reader_2 = apiritif.CSVReaderPerThread('/second/file.csv', fieldnames=['bn', ' bbn'], loop=True, quoted=False, delimiter='-')


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.vars = {'cn': 'cv'}
        reader_1.read_vars()
        reader_2.read_vars()
        self.vars.update(reader_1.get_vars())
        self.vars.update(reader_2.get_vars())

        timeout = 30.0
        self.target = apiritif.http.target('http://localhost:8000/')
        self.target.keep_alive(True)
        self.target.auto_assert_ok(True)
        self.target.use_cookies(True)
        self.target.allow_redirects(True)
        apiritif.put_into_thread_store(timeout=timeout, func_mode=False, scenario_name='autogenerated_0c286c1c5a', data_sources=True)

    def _1_an(self):
        with apiritif.smart_transaction(self.vars['an']):
            response = self.target.get(self.vars['an'])

    def _2_bn(self):
        with apiritif.smart_transaction(self.vars['bn']):
            response = self.target.get(self.vars['bn'])

    def _3_cn(self):
        with apiritif.smart_transaction(self.vars['cn']):
            response = self.target.get(self.vars['cn'])

    def test_test_requests(self):
        self._1_an()
        self._2_bn()
        self._3_cn()
