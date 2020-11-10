import unittest


class TestData(unittest.TestCase):
    
    def test_PatientTemperature(self):
        
        temp_thresh = range(20,50)
        
        self.assertIn(45,temp_thresh)
        self.assertIn(80,temp_thresh)
        self.assertIn(10,temp_thresh)
        self.assertIn(50,temp_thresh)
        
        
if __name__=='__main__':
    unittest.main()