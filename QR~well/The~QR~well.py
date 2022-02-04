#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:58:30 2021

@author: fadewell6
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:07:21 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 05:47:37 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:03:14 2020

@author: fadewell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:54:20 2020

@author: fadewell
"""

import qrcode
#import pyqrcode
import numpy as np
#from pandas import D
import matplotlib.pyplot as plt
#import pprint
import visualisedictionary as vd
from IPython.display import Image
#from sets import Set

OPQR = list()
db = list()
ind = list()
location = []
'''
CODE before the ship variable that makes ship thing changes!!
A ship is chaotic, but simple enough to fit here
Just be careful with the instructions....
ship is always equal to the number of the assemblies plus one
'''


                                            
                        
 #   #   #    #   #   #  *****
########## \ ########## |<****
ship = 5# / #  ### # # |<****
########## \ ########## |<****
 #   #   #    #   #   #  *****


'''
CODE after the ship variable that makes ship thing changes!!
A ship is chaotic, but simple enough to fit here....
Above is the egregious ship variable; below are the arbitrary added complexity to the dictionary variable
ship @ <ship = 12> 
For every unchanged 12 value, there was a characteristic ship horn.. Replacing all 12's with ship was not an easy task, and then the laptop can be tested.
ship @ <ship = 13>  *OK*
ship @ <ship = 14>  *OK*
ship @ <ship = 15>  *OK*
ship @ <ship = 16>  *OK*
ship @ <ship = 17>  *OK*
ship @ <ship = 18>  *OK*
ship @ <ship = 19>  *OK*
ship @ <ship = 20>  *OK*
'''

import cv2
# read the QRCODE image
img = cv2.imread("QRin77pp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range (n_lines):
        #draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
       # cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
        OPQR.append( f"{data}" )

for i in range(1,ship):
   # import cv2
# read the QRCODE image
    rep = str('7p')+'0'+str(i)
    QRin77pp = str("QRin77pp.png").replace('7pp',rep)
    img = cv2.imread(QRin77pp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
          #  cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
            OPQR.append( f"{data}" )
    
dbQR = []
for i in range(0,len(OPQR)):
    c = str(OPQR[i])
    c= c.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    db.append([c])
    pars=c.split(',')
    dbQR.append(pars)
    ind.append(len(pars))
    #ind 
dQR = []
itd= []
axis0 = len(dbQR)
for i in range(0,axis0):
    axis1 = int(ind[i])
    dQR0= []
    for j in range(axis1):
      #  print(i,j)
        par = int(dbQR[i][j])
        print(par)
        dQR0.append(par)
    dQR.append(dQR0)
    ist = dQR0[0]
    itd.append(ist)
    
locations= []
location =[]
numbers = []

img2 = cv2.imread("compressedEntriesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img2)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
    #    cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
number =  f"{data}"
number = number.replace('-1','')
numbers.append(number)


for i in range(1,ship):
   # import cv2
# read the QRCODE image
    rep = str('es')+'0'+str(i)
    print(rep)
    compressedEntriesp = str("compressedEntriesp.png").replace('esp',rep)
    print(compressedEntriesp)
    img2 = cv2.imread(compressedEntriesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img2)
    
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        # display the image with lines
        # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
        #    cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
            number =  f"{data}"
            print(number)
    number = number.replace('-1','')
    numbers.append(number)
   
#numbers[10]='0113355'

pages = []

img3 = cv2.imread("Entitiesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img3)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
      #  cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
page = f"{data}"
pages.append(page)

for i in range(1,ship):
    rep = str('es')+'0'+str(i)
    Entitiesp = str('Entitiesp.png').replace('esp',rep)
    img3 = cv2.imread(Entitiesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img3)
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
        # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
          #  cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
        page = f"{data}"
    pages.append(page)
    
    
sortcode = []
AmiQR = []
ggQR = []
for i in range(len(pages)):
    axis2= len(pages[i])
    AmiQR0 = []
    for j in range(axis2):
        a = j+1
        b = j
        c = pages[i]
        d = c[b:a]
        d = int(d)
        AmiQR0.append(d)
    AmiQR.append(AmiQR0)

for i in range(len(ind)):    
    axis3 = ind[i]
    ggQR0=[0]
    for j in range (1,axis3):
        d2 = numbers[i]
        d3 = d2[dQR[i][j-1]:dQR[i][j]]
        d3= int(d3)
        ggQR0.append(d3)
    ggQR.append(ggQR0)

QRlist = []
for i in range(len(ind)):    
    axis3 = ind[i]
    QRlist0=[0]
    for j in range (1,axis3):
        e = str(ggQR[i][j])
        f = len(e)/(j+1)
        f = int(f)
        QRlist0.append(f)
    QRlist.append(QRlist0)
    
wtj = []
tCt = []
k = 1
for y in range(len(ind)):
    k = 1
    axis3 = ind[y]
    wtj0=[]
    while k < axis3:
        i=0
        istr = str(ggQR[y][k])
        j = (k+1)* QRlist[y][k]
        wtj0.append(j)
        k += 1
      #  ij = istr[i:i+k]
    wtj.append(wtj0)
    i1 = k
    tCt0= [0]
    L= ind[y] - 2
    if itd[y] != 1:
        x = 1
        while itd[y] > x:
            tCt0.append(int(numbers[y][x]))
            x+=1
    for i in range(i1-L,axis3+1):
        h = wtj0[i-2]
        for k in range (0,wtj0[i-2],i):
            istr = str(ggQR[y][i-1])
            j= istr[k:k+i]
            j = int(j)
            tCt0.append(j)
    tCt.append(tCt0)
    
files = []
file1 = open("ShipParts.txt","r") 
files.append(file1)
for i in range (1,ship):
    rep = str('Instr')+str(i)
    subtxt = str(rep)
    file1 = open(subtxt,"r") 
    files.append(file1)
    
duuxx = []
dix = []

for i in range(0,len(files)):
    dix0= files[i].readlines()
    z = np.size(dix0)
    ion = []
    files[i].close()
    for x in range(z):
        ion.append(dix0)
    dix0 = str(dix0)
    duuxx0=dix0#.replace(", \' \',", "")#.replace(", \'" , "")#.replace("[","")#.replace("]","")#.replace("'","")#.replace("\\n", "  ")#.replace(","," ")
    duuxx0=dix0.replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    tCt[i].append(-1)
    duuxx.append(duuxx0)

AmQR = []
for z in range (len(pages)):
    axis4= len(pages[z])-1
    AmQR0=[]
    for i in range (axis4):
        a = tCt[z][i]
        b = tCt[z][i+1]
        c = (str(a)+str(b))
       # c = int(c)
      #  print(c)
        AmQR0.append(c)
    AmQR.append(AmQR0)
OPQR_init = list()
db_init = list()
ind_init = list()
location_init = []

# read the QRCODE image
img = cv2.imread("QRin77pp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
    #    cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
OPQR_init.append( f"{data}" )

for i in range(1,ship):
   # import cv2
# read the QRCODE image
    rep = str('7p')+'0'+str(i)
    QRin77pp = str("QRin77pp.png").replace('7pp',rep)
    img = cv2.imread(QRin77pp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
       #     cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
            OPQR_init.append( f"{data}" )
    
dbQR_init = []
for i in range(0,len(OPQR)):
    c = str(OPQR_init[i])
    c= c.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    db.append([c])
    pars=c.split(',')
    dbQR_init.append(pars)
    ind_init.append(len(pars))
    #ind 
dQR_init = []
itd_init= []
axis0 = len(dbQR_init)
for i in range(0,axis0):
    axis1 = int(ind_init[i])
    dQR0= []
    for j in range(axis1):
      #  print(i,j)
        par = int(dbQR_init[i][j])
        print(par)
        dQR0.append(par)
    dQR_init.append(dQR0)
    ist = dQR0[0]
    itd_init.append(ist)
    
locations_init= []
location_init =[]
numbers_init = []

img2 = cv2.imread("compressedEntriesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img2)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
       # cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
number =  f"{data}"
number = number.replace('-1','')
numbers_init.append(number)

for i in range(1,ship):
   # import cv2
# read the QRCODE image
    rep = str('es')+'0'+str(i)
    print(rep)
    compressedEntriesp = str("compressedEntriesp.png").replace('esp',rep)
    print(compressedEntriesp)
    img2 = cv2.imread(compressedEntriesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img2)
    
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        # display the image with lines
        # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
       #     cv2.line(img2, point1, point2, color=(255, 0, 0), thickness=2)
            number =  f"{data}"
            print(number)
    number = number.replace('-1','')
    numbers_init.append(number)
   


pages_init = []

img3 = cv2.imread("Entitiesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img3)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
       # cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
page = f"{data}"
pages_init.append(page)

for i in range(1,ship):
    rep = str('es')+'0'+str(i)
    Entitiesp = str('Entitiesp.png').replace('esp',rep)
    img3 = cv2.imread(Entitiesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img3)
# if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
        # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
           # cv2.line(img3, point1, point2, color=(255, 0, 0), thickness=2)
        page = f"{data}"
    pages_init.append(page)
    
    
sortcode_init = []
AmiQR_init = []
ggQR_init = []
for i in range(ship):
    axis2= len(pages_init[i])
    AmiQR0 = []
    for j in range(axis2):
        a = j+1
        b = j
        c = pages_init[i]
        d = c[b:a]
        d = int(d)
        AmiQR0.append(d)
    AmiQR_init.append(AmiQR0)

for i in range(len(ind)):    
    axis3 = ind_init[i]
    ggQR0=[0]
    for j in range (1,axis3):
        d2 = numbers_init[i]
        d3 = d2[dQR_init[i][j-1]:dQR_init[i][j]]
        d3= int(d3)
        ggQR0.append(d3)
    ggQR_init.append(ggQR0)

QRlist_init = []
for i in range(len(ind)):    
    axis3 = ind_init[i]
    QRlist0=[0]
    for j in range (1,axis3):
        e = str(ggQR_init[i][j])
        f = len(e)/(j+1)
        f = int(f)
        QRlist0.append(f)
    QRlist_init.append(QRlist0)
    
wtj_init = []
tCt_init = []
k = 1
for y in range(len(ind_init)):
    k = 1
    axis3 = ind_init[y]
    wtj0=[]
    while k < axis3:
        i=0
        istr = str(ggQR_init[y][k])
        j = (k+1)* QRlist_init[y][k]
        wtj0.append(j)
        k += 1
      #  ij = istr[i:i+k]
    wtj_init.append(wtj0)
    i1 = k
    tCt0= [0]
    L= ind_init[y] - 2
    if itd_init[y] != 1:
        x = 1
        while itd[y] > x:
            tCt0.append(int(numbers_init[y][x]))
            x+=1
    for i in range(i1-L,axis3+1):
        h = wtj0[i-2]
        for k in range (0,wtj0[i-2],i):
            istr = str(ggQR_init[y][i-1])
            j= istr[k:k+i]
            j = int(j)
            tCt0.append(j)
    tCt_init.append(tCt0)
    
files_init = []
file1 = open("ShipParts.txt","r") 
files_init.append(file1)
for i in range (1,ship):
    rep = str('Instr')+str(i)
    subtxt = str(rep)
    file1 = open(subtxt,"r") 
    files_init.append(file1)
    
duuxx_init = []
dix_init = []

for i in range(0,ship-1):
    dix0= files_init[i].readlines()
    z = np.size(dix0)
    ion = []
    files[i].close()
    for x in range(z):
        ion.append(dix0)
    dix0 = str(dix0)
    duuxx0=dix0#.replace(", \' \',", "")#.replace(", \'" , "")#.replace("[","")#.replace("]","")#.replace("'","")#.replace("\\n", "  ")#.replace(","," ")
    duuxx0=dix0.replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    tCt_init[i].append(-1)
    duuxx_init.append(duuxx0)

AmQR_init = []
for z in range (len(pages)):
    axis4= len(pages[z])-1
    AmQR0=[]
    for i in range (axis4):
        a = tCt[z][i]
        b = tCt[z][i+1]
        c = (str(a)+str(b))
       # c = int(c)
      #  print(c)
        AmQR0.append(c)
    AmQR_init.append(AmQR0)        
xy = []
for z in range(len(files)):
    j=0
    i = 1
    xy0=[]
    #while i or j < np.size(tCt) or np.size(AmQR):
    while i & j < np.size(AmQR[z])-1:
    
        x=AmQR[z][j]
        #print (x)
       # qr = qrcode.make(x)
       # qr.save('entrypoints.png')
    #    img1 = cv2.imread("entrypoints.png")
        aa = AmiQR[z][j]
        i += 1
        bb = AmiQR[z][i-1]
        j +=1
        yy = x [0:aa]
        yy = int(yy)
        xx = x [aa:aa+bb]
        xx= int(xx)
       #### xy = (str(yy)+str(xx))
        xxyy =[(xx,yy)]
        xy0.append(xxyy)  
    xy.append(xy0)
for i in range(len(tCt)):
    j=1
    if i == 0 :
        while j <np.size(tCt[i])-3:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])####
         
            if j != np.size(tCt[i])-3:
                print (duuxx[i][aab:aaa-4])
            elif j == np.size(tCt[i])-3:
                print(duuxx[i][aab:aaa-2])
            print(j,aab,aaa)
    
            qr = qrcode.make(duuxx[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
         #   plt.imshow(greyy)
         #   plt.show()
            j += 1
    elif i != 0:
        while j <np.size(tCt[i])-2:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])####
         
            if j != np.size(tCt[i])-3:
                print (duuxx[i][aab:aaa-4])
            elif j == np.size(tCt[i])-3:
                print(duuxx[i][aab:aaa-2])
  #          print(j,aab,aaa)
    
            qr = qrcode.make(duuxx[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
         #   plt.imshow(greyy)
         #   plt.show()
            j += 1
            
dax = dax_init = []
p2 = p2_init=[]
p1=p1_init=[]
Subs_init =[]

for i in range(len(duuxx)):
    if i == 0 :
        p01 = tCt[i][1]
        p02 = tCt[i][len(tCt[i])-2]
        dax0= duuxx[i][p01:p02]
        dax0 = dax0.replace('   ',',').replace('rQr ', '.')#.replace(' ','')
        dax0 = dax0[:len(dax0)-3]
        dax.append(dax0)
    else:
        p01 = tCt[i][1]
        p02 = tCt[i][len(tCt[i])-2]
        dax0= duuxx[i][p01:p02]
        dax0 = dax0.replace('   ',',').replace('rQr ', '.')#.replace(' ','')
        dax0 = dax0[:len(dax0)]
        dax.append(dax0)
    p1.append(p01)
    p2.append(p02)
        
 
Subs = []  
for i in range(0,len(dax)):
    blanks= []
    if i != 0 :
        dax0= dax[i][p1[i]:p2[i]]
        dax0 = dax[i].replace('rQr',',').replace(', ',',').replace('   ',',').replace('.',',')
        dax0 = dax0[:len(dax0)-2]
        sub = dax0.split(',')
        Subs.append(sub)
    else:
        dax0= dax[0]
        dax0 = dax0.replace('.',',')#.replace(' ','')
        dax0 = dax0[:len(dax[0])]
        sub = dax0.split(',')
        Subs.append(sub)
     #   print(Subs)






Assembly ={}
#Don t forget, history repeats itself; " those who don t respect history, will repeat it " <Echiro Oda: One Piece story, Robin's claim>
Subone = [0,1,2,3,4,5,6,7,8,9,10,11,12]#,13,14,15,16,17,18,19]
Subway =[0,1,2,3,4,5,6,7,8,9,10,11,12]#,13,14,15,16,17,18,19]
Subwas =[0,1,2,3,4,5,6,7,8,9,10,11,12]#,13,14,15,16,17,18,19]
for i in range(1,ship):
    #print(i,'doux',len(Subs[i]))
    k = len(Subs[i])
    elp = []
    hel = []
    for j in range(0,k,2):
   #     print(Subs[i][j])
        elp.append(Subs[i][j])        
        hel.append(Subs[i][j+1])
    Subone[i] = elp
    Subway[i]= hel
    Subwas[i] = hel
Subone.pop(0)
Subway.pop(0)   
Subwas.pop(0)

for i in range(1,ship):
    mylist = set(Subway[i-1])
    Subway[i-1]=list(mylist)

Assembly ={}

for i in range (1,ship):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
       # print(k,j)
        for kij in range(0,k):
           # print(j,Subwas[i-1][kij],kij)
            if j == Subwas[i-1][kij]:
             #   print(kij,'here',Subone[i-1][kij][0:4])
                if Subone[i-1][kij][0:5] != 'PartS' :
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij][0:5] == 'PartS' :
                    ijk = int(Subone[i-1][kij][5:])
                   # print(Subone[ijk],'THAt') 
                    Dic.update(Assembly['PartS'+str(Subone[i-1][kij][5:])])
                    Subj.update({j:Dic})
          #      print(Subj)
        Assembly.update({'PartS'+str(i):Subj})
                
##### no sub count


Assembly ={}

for i in range (1,ship):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
       # print(k,j)
        for kij in range(0,k):
           # print(j,Subwas[i-1][kij],kij)
            if j == Subwas[i-1][kij]:
            #    print(kij,'here',Subone[i-1][kij][0:4])
                if Subone[i-1][kij][0:5] != 'PartS' :
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij][0:5] == 'PartS' :
                    ijk = int(Subone[i-1][kij][5:])
               #     print(Subone[ijk],'THAt') 
                    Dic.update({'PartS'+str(Subone[i-1][kij][5:]):Assembly['PartS'+str(Subone[i-1][kij][5:])]})
                    Subj.update({j:Dic})
             #   print(Subj)
            Assembly.update({'PartS'+str(i):Subj})


Outlist = {'Outlist':Assembly['PartS4']}
G = vd.KeysGraph(Assembly)

G.draw('./test.png')
Image('./test.png')



#############################################################################################################################################

"""
The dictionary method
Same data in reverse that will be used to search keys
"""

URDb ={}

def unichine2(Sub,Subz):
    nets = []
    for j in Sub:
        if j[0:5]!="PartS":
            nets.append(j)
        elif j[0:5]=="PartS":
            k= int(j[5:6]) - 1 
            nets.append(j)
            yets = unichine2(Subz[k],Subz)
            nets.append(yets)

    
    return(nets)

def unichine(Sub,Subz):
    nets = []
    for j in Sub:
        if j[0:5]!="PartS":
            nets.append(j)
        elif j[0:5]=="PartS":
            k= int(j[5:6]) - 1 
            yets = unichine(Subz[k],Subz)
            nets.append(yets)

    
    return(nets)

Subz = []
fk = 1
for i in Subone:
    if fk < ship:
        Subz.append(i)
        fk +=1
        
Suby = []
Subx = []
fk = 1
for i in Subwas:
    if fk < ship:
        Suby.append(i)
       # Subx = set(Suby)
        fk +=1
        
        
for i in range(len(Subz)):
    Sxb = []
    for j in range(len(Subz[i])):
        
        k = (Subz[i][j],Suby[i][j])
        Sxb.append(k)
    Subx.append(Sxb)
       # Subx = set(Suby)
       
Unicode = []
Uni2code = []
for i in range(0,len(Subz)):
    Unicode.append(unichine(Subz[i],Subz))
    Uni2code.append(unichine2(Subz[i],Subz))





def trnslate(val):
    b = int(val[5:6])-1
    return(b)
    
def trnsfuse(val):
    return()


def Omnichine2(Sub,Subx):
    nets = []
    for j in Sub:
        if j[0][0:5]!="PartS":
            nets.append(j[1])
        elif j[0][0:5]=="PartS":
            k= int(j[0][5:6]) - 1 
            
            yets = Omnichine2(Subx[k],Subx)
            nets.append(yets)
          
    return(nets)

def Omni2chine2(Sub,Subx):
    nets = []
    for j in Sub:
        if j[0][0:5]!="PartS":
            nets.append(j[1])
        elif j[0][0:5]=="PartS":
            k= int(j[0][5:6]) - 1 
            nets.append(j[1])
            yets = Omni2chine2(Subx[k],Subx)
            nets.append(yets)
          
    return(nets)

       
Unicode2 = []
Uni2code2 = []
for i in range(0,len(Subx)):
    Unicode2.append(Omnichine2(Subx[i],Subx))
    Uni2code2.append(Omni2chine2(Subx[i],Subx))




URd ={}
UMDb ={}
URdmb = {}
for i in range(0,len(Suby)):
    D1 = {}
    for j in range(0,len(Suby[i])):
        if Subz[i][j][0:5]!="PartS":
            D1 = {Subz[i][j]:{Suby[i][j]:Subz[i][j]}}
            D2 ={Subz[i][j]:0}
            D3 = {Subz[i][j]:Suby[i][j]}
            URDb.update(D1)
            URd.update(D2)
            UMDb.update(D1) 
            URdmb.update(D3)

semantic = list(URd.keys())


def unit(u,l0):
    entails =[]
    for x in range(len(l0)):
        for a in range(len(l0[x])):
            if u == l0[x][a]:
                entails.append('PartS'+str(x+1))
    return(entails)
                

semantics = []
semantics0 = []
for i in semantic:
    semantics.append(unit(i,Uni2code))
    semantics0.append(unit(i,Uni2code))
    
  
for j in range(len(semantics)):
    #if len(semantics[j]) >= 1:
      #  continue
      #  for e in semantics[j]:
          #  for k in  Subz:
             #   for f in k:
                  #  if 
    if len(semantics[j]) == 1:
        for k in range(len(Subz)):
            for f in Subz[k]:
                if f == semantics[j][0]:
                    semantics[j].append("PartS"+str(k+1))     
    elif len(semantics[j]) > 1:
        for k in range(len(Subz)):
            for f in Subz[k]:
                for e in range(len(sematics[j])):
                    if f == semantics[j][e]:
                        semantics[j].append("PartS"+str(k+1))


entailed = []
for k in range(len(semantics)):
    entailed.append({semantic[k]:semantics[k]})
    
    
    
    
sembling = []
sun = []
suun = []
for l in range(len(semantics)):
    q = 0
    for p in semantics[l]:
  #      print('voi',semantics[l],p,"==",trnslate(p),q)
        w = trnslate(p)
        
        if q == 0:
            r = [p,URdmb[semantic[l]],semantic[l],q]     
            sembling.append(r)
            suun.append(r)
            
        elif q > 0 :
            for x in range(len(Subz[w])) :
                if Subz[w][x][0:5] == "PartS" :    
                    w2 = trnslate(Subz[w][x])
                    r = [p,Suby[w][x],Subz[w][x],q]#,w,x]
                    sun.append(r)
                    sembling.append(r)   
     
        q += 1


entelei =[]



yt = []
x = 0
for i in range(len(sembling)):
    
    if sembling[i] == suun[x]:
        yt.append(i)
        x+=1


suuun = []
for z in range(1,len(yt)):
    suuun.append(sembling[yt[z-1]:yt[z]])
    
suuun.append([sembling[yt[len(yt)-1]]])
        
        
for f in range(len(suuun)):
    suuuun = []
    for u in range(len(suuun[f])):
        print(suuun[f][u][3],f,u)
        if int(suuun[f][u][3]) != 0:
            for v in semantics[f]:
                bo = False
                if suuun[f][u][2] == v:
                    bo = True 
                if bo is True:
                    suuuun.append(suuun[f][u])
        elif int(suuun[f][u][3])  == 0:
            suuuun.append(suuun[f][u])
    entelei.append(suuuun)






SS = []
GG = []
FF = []

for i in entelei:
    A = []
    B = []
    C = []
    for j in i:
        A.append(j[0])
        B.append(j[1])
        C.append(j[2])
    SS.append(A) ### Subway
    #semantics ---> Subwas, keys (comparisons)
    GG.append(B) ### Subway values
    FF.append(C) ### SS, Subone


Unsemble ={}

for i in range (1,len(SS)+1):
    Xan = {}
    for j in semantics[i-1]: 
        Dic = {}
        k = len(SS[i-1])
       # print(k,j)
        for kij in range(0,k):
            if j == SS[i-1][kij]:
                jik = GG[i-1][kij]
                ijk = FF[i-1][kij]
                ijj = SS[i-1][kij]
                if ijk[0:5] != 'PartS' :
                    Dic.update({j:{jik:{ijk:kij}}})
                    Xan.update({ijk:Dic})
                elif ijk[0:5] == 'PartS' :
                    cfd = list(Xan.keys())
                    #print(FF[kij],'THAt') 
                    #Dic.update({j:{jik:{ijk:kij}}})
                    #Dic = ({j})
                    for rof in cfd:  
                        Dic.update({jik:{ijk:Xan[rof][ijk]}})
                        Xan[rof].update({ijj:Dic})
             #   print(Subj)
            Unsemble.update(Xan)

















It = {}
At = {}
for f in entailed:
    lo = list(f.values())[0]
    lu = list(f.keys())[0]
   # print(lo,lu)
    g = 0
    

    while g < len(lo):
        h = trnslate(lo[g])
       # print(h)
        if g == 0 :
            Iet = {lo[0]:{URdmb[lu]:{lu:0}}}
            It.update({lu:Iet})
           # print(It)
            
        elif g > 0:
            if g == 1:
                for m in range(len(Subz[h])):
                    if Subz[h][m] == lo[0]:     
                      #  print('YY',lo[1],lu)
                        Iet = {lo[1]:{Suby[h][m]:{lo[0]:{URdmb[lu]:{lu:0}}}}}
                        It[lu].update(Iet)
                        
            elif g > 1:
                for m in range(len(Subz[h])):
                    if Subz[h][m] == lo[g-1]:     
                        Iet = {Suby[h][m]:It[lu]}
                       # At.update(Iet)
                        
                       # At.update({lo[g]:Iet})
                      #  print("Not",Iet)
                      #  print("")
                       # print("if", It[lu])
                        It[lu].update({lo[g]:Iet})
          #  print("defNot", At)
           # 
                    
        g += 1
    At  = {}


























def Omnichines(Sub,Subx):
    nets = []
    for j in Sub:
        if j[0][0:5]!="PartS":
            nets.append(j)
        elif j[0][0:5]=="PartS":
            k= int(j[0][5:6]) - 1 
       #     print("JJ",j,"JJ")
            nets.append(j)
            yets = Omnichines(Subx[k],Subx)
            nets.append(yets)
          
    return(nets)


def Omnichines2(Sub,Subx):
    nets = []
    for j in Sub:
        if j[0][0:5]!="PartS":
            nets.append((j[1],j[0]))
        elif j[0][0:5]=="PartS":
            k= int(j[0][5:6]) - 1 
        #    print("JJJ",j,"JJJ")
            nets.append((j[0]))
            yets = Omnichines2(Subx[k],Subx)
            nets.append(yets)
          
    return(nets)
       


Omnicodes = []
Omnicodes2 = []
for i in range(0,len(Subx)):
    Omnicodes.append(Omnichines(Subx[i],Subx))
    Omnicodes2.append(Omnichines2(Subx[i],Subx))


   
Omnicon = {}
   


        














def Omnichine(Sub,Subx):
    nets = []
    for j in Sub:
        if j[0][0:5]!="PartS":
            nets.append(j)
        elif j[0][0:5]=="PartS":
            k= int(j[0][5:6]) - 1 
          #  print("JJ",j,"JJ")
            
            yets = Omnichine(Subx[k],Subx)
            nets.append(yets)
          
    return(nets)

       
Omnicode = []
for i in range(0,len(Subx)):
    Omnicode.append(Omnichine(Subx[i],Subx))































print("")
print(" ")


uty = list(URDb.keys())

IMDb ={}
k = 0 
for i in Subz:
    k += 1
    jl = 0
    for j in i:
        IMDb.update({(k-1,jl,j):j})
        jl += 1
ff = list(IMDb.values())
fa = list(IMDb.keys())
aa = []
bb = []
for i in fa:
    jl = 0
    for j in fa:
        if i[2] == j[2] and i[0] != j[0]:
            aa.append(i)  
        if i[2][0:5] == "PartS" :
            bb.append(i)
            
bb = set(bb)
uu = []
for i in bb:
    uu.append(i)
    
    
def prci(x):
    p1 = str()
    p2 = []
    p3 = -1
    if x[0:5] == "PartS":
        p1 = int(x[5:6])-1
        p2 = Suby[p1]
     #   p3 = int(-1)
        for l in Subz[p1]:
            if l[0:5] == "PartS":
                p3 = int(l[5:6])-1
    
    return(p1,p2,p3)

def src(i):
    hk = "PartS"
    for j in range(0,len(Subz)):
        for k in Subz[j]:
            
            if k == i and i[0:5] != hk:
                hk += str(j+1)
            #elif k == i and i[0:5] == hk:
                #hk = i + str(j)
    return(hk)



for i in uty:
    URDb.update({i:{list(URDb[i].keys())[0]:{i:0}}})
    UMDb.update({i:{list(UMDb[i].keys())[0]:{i:0}}})
    
for i in uty:
    src(i)
    URDb.update({i:{src(i):{list(URDb[i].keys())[0]:{i:0}}}})
    UMDb.update({i:{src(i):{list(UMDb[i].keys())[0]:{i:0}}}})








for i in uu:
    a = i[0]
    b = i[1]
    c = int(Subz[a][b][5:6])-1
    for j in Subz[c]:
        n = "PartS"+str(a+1)
        if j[0:5] != "PartS":
      #      print(Subz[a][b],Suby[a][b],'Ohiw')#
            DN = URDb[j][Subz[a][b]]
            DM= {n:{Suby[a][b]:{src(j):DN}}}
            URDb[j].update(DM)
            prci(Subz[a][b])
        
        
        
        
for i in uu: 
    a = i[0]
    b = i[1]
    c = i[2]
    d = prci(Subz[a][b])
    c2 = prci(Subz[a][b])[0]
    n = prci(Subz[a][b])[1]
    f = prci(Subz[a][b])[2]
    for j in Subz[c2]:
        if j[0:5] == "PartS":
            #print("DDD",j,n,f,a,b)
            uf = []
         #   print(Subz[a][b],Suby[a][b],'Whoray')
            for j2 in Subz[a]:
                if j2[0:5] != "PartS":
               #     print(j2,'!=')
                   af = list(URDb[j2].values())[0].keys()
                   af = list(af)[0]
                   uf.append(af)
                 #  print(uf)
                elif j2[0:5] == "PartS":
                #    print(j2,'==')
                    f1 = prci(j2)[2]
                    fn = prci(j2)[1]
                    ff = prci(j2)[0]
                    if f1 >= 0:
                      #  print(f1,ff,'==')
                        D1= Suby[a][b]
                        D2 = Subz[a][b]
                        D3 = D2[0:5]+str(ship-1)
                        for j3 in Subz[f1]:
                            f2 = prci(j3)[2]
                           # print(prci(j3),'j3',j3)
                            if f2 >=0:
                                d =  prci(j3)[1] 
                           #     print(d,'d')
                            elif f2 == -1:
                           #     print(',,,')
                            #    print(j3)
                                mkni = URDb[j3]
                                mkno =  {D1:{D2:mkni[D2]}}
                                URDb[j3][D3].update(mkno)
            
            
            
            
 

def halting(xyz):
    #print(xyz)
    IIMDb ={}
    a = xyz[0]
    b = xyz[1]
    c = int(xyz[2][5:6]) - 1
    print(a,b,c)
    for t in Subz[c]:
        m = "PartS"+str(a+1)
        if t[0:5] != "PartS":
           # print(Subz[a][b],Suby[a][b],'Ohiw')#
            DN = UMDb[t][Subz[a][b]]
            DM= {m:{Suby[a][b]:{src(t):DN}}}
            UMDb[t].update(DM)
            IIMDb = UMDb
     #   elif t[0:5] == "PartS":
         #   print(Unicode[a][b][c+1])
            
    return(IIMDb)




for JiK in uu:
   # halting(JiK)
    UMDb.update(halting(JiK))






G = vd.KeysGraph(URDb)


G.draw('./tes1t.png')
Image('./tes1t.png')
