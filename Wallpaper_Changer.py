#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:26:33 2019

@author: apurvi
"""

def get_part(hr):
    
    if hr>=5 and hr<=11:
        return "morning"

    if hr>=12 and hr<=18:
        return "day"

    #if hr>=17 and hr<=21:
       # return "evening"

    #if hr>=22 and hr<=4:
    else :
        return "night"
    
    
def change_wall(weth,part):
    
#    #clear
    print(weth)
    if(part=="morning" and weth=="clear"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/cm.jpg")
    
    elif(part=="day" and weth=="clear"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/cd.jpg")
        
    elif(part=="night" and weth=="clear"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/cn.jpg")
        
    #clouds
    
    elif(part=="night" and weth=="clouds"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/cln.jpg")
        
    
    elif(part=="morning" and weth=="clouds"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/clm.jpg")
        
    
    elif(part=="day" and weth=="clouds"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/cld.jpg")
        
    #snow
    
    elif(part=="night" and weth=="snow"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/sn.jpg")
        
    
    elif(part=="morning" and weth=="snow"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/sm.jpg")
        
    
    elif(part=="day" and weth=="snow"):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/sd.jpg")
    
    
    #rain
    elif(part=="night" and (weth=="thunderstorm" or weth=="drizzle")):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/rn.jpg")
        
    
    elif(part=="morning" and (weth=="thunderstorm" or weth=="drizzle")):
         os.system("gsetjpgtings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/rm.jpg")
        
    
    elif(part=="day" and (weth=="thunderstorm" or weth=="drizzle")):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/rd.jpg")
    
        
    #haze mist
    elif(part=="night" and (weth=="mist" or weth=="dust" or weth=="fog" or weth=="haze" or weth=="smoke")):
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/fn.jpg")
        
    
    elif(part=="morning" and (weth=="mist" or weth=="dust" or weth=="fog" or weth=="haze" or weth=="smoke")):
         os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/fm.jpg")
        
    
    elif(part=="day" and (weth=="mist" or weth=="dust" or weth=="fog" or weth=="haze" or weth=="smoke")):
         os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/fd.jpg")
    
    else:
        os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/cd.jpg")


import os
import requests
#import json
from datetime import datetime





print("hi")
url ="http://api.openweathermap.org/data/2.5/weather?q=delhi&APPID=e3e388365f7da0eaf7bad2cd46e2571c"
res=requests.get(url)

x=res.json()

weth=x["weather"][0]["main"]
print(weth)

hr=datetime.now().hour

part=get_part(hr)
print(part)
#weth="mist"
#part="day"
change_wall(weth.lower(),part)
#print('weather : ',description)

#os.system("gsettings set org.gnome.desktop.background picture)
#os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/apurvi/Desktop/python_assignment_2/wallpaper/a.jpg")
