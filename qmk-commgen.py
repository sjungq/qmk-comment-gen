import qmk_kc
import qmk_kc2
import re
from tkinter import Tk
import collections
import json
#import pusheen

#print(pusheen.widthlist)
#widthlist = pusheen.widthlist
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
layoutname = ''
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
    
    if not layoutname:
        match = re.search('(LAYOUT_*?\w*\({1}?)', line)
        if match:
            layoutname = match.group(1)[:-1] #group 3 will contain LAYOUT_blahblah( string
        #try looking for just LAYOUT(?


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

Layout = collections.namedtuple('Layout', ['name', 'layout_data'])
unit = 7 #spaces for 1u cap
def generate_filler(text, width):
    """
    Takes in keycode string (ie. "A", "BSPACE") and returns the same string padded with spaces as necessary
    1 : 6,
        1.25 : 7,
        1.5 : 9,
        1.75 : 11,
        2 : 12,
        2.25 : 13,
        2.75 : 17,
        3 : 18,
        6.25 : 38
    """
    #Minimum size 6 units = 1u
    #gonna be ugly hardcoded lines here
    spaces = {
        1 : unit,
        1.25 : int(round(unit*1.25)),
        1.5 : int(round(unit*1.5)),
        1.75 : int(round(unit*1.75)),
        2 : int(round(unit*2)) + 1,
        2.25 : int(round(unit*2.25)),
        2.75 : int(round(unit*2.75)) + 1,
        3 : int(round(unit*3)) + 2,
        6.25 : int(round(unit*6.25)) + 5
    }
    padded_text = text
    keysize = spaces[width]
    fillercount = keysize - len(text) #number of blank spaces we need.
    if len(text) > 6:
      padded_text = text[0:6]
    else:
      if fillercount != 0:
          if fillercount % 2 == 0:
              #if there's an even number of spaces, equally distribute spaces.
              spaces = ' ' * int(fillercount / 2)
              padded_text = '{padding}{text}{padding}'.format(padding=spaces, text=text)
          else:
              #odd number of spaces; equally distribute, but put one extra after
              if fillercount == 1:
                  #if only one space, glue onto the right
                  padded_text = ' {text}'.format(text=text)
              else:
                  spaces = ' ' * int(fillercount / 2)
                  padded_text = '{padding}{text}{padding} '.format(padding=spaces, text=text)

    return padded_text

def generate_ascii(layout, jsonfile='info.json'):
    info_data = json.load(open(jsonfile))
    layouts = info_data['layouts']
    print(layoutname)
    #input()
    layoutinfo = layouts[layoutname]['layout']
    ascii = ''
    #print(layoutinfo['layout'])
    #input()
    #print(layout.layout_data)
    width = 0
    #first generate the total length; for now we're just going to use the first layout
    for index in range(0, len(layoutinfo)):
        if layoutinfo[index]['y'] == 0:
            if 'w' in layoutinfo[index].keys():
                width += layoutinfo[index]['w']
            else:
                width += 1
    #print(layoutinfo)
    #input()
    #print(width)
    #print(layoutinfo['w'])
    #input()

    edge = '.' + ('-' * int(unit * width) )
    edge += ('-' * int(width-1)) + '.\n'
    edge2 = edge.replace('.','|')
    ascii += edge
    #print(ascii)
    width_index = 0 #I REALLY DON'T LIKE THIS BUT I DON'T WANNA REWRITE?
    for line in layout.layout_data:
        ascii += '|' #start of keymap row
        for text in line:
            width = 1
            if 'w' in layoutinfo[width_index].keys():
              width = layoutinfo[width_index]['w']

            ascii += (generate_filler(text, width) + '|')
            width_index += 1
            #print(line)
            #input()
        ascii += '\n'

        #at end of keymap row, add another edge.
        ascii += edge2
    print(ascii)
    return ascii

with open('comment.txt', 'w', encoding='utf-8') as comment_file:
    for custom in notdef:
        qmk_kc2.keycodes[custom.split(' ')[1]] = custom.split(' ')[2]
    for layer_index in range(0, len(KClayers)):
        print(layer_index)
        print(names)
        """
        Each layer looks as thus:
        ['KC_GRV,KC_Q,KC_W,KC_E,KC_R,KC_T,KC_Y,KC_U,KC_I,KC_O,KC_P,KC_BSPC,', 'KC_LCTL,KC_A,KC_S,KC_D,KC_F,KC_G,KC_H,KC_J,KC_K,KC_L,KC_SCLN,KC_QUOT,', 'KC_LSFT,KC_Z,KC_X,KC_C,KC_V,KC_B,KC_N,KC_M,KC_COMM,KC_DOT,KC_SLSH,KC_ENT,', 'KC_ESC,KC_TAB,KC_LALT,KC_LGUI,LOWER,KC_SPC,RAISE,KC_LEFT,KC_RGHT,KC_UP,KC_DOWN']
        layer[x] = single comma delimited string of all keycodes for a single row 'x'
        using width information from info.json, 
        create a 
        """
        layer = KClayers[layer_index]
        #comment_file.write(names[layer_index] + '\n')
        layout = Layout('', [])
        for row_index in range(0, len(layer)):
            if layer[row_index].endswith(','):
                layer[row_index] = layer[row_index][:-1]
            layersplit = layer[row_index].split(',')
            textlist = [qmk_kc2.keycodes[code] for code in layersplit]

            #do shit with textlist here
            #comment_file.write(str(textlist) + '\n')
            #print(textlist)
            layout.layout_data.append(textlist)

        comment_file.write(generate_ascii(layout))
        #print(layout['layoutdata'])


            

""" original spaceman code here       
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
"""