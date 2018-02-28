import main as m
from main import *

def run():
    x = input("prompt: ")
    if x == 'data/input_assign3.txt' or x == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt':
        m.first()
    elif x == 'data/input_assign3_a.txt' or x == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt':
        m.A()
    elif x == 'data/input_assign3_b.txt' or x == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt':
        m.B()
    elif x == 'data/input_assign3_c.txt' or x == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt':
        m.C()
    elif x == 'data/input_assign3_d.txt' or x == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt':
        m.D()
run()
