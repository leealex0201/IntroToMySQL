#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:29:24 2018

@author: Alex
"""

import mysql.connector
import cookbook

try:
    conn = cookbook.connect()
    print("Connected")
except mysql.connector.Error as e:
    print("Cannot connect to server")
    print("Error code: %s" % e.errno)
    print("Error message: %s" % e.msg)
else:
    conn.close()
    print("Disconnected")