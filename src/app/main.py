import cmd
from LightTester import *

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
        
    print("#occupied: ",lights.count())
    

def first():
    print(mainF('data',1000)) #400,410

def A():    
    print(mainF('dataA',5000)) # won't compute 

def B():
    print(mainF('dataB',11000)) #29,942,250

def C():
    print(mainF('dataC',1000)) #477,452

def D():
    print(mainF('dataD',1000)) #349,037

if __name__ == '__main__':
    main()
