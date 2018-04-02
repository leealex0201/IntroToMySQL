#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:00:21 2018

@author: Alex
"""

import cookbook

conn = cookbook.connect()

## 1. first method
#cursor = conn.cursor()
#cursor.execute("SELECT id, name, cats FROM profile")
#while True:
#    row = cursor.fetchone()
#    if row is None:
#        break
#    print("id: %s, name: %s, cats: %s" % (row[0], row[1], row[2]))
#    
#print("Number of rows returned: %d" % cursor.rowcount)
#cursor.close()

## 2. another method - I like this method better. 
#cursor = conn.cursor()
#cursor.execute("SELECT id, name, cats FROM profile")
#for (id, name, cats) in cursor:
#    print("id: %s, name: %s, cats: %s" % (id, name, cats))
#print("Number of rows returned: %d" % cursor.rowcount)
#cursor.close()

# 3. and yet, there is one more to do this
cursor = conn.cursor()
cursor.execute("SELECT id, name, cats FROM profile")
rows = cursor.fetchall()
for row in rows:
    print("id: %s, name: %s, cats: %s" % (row[0], row[1], row[2]))
print("Number of rows returned: %d" % cursor.rowcount)
cursor.close()
    