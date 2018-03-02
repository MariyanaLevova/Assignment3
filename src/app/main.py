import cmd
from app.LightTester import *

def program(filename):
    print(filename)

def main():
    import sys
    filename = sys.argv[1]
    program(filename)
    if filename is 'data':
        first()

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
