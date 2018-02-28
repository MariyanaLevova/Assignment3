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
        print(a.lights)
        print("count is: ",a.count())
        self.assertTrue(a.count() == 1)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
