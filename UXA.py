import os,re,sys,platform
 
os.system('git pull')
 
os.system('pkg install play-audio')
 
import requests
 
 
 
bit = platform.architecture()[0]
 
if bit == '64bit':
 
    from UXA1 import ud
 
    Main()
