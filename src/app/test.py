import unittest


from LightTester import *

class Test(unittest.TestCase):
    
    def test_apply(self):
        a = LightTester(3)
        a.apply('toggle')
        self.assertTrue(a.lights[0][1] == True)

    def test_count(self):
        count = 0
        a = LightTester(3)
        cmd = "toggle"
        a.apply(cmd)
        self.assertTrue(a.count() == 1)

    def test_coordinates(self):
        a=LightTester(5)
        x,y,x1,y1 = 1,1,2,4
        a.coordinates(x,y,x1,y1)
        print(a.count())
        self.assertTrue(a.count() == 8)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
