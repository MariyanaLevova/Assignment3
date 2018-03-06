import unittest
import numpy as np


from LightTester import *

class Test(unittest.TestCase):
    
    def test_apply(self):
        a = LightTester(3)
        a.apply('switch', 0,0,1,1)
        self.assertTrue(a.lights[0][1] == 1)
        b = LightTester(5)
        b.apply('turn on',1,1,3,3)
        self.assertTrue(b.lights[3][4] == 0)
        self.assertTrue(b.lights[2][3] == 1)
        b.apply('turn off',3,0,3,3)
        self.assertTrue(b.lights[3][3] == 0)


    def test_count(self):
        count = 0
        a = LightTester(3)
        x,y,x1,y1 = 1,1,2,2
        cmd = "switch"
        a.apply(cmd,x,y,x1,y1)
        self.assertTrue(a.count() == 4)
        b = LightTester(3)
        b.apply('turn on',0,0,2,2)
        self.assertTrue(b.count() == 9)
        b.apply('turn off',1,1,4,4)
        self.assertTrue(b.count() == 5)
        #for row in b.lights:
            #print(row)

    

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
