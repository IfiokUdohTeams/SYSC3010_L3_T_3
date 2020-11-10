import unittest


class TestData(unittest.TestCase):
    
    def test_vaccineTemperature(self):
        
        temp_thresh = range(20,50)
        
        self.assertIn(35,temp_thresh)
        self.assertIn(70,temp_thresh)
        self.assertIn(20,temp_thresh)
        self.assertIn(50,temp_thresh)
        
    def test_vaccinePressure(self):
        
        press_thresh = range(100,500)
        
        self.assertIn(150,press_thresh)
        self.assertIn(100,press_thresh)
        self.assertIn(600,press_thresh)
        self.assertIn(50,press_thresh)
        
        
if __name__=='__main__':
    unittest.main()
        
        
        