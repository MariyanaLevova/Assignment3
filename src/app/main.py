import cmd
from LightTester import *

def main(filename,N):
    
    lights = LightTester(N)
    instructions = lights.parse(filename)
    
    for cmd in instructions:
        cmd0 = cmd[0]
        x = int(cmd[1])
        y = int(cmd[2])
        x1 = int(cmd[3])
        y1 = int(cmd[4])       
        lights.apply(cmd0,x,y,x1,y1)
        
    print("#occupied: ",lights.count())
    

def first():
    print(main('data',1000)) #400,410

def A():    
    print(main('dataA',5000)) # won't compute 

def B():
    print(main('dataB',11000)) #29,942,250

def C():
    print(main('dataC',1000)) #477,452

def D():
    print(main('dataD',1000)) #349,037

if __name__ == '__main__':
    main()
