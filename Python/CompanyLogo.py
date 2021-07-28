import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    count = dict()

    for x in sorted(s):
        count[x]=count.get(x,0)+1
    Dict_keys=sorted(count, key=count.get, reverse=True)  

    for key in Dict_keys[:3]:
        print(key,count[key])