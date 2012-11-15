#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Nexcess.net L.L.C.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Script to convert from Apache vhost config files to Nginx
"""

__title__       = 'apache2nginx'
__version__     = '0.1.0'
__author__      = 'Alex Headley <aheadley@nexcess.net>'
__license__     = 'GPLv2'
__copyright__   = 'Copyright (C) 2012 Nexcess.net L.L.C.'

import logging

logger = logging.getLogger(__name__)

class ConfigTree(object):
    """
    """
    pass

class BaseConfigReader(object):
    """
    """
    def __init__(self, config_file):
        """
        """
        if hasattr(config_file, 'read'):
            self._config_file = config_file
        else:
            try:
                self._config_file = open(config_file, 'r')
            except IOError as err:
                logger.warning('Unable to open config file: %s', config_file)
                raise err

    def parse(self):
        raise NotImplemented()

class BaseConfigWriter(object):
    """
    """
    def __init__(self, config_file):
        """
        """
        if hasattr(config_file, 'write'):
            self._config_file = config_file
        else:
            try:
                self._config_file = open(config_file, 'w')
            except IOError as err:
                logger.warning('Unable to open config file: %s', config_file)
                raise err

class ApacheConfigReader(BaseConfigReader):
    pass

class NginxConfigWriter(BaseConfigWriter):
    pass


if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    reader = ApacheConfigReader(in_file)
    writer = NginxConfigWriter(out_file)
    ctree = reader.parse()
    writer.write(ctree)
