import sys
sys.path.append('..')
from Emulators import ThermalCamera
import unittest


class TestThermalCamera(unittest.TestCase):  

        def test_ThermalCamera(self):
                thermalCamera = ThermalCamera.ThermalCamera()      
                temp1 = thermalCamera.read()
                temp2 = 32.2

                thermalCamera.close()
                self.assertAlmostEqual(float(temp1), temp2, delta= 11.11)
                  


if __name__ == '__main__':
            unittest.main()