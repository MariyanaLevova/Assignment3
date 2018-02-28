import unittest


from LightTester import *

class Test(unittest.TestCase):
    
    def test_apply(self,cmd):
        a = LightTester(3)
        a.apply('toggle')
        
        self.assertTrue(a.lights[0][1] == True)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
