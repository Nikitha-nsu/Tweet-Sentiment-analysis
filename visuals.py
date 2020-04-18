# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:02:47 2020

@author: Nikitha
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')

fig = plt.figure()
axis1 = fig.add_subplot(1,1,1)

def anima(i):
        
    pull = open('twitter-out.txt', 'r').read()
    print(pull)
    lines = pull.split('\n')
    
    xlist = []
    ylist = []
    
    x = 0
    y = 0
    
    for line in lines:
        
        x += 1
        if line == 'positive':
            y += 1
        elif line =='negative':
            y += -1
        else:
            y += 0
            
            xlist.append(x)
            ylist.append(y)  
            
    axis1.clear()
    axis1.plot(xlist,ylist)
            
animate = animation.FuncAnimation(fig, anima, interval = 1000)
plt.show()

           
        

    