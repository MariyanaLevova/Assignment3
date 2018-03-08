import cmd
from app.LightTester import *

def main():
    import sys
    input = sys.argv[1]
    filename = sys.argv[2]
    if filename == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt' or filename == 'data/input_assign3.txt' or filename == '--input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt':
        first()
    elif filename == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt' or filename == 'data/input_assign3_a.txt' or filename == '--input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt':
        A()
    elif filename == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt' or filename == 'data/input_assign3_b.txt' or filename == '--input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt':
        B()
    elif filename == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt' or filename == 'data/input_assign3_c.txt' or filename == '--input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt':
        C()
    elif filename == 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt' or filename == 'data/input_assign3_d.txt' or filename == '--input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt':
        D()

def mainF(filename,N):
    
    lights = LightTester(N)
    instructions = lights.parse(filename)
    
    for cmd in instructions:
        cmd0 = cmd[0]
        x = int(cmd[1])
        y = int(cmd[2])
        x1 = int(cmd[3])
        y1 = int(cmd[4])       
        lights.apply(cmd0,x,y,x1,y1)
        
    print("# of lights on: ",lights.count())
    

def first():
    mainF('data',1000) #400,410

def A():    
    mainF('dataA',5000) # 24,999,879 

def B():
    mainF('dataB',11000) #29,942,250

def C():
    mainF('dataC',1000) #477,452

def D():
    mainF('dataD',1000) #349,037

if __name__ == '__main__':
    main()
