#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k ):
    # Write your code here
    
    
    
    if len(str(n)) == 1:
        return n
        
    n = sum(map(int,list(str(n))))
    
    n = int(n * k)
    
    return superDigit(n , 1)