import cmd
from app.LightTester import *

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
    
print(main('data',1000))
