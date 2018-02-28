import re #regex module
import urllib.request
import requests
import urllib # to open and read from a URL

class LightTester(object):
     
    def __init__(self,N):
        self.size = N
        self.lights = [[False]*N for _ in range(N)]
              
    def apply(self,cmd,x,y,x1,y1):
        
        for i in range(y,y1+1): # arrays
            for j in range(x,x1+1): 
                if cmd == 'turn on':# elements
                    self.lights[i][j] = True
                elif cmd == 'turn off':
                    self.lights[i][j] = True
                elif cmd == 'switch':
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    else:
                        self.lights[i][j] = True
        
    def count(self):
        count = 0
        for i in self.lights:
            for j in i:
                if j == True:
                    count+=1
        return count

    def parse(self,filename):
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        if filename == 'data':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
        elif filename == 'dataA':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt")
                        
        file1 = fh.text.split('\n')
        for line in file1[ :1]:
            N = line

        for line in file1[1:-1]:
            sort = pat.match(line) #matches the regex
            arr = [sort.group(1),sort.group(2),sort.group(3),sort.group(4),sort.group(5)]
            yield arr

if __name__ == "__main__":
    LightTester().__init__
