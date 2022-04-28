#!/usr/bin/python3
import os
message = "#pythoniscool\n"
line = str.encode(message)
os.write(1, line)
