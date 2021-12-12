# coding: utf-8

import unittest

from tapioca_{{ cookiecutter.service_name}} import {{ cookiecutter.service_name}}


class TestTapioca{{ cookiecutter.service_name}}(unittest.TestCase):

    def setUp(self):
        self.wrapper = {{ cookiecutter.service_name}}()


if __name__ == '__main__':
    unittest.main()
