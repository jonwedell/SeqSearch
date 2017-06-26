#!/usr/bin/env python3

from __future__ import print_function

import re
import sys
import json

sequences = json.loads(open("ss.json",'r').read())

def contains(search):
    """ Check if search strings exist in DB separated by distance. """
    
    matches = []
    
    str1, distance, str2 = search.split(":")
    for seq in sequences.keys():
        if str1 in seq and str2 in seq:
            s1idx = [m.start() for m in re.finditer('(?=%s)' % str1, seq)]
            #print("Found for %s in idx %s" % (sequences[seq], s1idx))
            for idx in s1idx:
                start = idx+int(distance)+len(str1)
                end = start + len(str2)
                #print("comparing %s to %s" % (str2, seq[start:end]))
                if seq[start:end] == str2:
                    #print("FOUND! %s " % sequences[seq])
                    matches.extend(sequences[seq])
                    
    return sorted(list(set(matches)))

for arg in sys.argv[1:]:
    print("%s %s" % (arg, contains(arg)))
