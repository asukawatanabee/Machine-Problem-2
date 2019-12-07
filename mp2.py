#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:55:40 2019

@author: asukawatanabe
"""

from math import sqrt
def Circle(x1, y1, x2, y2, x3, y3) :
        x12 = x1 - x2;
        x13 = x1 - x3;
    
        y12 = y1 - y2;
        y13 = y1 - y3;
    
        y31 = y3 - y1;
        y21 = y2 - y1;
    
        x31 = x3 - x1;
        x21 = x2 - x1;
    
        sx13 = pow(x1, 2) - pow(x3, 2);
        sy13 = pow(y1, 2) - pow(y3, 2);
    
        sx21 = pow(x2, 2) - pow(x1, 2);
        sy21 = pow(y2, 2) - pow(y1, 2);
    
        f = (((sx13) * (x12) + (sy13) * (x12) + (sx21) * (x13) + (sy21) * (x13)) // 
         (2 * ((y31) * (x12) - (y21) * (x13))));
    
        g = (((sx13) * (y12) + (sy13) * (y12) + (sx21) * (y13) + (sy21) * (y13)) // 
         (2 * ((x31) * (y12) - (x21) * (y13))));
     
        c = (-pow(x1, 2) - pow(y1, 2) - 2 * g * x1 - 2 * f * y1);
        
        h = -g;
        k = -f;
        sqr_of_r = h * h + k * k - c;
        r = round(sqrt(sqr_of_r), 5);
        print("Centre = (", h, ", ", k, ")");
        print("Radius = ", r);
        l=[2*g,2*f,c]
        
        print("vector[D,E,F]",l)
              
x1,y1=map(int,input('Enter first coordinates: ').split())
x2,y2=map(int,input('Enter second coordinates: ').split())
x3,y3=map(int,input('Enter third coordinates: ').split())
              
Circle(x1,y1,x2,y2,x3,y3)