# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'antoni.kukowski.stud@pw.edu.pl'
__date__ = '2023-06-09'
__copyright__ = 'Copyright 2023, Antoni Kukowski / Rafał Szlendak'

import unittest

from qgis.PyQt.QtGui import QIcon



class Informatyka_proj_2DialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/Informatyka_proj_2/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(Informatyka_proj_2ResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



