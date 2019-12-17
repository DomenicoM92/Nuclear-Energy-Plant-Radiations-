# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'domenicomarino42@gmail.com'
__date__ = '2019-12-17'
__copyright__ = 'Copyright 2019, Marino Domenico, Ruggiero Mario'

import unittest

from qgis.PyQt.QtGui import QIcon



class energy_plant_radiation_classDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/energy_plant_radiation_class/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(energy_plant_radiation_classResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



