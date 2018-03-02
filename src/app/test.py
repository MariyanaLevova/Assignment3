import unittest


from LightTester import *

class Test(unittest.TestCase):
    
    def test_apply(self):
        a = LightTester(3)
        a.apply('switch', 0,0,1,1)
        self.assertTrue(a.lights[0][1] == True)
        b = LightTester(5)
        b.apply('turn on',1,1,3,3)
        self.assertTrue(b.lights[3][4] == False)
        self.assertTrue(b.lights[2][3] == True)
        b.apply('turn off',3,0,3,3)
        self.assertTrue(b.lights[3][3] == False)

    def test_count(self):
        count = 0
        a = LightTester(3)
        x,y,x1,y1 = 1,1,2,2
        cmd = "switch"
        a.apply(cmd,x,y,x1,y1)
        self.assertTrue(a.count() == 4)

    

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
