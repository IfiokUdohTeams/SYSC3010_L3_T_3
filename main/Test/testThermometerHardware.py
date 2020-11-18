import sys
sys.path.append('..')
from Emulators import ThermometerEmulator
import sense_hat
import sense_emu 
import unittest


class TestThermometer(unittest.TestCase):  

        def test_Thermometer(self):
                thermometer = ThermometerEmulator.ThermometerEmulator()
                sense = sense_emu.SenseHat()
                # sense = sense_hat.SenseHat()
                temp1 = thermometer.read()
                # temp2 = sense.get_temperature()
                temp2 = 20.2

                thermometer.close()
                self.assertAlmostEqual(float(temp1), temp2, delta= 11.11)
                  


if __name__ == '__main__':
            unittest.main()