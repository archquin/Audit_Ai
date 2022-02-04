#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:54:16 2022

@author: fadewell6
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 17:46:29 2022

@author: fadewell6
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:31:43 2022

@author: fadewell6
"""

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


            
'''
Chapter1
'''


##################################################################################################################################################

######  An introdoction to the analysis  #####

##################################################################################################################################################



import qrcode
import numpy as np
import matplotlib.pyplot as plt
import visualisedictionary as vd
from IPython.display import Image
import cv2

### Used libraries that are required for the shipyard Assembly QR code monitoring system to function properly 

OPQR = list()
db = list()
ind = list()
location = []

### Lists are used a lot by this program! They provided a simple and elegant solution in one's attempt to organized stored information as 

#it pleases him...


'''
CODE before the ship variable that makes ship thing changes!!
A ship is chaotic, but simple enough to fit here
Just be careful with the instructions....
ship is always equal to the number of the assemblies plus one
'''


                                            
##### The ship parameter is literally only parameter that needs manual configuration... And that is because this idea came for the UK shipyard

# in Southampton. 
                        
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





### So when simple things go wrong!!!


img = cv2.imread("QRin77pp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range (n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        OPQR.append( f"{data}" )
        
        
### The point of this algorythm was to order a set of shipbuilding related items. These items, strictly speaking can be whatever after all 

# it is why it works out, but for its first inception this the algorithm had to be co-monitoring a Lego-puzzle.

   

for i in range(1,ship):
    rep = str('7p')+'0'+str(i)
    QRin77pp = str("QRin77pp.png").replace('7pp',rep)
    img = cv2.imread(QRin77pp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            OPQR.append( f"{data}" )
    
 ### So far, no input mention has been made except that the ship variable is the only algorithm configuration that is required;

# as a manufacturing place a shipyard was theoretically interested in Parts, Processes that each part undergoes, and grouped items.

# A group of items is totally functioning driven and it involves Processed items stacks, processes, parts, and progress is involved to.

    
dbQR = []
for i in range(0,len(OPQR)):
    c = str(OPQR[i])
    c= c.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    db.append([c])
    pars=c.split(',')
    dbQR.append(pars)
    ind.append(len(pars))
dQR = []
itd= []
axis0 = len(dbQR)
for i in range(0,axis0):
    axis1 = int(ind[i])
    dQR0= []
    for j in range(axis1):
        par = int(dbQR[i][j])
        print(par)
        dQR0.append(par)
    dQR.append(dQR0)
    ist = dQR0[0]
    itd.append(ist)
    
 
    # The first idea considering monitoring was to use a note page as an input that describe a Stack of parts symbolic; the original parts

    # which are still the default choice where then consindered a special coding treat due to the a great imprompteu of the note input relying 

    # on QR code to interpret further parameterization!!!             

    
locations= []
location =[]
numbers = []

img2 = cv2.imread("compressedEntriesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img2)

if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
number =  f"{data}"
number = number.replace('-1','')
numbers.append(number)

    # Basically, to recieve input from the notes three kind of QR code is generated with a Jupyter notebook script. According to will there are
    
    # QR code labels used to identify the passage and spacing from the notes; Each space location is kept and a number is generated in a QR-code
    
    # that instructs the script about each note position as the sub-assembly. 


for i in range(1,ship):
    rep = str('es')+'0'+str(i)
    print(rep)
    compressedEntriesp = str("compressedEntriesp.png").replace('esp',rep)
    print(compressedEntriesp)
    img2 = cv2.imread(compressedEntriesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img2)
    
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            number =  f"{data}"
            print(number)
    number = number.replace('-1','')
    numbers.append(number)
   

    # Nontheless, it was too frugal to keep the commas for each blank and that deems it impossible to determine which number digit is
    
    # on which side. For this reasons, i.e. decoding the CompressedEntries input is the first task and then utilising it as is the second.
    
    # The for the decoding process two alternative QR code patterns are used varying by case.

pages = []

img3 = cv2.imread("Entitiesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img3)
if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
page = f"{data}"
pages.append(page)

    # Still the task for the system is to decypher a naumber so that every note page is a perfect fit of its contents. Instead of using,
    
    # the method on Spyder it is prefit as well as a 3-4 length list. By counting n-digit numbers, the number of numbered digit numbers 
    
    # can preciselly fit into the cypher, which was considered to be too elegant for a way, hence a more rigid QR code one is used as
    
    # other means. Instead of writing the count this QR code is a string of each number of digit and is the Entities QR-code.


for i in range(1,ship):
    rep = str('es')+'0'+str(i)
    Entitiesp = str('Entitiesp.png').replace('esp',rep)
    img3 = cv2.imread(Entitiesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img3)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
        page = f"{data}"
    pages.append(page)
    
    
    # Then pages had been decoded notes and were lain down to th elements; the first thing is the count of pages, then for each part
    
    # the description comes on the top line and the item which is described in the bottom line, or vice versa.
    
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
    
    # At this phase the algorithm starts to store the information for each QR code in different lists. Such lists include the data copy of 
    
    # QR codes and despit some minor offsets due to attention required in details as well as some getting used before one got to work with it
    
    # had been natural 
    
for i in range(len(ind)):    
    axis3 = ind[i]
    ggQR0=[0]
    for j in range (1,axis3):
        d2 = numbers[i]
        d3 = d2[dQR[i][j-1]:dQR[i][j]]
        d3= int(d3)
        ggQR0.append(d3)
    ggQR.append(ggQR0)
    
    # Decoding the pages using the QR code required to implement more lists to supply the large demmand which was a consequence of the stage
    
    # high in data and low in information

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
    
    # Lastly, an important aspect is the page naming, both in the QR-code generating stage and in the decoding stage. The filenames,
    
    # are important only for the instructions, because one needs to adapt the 'Instr' page set in order for it to be up to date!
    
    
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

    #At this point, everything has been inputed and stored in a list for further usage, and it comes to be perceiving note pages
    
    # by default as well as manipulate the contents of the page to be fit into a list!
    
for i in range(0,len(files)):
    dix0= files[i].readlines()
    z = np.size(dix0)
    ion = []
    files[i].close()
    for x in range(z):
        ion.append(dix0)
    dix0 = str(dix0)
    duuxx0=dix0
    duuxx0=dix0.replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    tCt[i].append(-1)
    duuxx.append(duuxx0)


    # To filter the excessive use of spacebar symbols, however, the list is formed by manipulating and spliting a string that seems fit.    

AmQR = []
for z in range (len(pages)):
    axis4= len(pages[z])-1
    AmQR0=[]
    for i in range (axis4):
        a = tCt[z][i]
        b = tCt[z][i+1]
        c = (str(a)+str(b))
        AmQR0.append(c)
    AmQR.append(AmQR0)
OPQR_init = list()
db_init = list()
ind_init = list()
location_init = []


    # It is important to note, that three page editing formats had to be tested to decide which list among those three has better content for
    
    # and the current format was seemed excellent for getting the task done right. 
    
img = cv2.imread("QRin77pp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
OPQR_init.append( f"{data}" )

for i in range(1,ship):
    rep = str('7p')+'0'+str(i)
    QRin77pp = str("QRin77pp.png").replace('7pp',rep)
    img = cv2.imread(QRin77pp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            OPQR_init.append( f"{data}" )
    
    
    # Basically the init forms that were used are simply a copy of the actual inputs; what used to be took the place from the current setup
    
    # predecessor, so the same data processing is necessary.
    
    
dbQR_init = []
for i in range(0,len(OPQR)):
    c = str(OPQR_init[i])
    c= c.replace('[','').replace(']', '').replace(' ', '').replace("''", "")
    db.append([c])
    pars=c.split(',')
    dbQR_init.append(pars)
    ind_init.append(len(pars))
dQR_init = []
itd_init= []
axis0 = len(dbQR_init)
for i in range(0,axis0):
    axis1 = int(ind_init[i])
    dQR0= []
    for j in range(axis1):
        par = int(dbQR_init[i][j])
        print(par)
        dQR0.append(par)
    dQR_init.append(dQR0)
    ist = dQR0[0]
    itd_init.append(ist)
    
locations_init= []
location_init =[]
numbers_init = []


    # A major issue that had been obscurring the venture was succint coding as item description, i.e. dictionary keys. The descriptive nature of
    
    # data was sufficient on itsown, hence was the preferred alternative to the more verbose and lenghty configurations prior.
    

img2 = cv2.imread("compressedEntriesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img2)

if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
number =  f"{data}"
number = number.replace('-1','')
numbers_init.append(number)

for i in range(1,ship):
    rep = str('es')+'0'+str(i)
    print(rep)
    compressedEntriesp = str("compressedEntriesp.png").replace('esp',rep)
    print(compressedEntriesp)
    img2 = cv2.imread(compressedEntriesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img2)
    
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            number =  f"{data}"
            print(number)
    number = number.replace('-1','')
    numbers_init.append(number)
   

    # Yet a lengthy configuration was assumed to be optimal for the implimentation of the CGA(Cognitive Guide Assistance), but it has 
    
    # officially dismissed as an alternative as it had more disdvantages than advantages.


pages_init = []

img3 = cv2.imread("Entitiesp.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img3)
if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
page = f"{data}"
pages_init.append(page)

for i in range(1,ship):
    rep = str('es')+'0'+str(i)
    Entitiesp = str('Entitiesp.png').replace('esp',rep)
    img3 = cv2.imread(Entitiesp)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img3)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
        for i in range(n_lines):
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
        page = f"{data}"
    pages_init.append(page)
    
    # The same process had been tested for reverse item to item descriptions; regarding that part a disctinction was made between the Subn
    
    # PartS and deemed it more practical over its descriptor location during its implementing.
    
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
    
    # Same processing as done before for the _init lists. 

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
    
    # Same principles but different values and consequently other QR-codes that were generated for each an different naming scheme;
    
    # Instr came from _init scheme, but eventually the final piece of code was lost in a fatal OS crash, so since then code was not
    
    # removed just repeat x3. There is too much nonsensical detail and it does not require any significant processing power as well
    
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
    duuxx0=dix0
    duuxx0=dix0.replace("[","").replace("]","").replace(","," ").replace("\'  \'"," ").replace("\'" , "").replace("\\n", "  ").replace("     ", 'rQr')
    tCt_init[i].append(-1)
    duuxx_init.append(duuxx0)


    # Even though the processing is an exact copy of the first processing implementation, it was difficult to reduce everything into function as

    # for the different formats involved some details had to change, and eventually it goes unnoticed!!!    

AmQR_init = []
for z in range (len(pages)):
    axis4= len(pages[z])-1
    AmQR0=[]
    for i in range (axis4):
        a = tCt[z][i]
        b = tCt[z][i+1]
        c = (str(a)+str(b))
        AmQR0.append(c)
    AmQR_init.append(AmQR0)        
xy = []
for z in range(len(files)):
    j=0
    i = 1
    xy0=[]
    while i & j < np.size(AmQR[z])-1:
        x=AmQR[z][j]
        aa = AmiQR[z][j]
        i += 1
        bb = AmiQR[z][i-1]
        j +=1
        yy = x [0:aa]
        yy = int(yy)
        xx = x [aa:aa+bb]
        xx= int(xx)
        xxyy =[(xx,yy)]
        xy0.append(xxyy)  
    xy.append(xy0)
    
    # More about the root of an error, it all started here, on string manipulation. The idea was obviously to put everything into a strict sense
    
    # of order by using a sign, though it can serve for more space of an interesting analysis.
    
    
    
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
            aab = int(ab[1])
         
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
            j += 1
    elif i != 0:
        while j <np.size(tCt[i])-2:
            aa= xy[i][j]
            a = str(aa)
            a = str(a)
            a = a.replace('[','').replace('(','').replace(']','').replace(')','')
            ab = a.split(',')
            aaa = int(ab[0])
            aab = int(ab[1])
         
            if j != np.size(tCt[i])-3:
                print (duuxx[i][aab:aaa-4])
            elif j == np.size(tCt[i])-3:
                print(duuxx[i][aab:aaa-2])
    
            qr = qrcode.make(duuxx[i][aab:aaa-4])
            qr.save('partEntities.png')
            img1 = cv2.imread("partEntities.png")
            greyy = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
            data, bbox, straight_qrcode = detector.detectAndDecode(img1)
            j += 1
            
dax = dax_init = []
p2 = p2_init=[]
p1=p1_init=[]
Subs_init =[]


    # After the processes were done symbols became more convoluted.. Not only is the objective more direct and sensing oriented but 
    
    #it gets more and more abstract as now the algorithm possesses full control of pages and has listed indexes for everything.
    
    # What is more is that generating QR - code for the monitoring parts can be accomplished only in the vicinity of an Assembly dictionary;
        
    
for i in range(len(duuxx)):
    if i == 0 :
        p01 = tCt[i][1]
        p02 = tCt[i][len(tCt[i])-2]
        dax0= duuxx[i][p01:p02]
        dax0 = dax0.replace('   ',',').replace('rQr ', '.')
        dax0 = dax0[:len(dax0)-3]
        dax.append(dax0)
    else:
        p01 = tCt[i][1]
        p02 = tCt[i][len(tCt[i])-2]
        dax0= duuxx[i][p01:p02]
        dax0 = dax0.replace('   ',',').replace('rQr ', '.')
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
        dax0 = dax0.replace('.',',')
        dax0 = dax0[:len(dax[0])]
        sub = dax0.split(',')
        Subs.append(sub)



### However, it is important to put Sub-assemblies together and use interim product progress a prerequisite to form an assembly, hence 

    # for a dictionary variable that represents the entity it describes as assembly and can be visualised the linking key word "PartSn"
    
    # was by far the superior alternative. 


Assembly ={}
Subone = [0,1,2,3,4,5,6,7,8,9,10,11,12]#,13,14,15,16,17,18,19]
Subway =[0,1,2,3,4,5,6,7,8,9,10,11,12]#,13,14,15,16,17,18,19]
Subwas =[0,1,2,3,4,5,6,7,8,9,10,11,12]#,13,14,15,16,17,18,19]
for i in range(1,ship):
    k = len(Subs[i])
    elp = []
    hel = []
    for j in range(0,k,2):
        elp.append(Subs[i][j])        
        hel.append(Subs[i][j+1])
    Subone[i] = elp
    Subway[i]= hel
    Subwas[i] = hel
Subone.pop(0)
Subway.pop(0)   
Subwas.pop(0)

    # Furthermore, as the dictionary is visualised one can really grasp to the ideal list contents, which need to be clear and constrict for the
    
    # processes to work properly. 

for i in range(1,ship):
    mylist = set(Subway[i-1])
    Subway[i-1]=list(mylist)

    # Three lists namely: Subone, Subway, and Subwas are created to host the contents of the Assembly and gracefully order them in a dictionary
    
    # structure. 

Assembly ={}
for i in range (1,ship):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
        for kij in range(0,k):
            if j == Subwas[i-1][kij]:
                if Subone[i-1][kij][0:5] != 'PartS' :
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij][0:5] == 'PartS' :
                    ijk = int(Subone[i-1][kij][5:])
                    Dic.update(Assembly['PartS'+str(Subone[i-1][kij][5:])])
                    Subj.update({j:Dic})
        Assembly.update({'PartS'+str(i):Subj})
                
        
        # The system's governor is the ship variable; after further research on the ordering problem, the following method of
        
        # ordering has been proposed. Moreover, for the Assembly variable to be formed an archtypical breakdown is believed to be the critical 
        
        # approach; to put the archtype simple that is the ship variable in a sense, and an allegoric story.
        
        
        
##### no sub count
Assembly ={}
for i in range (1,ship):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
        for kij in range(0,k):
            if j == Subwas[i-1][kij]:
                if Subone[i-1][kij][0:5] != 'PartS' :
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij][0:5] == 'PartS' :
                    ijk = int(Subone[i-1][kij][5:])
                    Dic.update({'PartS'+str(Subone[i-1][kij][5:]):Assembly['PartS'+str(Subone[i-1][kij][5:])]})
                    Subj.update({j:Dic})
            Assembly.update({'PartS'+str(i):Subj})

    
    # One reduced his page notes into three simple lists according to the ship' construction site claiming for which
    
    #then he went back to the Subone list and asked himself for Assembling the ship, what is in it each stage? Subone shared index
    
    # with Subwas so this way the index could be used to match the two lists and provide information of each stage and each item in
    
    # that stage, i.e. Subone and Subwas! However, when updating a dictionary with a forloop there s a problem when you update the 
    
    #same item pair twice or item- other item pair cause the program finds the last data update only more convenient. To add that
    
    #dimension of order the new and third created list Subway is a copy of Subwas but has no duplicates. That was if he finds the same
    
    #thing on Subwas he goes through to update the Subway item only and that allows it to branch duplicates correctly!
     





Outlist = {'Outlist':Assembly['PartS4']}
G = vd.KeysGraph(Assembly)

    # Finally, the exact and accurate representation of the distiluted archetypical variable was opting to take an exact shape for which the last
    
    # key value would be the depict and accurate representation of: the Parts that will have been involved, ordered by virtue of proximity but
    
    # through the virtue of a process!!!
    
    
    
    
        

G.draw('./test.png') 

# That was to say pushing the raw-ish setup, where lists are omited, in its recursive dead ends; thought since the triple list interpretation

# one was able to even quantify the milenium falcon for which it has been safely concluded  that in no other case Assembly s compound form

# the is pressed so much, so this proposition works!!!  

Image('./test.png')



    
'''
Chapter2
'''



########################################## Implementation of monitoring resolution  ########################################################

# Instructions as a matter of implementation. 

#############################################################################################################################################

"""
The Assembly dictionary archetype method
Other than data is in reverse is to enable an Ensemble 
"""




 ### Therefore, resulting variable for given inputs that can be yield by two different techniques, one of which, the more focused one 

# was to create an algorithm that manually reverses the variable to provide adequate nesting result. 
 
  
    
    
URDb ={}

    ##The creation of the URDb dictionary in this case is at the end of the script, and the given reversal alternative can only be correct
    
Unsemble ={}

    ## iff Unsemble and URDb are a Tautology, assuming that URDb as provided is formated by human while following a database auditing procedure;
    
    # it is claimed to be accomplishing the intricate task of making an Assembly entity possibly monitorable by printing in each part QR-code
    
    # with the entire operational region. 
    
    
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


##### The first observation is that the number of values is distributed among a specific number of given Sub-assembly keys due to the nature 
    
# of the organization process for which monitoring has been proved. Moreover, the items of the Assembly are stored in the Subone

Subz = []
fk = 1
for i in Subone:
    if fk < ship:
        Subz.append(i)
        fk +=1
        
        
# Hence it was helpful to isolate the list indexes within input's range and form them into a new "Subz" list 

   
        
Suby = []
fk = 1
for i in Subwas:
    if fk < ship:
        Suby.append(i)
        fk +=1
            
#In a similar fashion a new "Suby" list was helpful to isolate the description of the items of the Assembly in an organised way

                
        
Uni2code = []
for i in range(0,len(Subz)):
    Uni2code.append(unichine2(Subz[i],Subz))

#Now with the newly created lists it was further deemed necessary to create a list of lists for both cases.

#Moreover, such considered to be in better order because it results 

                #! in the clarification of "PartS" to list parts order as in Uni2code next index     
                
                #! in the creation of a more uniform list, which included factoring entailments.
                


def trnslate(val):
    b = int(val[5:6])-1
    return(b)
    


####  The issue of is that for the a FIFO setup the same items is that one needs to have address the depth of the Assembly, and it was 

####challenging to find an unequivocal way or the point becomes a scavenging loop. 

#### Instead of going for all common ground to be utilized as means of confronting the reversal of the Assembly variable at any given depth!




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

    #Given that to create the list of item inputs provided, a dictionary datatype is used as a form of a set of keys


semantic = list(URd.keys())


    #Then through that unique set of URd keys, a new list semantic comprised of these elements provides a framework  




def unit(u,l0):
    entails =[]
    for x in range(len(l0)):
        for a in range(len(l0[x])):
            if u == l0[x][a]:
                entails.append('PartS'+str(x+1))
    return(entails)
                
    #Using the semantic list items a starting point was identifiable for each item, i.e. the first input trace


semantics = [] 
semantics2 = []
semantics3= []
semanticss = []
###  The second observation is that: semantics <----> Subwas

for i in semantic:
    semantics2.append(unit(i,Uni2code))
    #In case of multiple traces a function would be used to write-off each input trace in terms of "PartS"

for i in range(len(semantics2)):
    semantics.append([semantics2[i][0]])
    semantics3.append([semantics2[i][0]])


for j in range(len(semantics)):
    for i in range(len(semantics2[j])):
        semantics3[j] = [semantics2[j][i]]
        if i == 0:
            if len(semantics[j]) == 1:
                for k in range(len(Subz)):
                    for f in Subz[k]:
                        if f == semantics[j][0]:
                            semantics[j].append("PartS"+str(k+1))     
            elif len(semantics[j]) > 1:
                for k in range(len(Subz)):
                    for f in Subz[k]:
                        for e in range(len(semantics[j])):
                            if f == semantics[j][e]:
                                semantics[j].append("PartS"+str(k+1))
        elif i >  0:
            
            if len(semantics3[j]) == 1:
                for k in range(len(Subz)):
                    for f in Subz[k]:
                        if f == semantics3[j][0]:
                            semantics3[j].append("PartS"+str(k+1))     
            elif len(semantics3[j]) > 1:
                for k in range(len(Subz)):
                    for f in Subz[k]:
                        for e in range(len(semantics3[j])):
                            if f == semantics3[j][e]:
                                semantics3[j].append("PartS"+str(k+1))
            kkkk = [semantics[j],semantics3[j]]
            semantics[j] = kkkk

    ##Furthemore, there was an observation here!! There is a build-up!
        
        # The list semantics was comprised from singular "PartS" elements only. In turn, reasonin suggests that, due to item entailment
        
        # list's semantics indexes are sufficient information to configure a working setup.   
        
for i in range(len(semantics)):  
    semantics2[i] = semantics[i]
    if len(semantics3[i]) > 1:
        semantics2[i] = semantics[i][0]
        
        
SS = []### Subway
#!semantics ---> Subway to Subwas, values (comparison)!!
    
GG = []### Subway values
FF = []### SS, Subone second values for each Subway[x][y]

    
    
sembling = []### All inputs
sun = []###Every 'PartS' input that is not first
suun = []
suun1 = []###Every first 'PartS' input
suun2 =[]

###### After having a list of semantical entailments, such semantics, it is easy to produce a frontground that allows drawing inferences.

for l in range(len(semantics)):
    q = 0
    for p in semantics2[l]:
        w = trnslate(p)
        if q == 0:
            r = [p,URdmb[semantic[l]],semantic[l],q]     
            sembling.append(r)
            suun1.append(r)
            suun.append(r)
            
        elif q > 0 :
            for x in range(len(Subz[w])) :  
                if Subz[w][x][0:5] == "PartS" :    
                    r = [p,Suby[w][x],Subz[w][x],q]
                    sun.append(r)              
                    sembling.append(r)   
        q += 1
    if len(semantics3[l]) > 1:
        for n in range(1,len(semantics[l])):
            qn = 0
            for p1 in semantics[l][n]:
                if qn == 0:
                    w2 = trnslate(p1)
                    r = [p1,URdmb[semantic[l]],semantic[l],0] 
                    suun2.append(r)
                qn += 1
            suun1[l] = [suun1[l],suun2[0]]

#The inferences drawn that are from the indexes of elements are shared between semantics and semantic, hence for each 'PartS' of semantics all 

#semantic elements can firstly be inspected and then be used at various indexes to a list "sembling", which shall include all the necessary 

#information by virtue of being extended to two lists which are first entry only the suun, and ~other than first entries only entries the sun.       



zlast =[]
yt = []
x = 0
for i in range(len(sembling)):
    
    if sembling[i] == suun[x]:
        yt.append(i)
        x+=1

###### THat being said onfiguring the all value i of sembling[] list to match the size of i of semantics[] list can be implemented using the first

#entry only list due to the fact that it is a direct comparison between the first entry only and all the rest 

suuun = []### pattern of the non-trivial occurences
suuun1 = []
suuun2 = []
for z in range(1,len(yt)):
    suuun.append(sembling[yt[z-1]:yt[z]])
    suuun1.append(sembling[yt[z-1]:yt[z]])
    suuun2.append(sembling[yt[z-1]:yt[z]])

suuun.append([sembling[yt[len(yt)-1]]])
suuun1.append([sembling[yt[len(yt)-1]]])
suuun2.append([sembling[yt[len(yt)-1]]])
        
###In other words, between non-trivial occurences all possible combinations of the entity's elements


uuun = []
uun = []
un = []
for i in range(len(suun)):
    if suun[i] != suun1[i]:
        uun.append(i)
        
        for j in suun1[i]:
            suuun2[i][0] = j
            uuun.append(suuun2[i])
            
        un.append(uuun)
     
        
for i in range(len(uun)):
    suuun1[uun[i]] = un[i]


for i in range(len(suuun1)):
    if suuun[i] != suuun2[i]:
        suuun1[i][0] = suuun[i]
        
         
    
for f in range(len(suuun)):
    suuuun = []
    for u in range(len(suuun[f])):
        if int(suuun[f][u][3]) != 0:
            for v in semantics2[f]:
                bo = False
                if suuun[f][u][2] == v:
                    bo = True 
                if bo is True:
                    suuuun.append(suuun[f][u])
        elif int(suuun[f][u][3])  == 0:
            suuuun.append(suuun[f][u])
    zlast.append(suuuun)

zlast1 = []
for f in range(len(suuun)):
    suuuun  = []
    if suuun[f] != suuun1[f]:
        for c in range(1,len(semantics[f])):
            for u in range(len(suuun1[f][c])):
                print(f,c,u)
                if int(suuun1[f][c][u][3]) != 0:
                    for v in semantics[f][c]:
                        bo = False
                        if suuun1[f][c][u][2] == v:
                            bo = True 
                        if bo is True:
                            suuuun.append(suuun1[f][c][u])
                elif int(suuun1[f][c][u][3])  == 0:
                    suuuun.append(suuun1[f][c][u])
        zlast1.append(suuuun)


            ####        zlast if an item is included it is entailed, if not it is yet again entailed. Wheather or not was identifiable
            
                ####        by directly assessing its index on the elements of semantics list. 
            
                    ####      I.e., if suuun[f][u][3] it is zero is non-trivial, hence kept, and if it is not zero it is a triviality
                
                       ####       hence, when it doesn t match with no additional data according to semantics list index, it was discarded!!!
zlast2 = []

for i in range(len(semantics3)):
    if len(semantics3[i]) > 1:
        zlast2 = [zlast[i]] + zlast1
        zlast[i] = zlast2
        
for i in range(len(zlast)):
    if len(semantics3[i]) == 1:
        A = []
        B = []
        C = []
        for j in zlast[i]:
            
            A.append(j[0])
            B.append(j[1]) #Further distinctions
            C.append(j[2])
            
        SS.append(A) ### Subway <---> SS
        #semantics ---> Subwas, entails Subway ---->  SS, entails semantics
        GG.append(B) ### Subwas values <---> GG
        FF.append(C) ### if SS, then through the exact SS[x][y] one can add the recreate an alternative Assembly dictionary, as in Subone[x][y] <--
        #-> FF[i][j] ---> GG[i][j] <---> SS[i][j] !! indicates next position !!
    elif len(semantics3[i]) > 1:
        AA = []
        BB = []
        CC = []
        for k in range(len(semantics[i])):
            A = []
            B = []
            C = []
            for j in zlast[i][k]:
                A.append(j[0])
                B.append(j[1]) 
                C.append(j[2])
            AA += [A]
            BB += [B]
            CC += [C]
        SS.append(AA) 
        GG.append(BB) 
        FF.append(CC) 
HH = semantics








gg2= []
for i in GG:
    yy = dict()
    for j in i:
        print(j)
        yy.update({j:0})
    uu = list(yy.keys())
    gg2.append(uu)

UU = gg2


DD =[]
for i in FF:
    DD.append(i[0])
    
##DD--->SS-->GG<-->UU-->FF
    
def gWiX(RT,l,m,n,o,p):
    Q = {}
    for x in range(0,RT):
        print(x)
      #  if x == 0:
            
       # elif x > 0:
            
    return(Q)

Unsemble= {}
for i in range(0,len(GG)):
    print('DD.',DD[i])    
    

for i in range (1,len(SS)+1):
    Xan = {}
    for j in semantics[i-1]: 
        Dic = {}
        Dic2= {}
        Dic3 = {}
        k = len(SS[i-1])
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
                    if GG[i-1] == UU[i-1]:
                        for rof in cfd:  
                            Dic.update({jik:{ijk:Xan[rof][ijk]}})
                            Xan[rof].update({ijj:Dic})
                    elif GG[i-1] != UU[i-1]:
                        cfd = list(Xan.keys())
                    
                        for rof in cfd:  
                            Dic2.update({jik:Xan[rof][ijk]})
                            for jj in semantics[i-1]: 
                                if ijj == jj:
                                    Dic3.update({ijk:Dic2[jik]})
                                    print(Dic3)
                            Xan[rof].update({ijj:{jik:Dic3}})
                            break
            Unsemble.update(Xan)
            
            

G = vd.KeysGraph(Unsemble)


G.draw('./tesX1t.png')
Image('./tesX1t.png')
    
    
    
    
    
    

### After determining the valid situations the elements can be further grouped according to produce operational parameters

#that would rely on pattern organization which accesses max depth without needing more for loops to readjust

# An archetype of the dictionary is formed step by step, which providing that data is database catered works with key and value principles.


        
        ####  using the same dictionary method as in the creation of an Assembly variable!!!   


'''
for i in range (1,len(SS)+1):
    Xan = {}
    for j in semantics[i-1]: 
        Dic = {}
        k = len(SS[i-1])
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
                    for rof in cfd:  
                        Dic.update({jik:{ijk:Xan[rof][ijk]}})
                        Xan[rof].update({ijj:Dic})
            Unsemble.update(Xan)
            
            

G = vd.KeysGraph(Unsemble)


G.draw('./tesX1t.png')
Image('./tesX1t.png')


Unsemble = {}
for i in range (1,len(SS)+1):
    Xan = {}
    for j in semantics[i-1]: 
        Dic = {}
        Dic2={}
        Dic3={}
        k = len(SS[i-1])
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
                    
                    for rof in cfd:  
                        Dic2.update({jik:Xan[rof][ijk]})
                       # print(ijj,jik,ijk,Dic2[jik])
                        
                        for jj in semantics[i-1]: 
                            if ijj == jj:
                                Dic3.update({ijk:Dic2[jik]})
                                print(Dic3)
                        Xan[rof].update({ijj:{jik:Dic3}})
                        break
            Unsemble.update(Xan)
'''


            
             #### the Assembly dictionary method takes standard items for granted and then for every compound item, i.e. "PartS" it utilizes
             
             #the previously established knowledge to append on the current knowledge stack of information.
             
             #it is simple and straightforward, the Unsemble of this example,which had been updated for every item value by having 
             
             # first factored the items and then a sequence of "PartS" that had been established through the FF list of order.
             
             #Nonetheless, the idea is that the first element of an FF is an item and then for every other SS index holds the next of the se-
             
             #quence, i.e. the current one in terms "PartS" key position, while the item description for all that is non trivial can be determ-
             
             #ined using the same index on list of item description GG. Although, in order to evaluate the item description one must first,
             
             #have SS determined for which GG is implied by FF index. Lastly, when the FF index is trivial a sequence of keys is used
             
             #in order to address direct changes inductively!!
             
             




'''
Chapter3
'''


##################################################################################################################################################

##########################################          Analysis of a sound approach                    #############################################

##################################################################################################################################################



'''
                    In a paper long ago, in a far away county,

The issue of a FIFO setup for the same items is that one needs to address the depth of the Assembly, and should be assessable 
equivocally by default....




! First figuring the constants of a dictionary

uty = list(URDb.keys())
!.


!! first dict.update{} for the constants to be according to the values and then the gathering of additional puzzle pieces 

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
!!.            




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
    return(hk)


!!! Going layer by layer until dictionary keys are not discernable so a setup is attempted for obtaining some critical values

for i in uty:
    URDb.update({i:{list(URDb[i].keys())[0]:{i:0}}})
    UMDb.update({i:{list(UMDb[i].keys())[0]:{i:0}}})
    
...! filtering the list of constants ...!! doing the second dictionary update() for more data, such as nested keys.
    
for i in uty:
    src(i)
    URDb.update({i:{src(i):{list(URDb[i].keys())[0]:{i:0}}}})
    UMDb.update({i:{src(i):{list(UMDb[i].keys())[0]:{i:0}}}})


!!!.. As by that point all the values have been updated with a nested key, i.e. providing a draft for actual Unsemble that is required to be 




!!!. key values are identified for which the depth is at least two or more, i.e. at this point it becomes obscure...




!!!! one dictionary update for the keys that are confirmed within the "Nest" 

for i in uu:
    a = i[0]
    b = i[1]
    c = int(Subz[a][b][5:6])-1
    for j in Subz[c]:
        n = "PartS"+str(a+1)
        
        ...!!! But are not actually nesting items
        
        if j[0:5] != "PartS":
            DN = URDb[j][Subz[a][b]]
            DM= {n:{Suby[a][b]:{src(j):DN}}}
            URDb[j].update(DM)
            prci(Subz[a][b])
        
        
...!!!! And afterwards, using the more detailed sketch and the unconfound key values, one has to proceed to discern the data precisely. 
    
for i in uu: 
    a = i[0]
    b = i[1]
    c = i[2]
    d = prci(Subz[a][b])
    c2 = prci(Subz[a][b])[0]
    n = prci(Subz[a][b])[1]
    f = prci(Subz[a][b])[2]
    for j in Subz[c2]:
        
        ..!!! Due to obscurity, a for loop is used to shed light in case an item is nesting other values.
        
        if j[0:5] == "PartS":
            uf = []
            for j2 in Subz[a]:
                
                 ...!!! But are not actually nesting items
                
                if j2[0:5] != "PartS":
                   af = list(URDb[j2].values())[0].keys()
                   af = list(af)[0]
                   uf.append(af)
                   
                   
                   
                elif j2[0:5] == "PartS":
                    
                    
                    f1 = prci(j2)[2]
                    fn = prci(j2)[1]
                    ff = prci(j2)[0]
                    if f1 >= 0:
                        D1= Suby[a][b]
                        D2 = Subz[a][b]
                        D3 = D2[0:5]+str(ship-1)
                        
                        .!!! Due to obscurity, a for loop is used to shed light in case an item is nesting other values.
                        
                        for j3 in Subz[f1]:
                            f2 = prci(j3)[2]
                            if f2 >=0:
                                d =  prci(j3)[1] 
                            elif f2 == -1:
                                mkni = URDb[j3]
                                mkno =  {D1:{D2:mkni[D2]}}
                                URDb[j3][D3].update(mkno)
            
            ############ 
                Instead of the Unsemble, the URDb dict was addressing a depth larger than the actual setup and it goes on and on and on!
            As the URDb is fated to work on the example it is excellent to see that the condition (Unsemble == URDb) for dictionary equality
            prints True, i.e. the Unsemble's True potential.
            
            
 

def halting(xyz):
    IIMDb ={}
    a = xyz[0]
    b = xyz[1]
    c = int(xyz[2][5:6]) - 1
    print(a,b,c)
    for t in Subz[c]:
        m = "PartS"+str(a+1)
        if t[0:5] != "PartS":
            DN = UMDb[t][Subz[a][b]]
            DM= {m:{Suby[a][b]:{src(t):DN}}}
            UMDb[t].update(DM)
            IIMDb = UMDb
            
    return(IIMDb)

    Again, not long after I was trying to address the depth of the Assembly, because let the URDb equivocally assume ending 
and by default you cannot add more Subassemblies or self contradiction is confronting one!!!



for JiK in uu:
    UMDb.update(halting(JiK))
    
    
'''


G = vd.KeysGraph(Unsemble)


G.draw('./tesXt.png')
Image('./tesXt.png')

"""
Chapter 4
"""

#################################################################################################################################################

####################                                    Percpective of the idea                             #####################################

#################################################################################################################################################

#No more titanics, a similar monitoring approach, the contemporarily method, is in use by 75% of the shipyards in the world mostly

# in Asiatic country's. Contrary to the high ground that CGA technology possesses, the shipyards in the UK would actually avoid the risk of 

# implementing other monitoring system, and as such shipbuilding in the UK remains an empirical concept. About one thing that the UK shipbuilders

# are right was that achieving implementation of monitoring with system is practically a challenge and requires inscroutable means

# On the one hand, in Asia former databases such as mySQL run the monitoring, which given the interactive way of using a clever QR scanner,

# provides the system with the necessary condition to work conclusively and to operate in the digital frame whatsoever.


# Moreover, the monitoring of a system has been tested; it could monitor a cop car puzzle assembly, hence, it can be generalised further;

# The puzzle had a similar order as a shipbyard and after conducting it using that algorithm a facility s actual operation was constantly 

# and consistently in check. Although in an impractical way, which was sticker changes, it gave a great sense of importance in detail that

# would have been missed otherwise.

   
# About the ordering solution, where Subwas replied to Subone calling; by sheding light on its mitigrated high index values it allowed 

# the Assembly to reach a neighbooring place and determine the coin's flip side. It would have been by choice that for each element index 

#two lists had been sharing the same space but different form. When it came to synthesis it was therefore clear how to proceed, yet 

#still the question of how does it make no sense when the same thing is twice to just use twice persisted. Consequently 
    
# after a note was made for such thing by brilliant scavenging of for loops, and while having tried to shed light with his index 
    
# getting rid of the triviality required a new list that would include no duplicates at all struct. 

# Subwas, + Subone = Subway
    
# Before the time that the Assembly dictionary variant worked correctly at moste cases but abused Ram; brute forcing the pattern on the
    
#dictionary straight in an attempt get everything done with two lists. This would just result in more in the same problems without aleviating
    
# the situation if one was to nest values far appart many times due to the dimensional strain that updating dictionary kept causing.

    
# Needless to say, keeping a list of every input instead of straight up admiting a pattern was a good of determining the whereabouts
 
# of everything that would ever happen. No matter how obscure or senseless the input had become there was a pattern and the contents 

#ones note pages could be ordered!


# To elaborate on that claim, one tried to come up with an absurd data structure for the algorithm to push it and make it break, so he tried to

# order "StarWars III, the revenge of the Sith. A nice movie where the Protagonist is destined to lose his meaning. Hence, after converting any 

# sample of paper note into an Assembly as well as succesfully construing the monitoring plan was ready, the tragic fate was that only half

#of the problem was solved, which was the easier part. From the demonstration of Lego policeman, the importance of a second item 

# variable to unlock an Assembly became evident. All while proceeding with the millenium Falcon lego data variable creation, an iconic puzzle

# with over a thousand pieces to monitor, not only the assembly variable was virtually inaccessible for the audit but also traditional ways

#of making it work to achieve monitor were to ineffective at that scale.

    
# Nevertheles, achieving monitoring is about by assessing the Assembly dictionary. I.e. All or nothing in terms of functionality.
    
# Any sense of order such that is characterized by an Assembly variable will is just a cool constant after all; it cannot persistently answer 

#questions about data structure editing or whether things are proper or improper, but it can show the exact information location 

#for any item anywhere inside if knowledge is used along.  


#So to make dictionaries work as Assembly works, one needs to make ammends with surveillor in a LIFO (First in Last out setting) mode, 

#i.e. all items are correctly nested in the right keys, as by default now so a weird surveillance officer is confounded from a mediocre quality

# of a logistic life. He knows which part is it, and as he tries to inspect it, he can try to use the Assembly variable from which he loses

# patience because for such part that he has in mind Assembly has used to add it to the ship randomly as well as inconsistently .

# Hence, on various occasions that Assembly dictionary is correct if not to illustrate a percpective for each part the surveilor fails 

# his duty if he tries to use monitoring and expresses facts by claiming "this will not work" .


#### That said,  an invocation of the FIFO (First in First out) variable setting of the same entity, provides the necessary perspective

# to achieve sufficient monitoring, even for the surveillor! A monolithic assembly map, road to assembly can be used this way now.

# First the surveilor wants to inspect a part, but attempting to use the Assembly variable leads him to a dead end. So he proceeds

# by using the Unsemble variable, i.e.the multi nested dictionary reversal of the Assembly for that specific part. This way the surveilor

#now posseses all the code he needs to access remote datastructure keys. He presumably knows in what location of the factory events that

# take place are at so he quickly narrows down in that order all information he requires and so he moves to inspect a next part. 


#### Unsemble the database works in FIFO (First in Last out setting), i.e. all items that are correctly nested the keys and their values

#### are correct which in turn allows the use of each and every Unsemble list of values to be used as the keys for the entire Assembly variable





    #Hence, one can finally underestand what is the other part of a resolution, i.e. reversal and trivialties.
    
    # in a hypothetical manner if using a default archetype to make the Assembly database there should be a way of recreating that
    
    # other value ordering through a similar archetypical format. However, this time everythin has to be implement from the scratch,
    
    # no scavenging, but does that even work?
    


    
    # By acknowldging that the human factor has always contemplated a lot, while using that kind of imposing 
    
    #variables for itsown sake the anticipated new archetype has to somewhat absurd every time. Imagine having a dimensional archetype
    
    # how can you reverse the dimensions? Finding the first order and the swapping the ship case with number of semantic items seems to be 
    
    # the correct way. The first dimension is simple, one can just change the lenght, however, are these two archetypes even comprised by
    
    # the same number of dimensions or what is it going on there, are there any darker secrets that are hidden? 
    
    
    
    #Thankfuly the first index showed up for the cast of a reversal; from that it can t be stated the first dimension reverse 
    
    # has anything to do with other higher parameter reverse. To make matters worse, the nature of this reversal suggests that
    
    # there is no veritable conformity that simultaneously holds for both sides of items and other-items unless there are all unique
    
    # from the start. Now that the first index is determined, one can make excellent use of it; he can go through all the new keys
    
    # that shall prevail over other data without needing to demolish the new dictionary every time, which is what scavengers would do.
    
    
    #Moreover, it is possible to use the previous structure as reference and the new index in attempt to assimilate every change
    
    # at terms of the right measure. Okay, certaintly there is nothing strange so far, however, terms must be defined; one thing is 
    
    # for sure, it is impossible to utilize a current Assembly variable to do the reversal. Nonetheless, according to order and the 
    
    #remaints of the previous lists, it is also possible to determine the first whereabout of each new key in terms of 'PartS'. 
    
    # Here the reversal of the second and third dimensions can be profoundly illustrated in cases of similar reasoning; the 
    
    # new variable has a second dimension which is in terms of "PartS" corresponding to Assembly's item descriptions that had been
    
    # the second dimension of Assembly as well. So which one is the second dimension anyway?
    
    
    # To assimilate change terms and form the representing list of Unsemble's second dimension for each item, it is useful to determine
    
    # a list through procedures that includes every potential "PartS" location entry of that item and shares 'x' index with the keys. 
    
    #And that is just perfect, because location entry of nested lists  does not require scavenging; it s that everytime the first time
    
    # input entry of the item exists everything can been defined from that. Nevertheless, on the same single instance list using newly    
    
    # appended items, intending to then appending search results of that input yields a structure analogous to the Subway list that  
    
    # has been used.
    
    
    # Lastly, the third dimension can be defined as the item descriptions, which antecedes the major location entry
    
    # "PartS" is now the second to last dimension, which previously was the second dimension. Furthermore, that is prompted by the
    
    #practical sense that it makes, as in a dictionary reversal scenario the values become keys. Hence, it is safe to say that 
    
    # as for each location a topical reversal takes place to form the navigating variable the third dimension practically; Assembly's 
    
    # assumed third dimension is "PartS". 
    
    
    




### P.M1. A Major reason that deems all attempts to reverse the Assembly variable with a method in context of the creation of a URDb dictionary 

#probably futile is the pre-determined occurences of semantically entailed list that comes with digital ignorance about them.

#### P.M2.! I know how many trivialty is to find on the dictionary reversal.
