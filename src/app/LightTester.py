import re #regex module
import urllib.request
import requests
import urllib # to open and read from a URL
import numpy as np

class LightTester(object):
     
    def __init__(self,N):
        self.size = N
        self.lights = [[0]*N for _ in range(N)]
              
    def apply(self,cmd,x,y,x1,y1):
        
        if x < 0:
            x = 0
        if x > self.size-1:
            x = self.size-1
        if x1 < 0:
            x1 = 0
        if x1 > self.size-1:
            x1 = self.size-1
        if y < 0:
            y = 0
        if y > self.size-1:
            y = self.size-1
        if y1 < 0:
            y1 = 0
        if y1 > self.size-1:
            y1 = self.size-1
        
        for i in range(y,y1+1): # arrays
            for j in range(x,x1+1): 
                if cmd == 'turn on':# elements
                    self.lights[i][j] = 1
                elif cmd == 'turn off':
                    self.lights[i][j] = 0
                elif cmd == 'switch':
                    if self.lights[i][j] == 1:
                        self.lights[i][j] = 0
                    else:
                        self.lights[i][j] = 1
                else:
                    continue
        
    def count(self):
        count = 0
        for i in self.lights:
            for j in i:
                if j == 1:
                    count+=1
        return count

    def parse(self,filename):
        pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        if filename == 'data':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
        elif filename == 'dataA':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt")
        elif filename == 'dataB':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt")
        elif filename == 'dataC':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt")
        elif filename == 'dataD':
            fh= requests.get("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt")
                        
        file1 = fh.text.split('\n')

        for line in file1[1:-1]:
            sort = pat.match(line)
            if sort: #matches the regex
                arr = [sort.group(1),sort.group(2),sort.group(3),sort.group(4),sort.group(5)]
            else:
                continue 
            yield arr
        fh.close()

if __name__ == "__main__":
    LightTester().__init__
