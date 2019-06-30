import qmk_kc
import re
from tkinter import Tk
import pusheen

#print(pusheen.widthlist)
widthlist = pusheen.widthlist
#input()
r=Tk()
r.withdraw()
comb=[]             #combined layer ready for output
fill='──────┬'      #top fill lines 
fill2='──────┼'     #middle row fill lines
fill3='──────┴'     #bottom fill lines
laystart=False      #has the program found a layer start
layers=0            #how many layers
KClayers=[]         #array of all KClines
KClines=[]          #list if all KC on line
nl='\n'
width=[]
names=[]
layname=""
notdef=[]
ends=['','}']
#open keymap file
inpt=open('keymap.c','r')
inpList=inpt.readlines()
#add all lines of keymap to allin var and close
inpt.close()
file=open('comment.txt','w+',encoding='utf-8')
for line in inpList:
    line=line.replace('\n','')
    line=line.replace('\\','')
    for possible in ends:
        if line==possible:
            end=True
        else:
            end=False
    if line.count('#define '):
        notdef.append(line)
    #remove whitespace and new lines
    line=line.replace(' ','')
    if line.count(')')==1 and line.count('(')==0 and laystart==True or end==True and laystart==True:
        #if it is the end of a layer
        laystart=False
        #add layer to KClayers
        KClayers.append(KClines)
        KClines=[]
        layers+=1
    elif laystart==True:
        #if it part of keymap add it to KC lines
        KClines.append(line)
    if re.search('LAYOUT',line):
        laystart=True
        fnd = re.search('\[(.+?)\]',line)
        if fnd:
            layname=fnd.group(1).replace("_","")
            names.append(layname)
assert len(KClayers)>0,'+- No keymap Found -+'
assert layers==len(KClayers),'+- Layer Error -+'
print('Successfully imported layers')
lyrcount=layers
for layer in range(0,len(KClayers)):
    lyrcount-=1
    k = 0
    for num in range(0,len(KClayers[layer])):
        #define current layer
        crtln=(KClayers[layer][num])
        if crtln.endswith(',')==False:
            crtln=crtln+','
        colm=crtln.count(',')
        colm2=colm-1
        width.append(colm2)
        crtln=' * ,'+crtln

        #run it through my module see qmk_kc.py
        fixed=qmk_kc.replkc(crtln,notdef)

        print(fixed)
        input('meow')
        k+=1
        comb.append(fixed)
        lines=len(comb)
    file.write(nl)
    #Output to comment.txt
    print(f'/* {names[layer]}',file=file)
    print(f' * ┌{fill*width[0]}──────┐', file=file)
    for num in range(0,lines):
        print(comb[num])
        input()
        file.write(comb[num]+nl)
        if lines>1 and num<(lines-1):
            print(f' * ├{fill2*width[num]}──────┤', file=file)
    print(f' * └{fill3*width[len(width)-1]}──────┘',file=file)
    print(' */',file=file)
    print('Layer '+str(layer+1)+' done')
    #empty the combined list
    comb=[]
file.close()
#ask if clipboard
if qmk_kc.yesno('Enable paste to Clipboard')==True:
    opclp=open('comment.txt','r')
    clip=opclp.read()    
    r.clipboard_clear()
    r.clipboard_append(clip)
    r.update()
    r.destroy()
    print('Added to Clipboard')
print('Done printing Keymap')
