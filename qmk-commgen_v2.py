lines=input("How many lines? ")
lines=int(lines)
for num in range(1,(lines+1)):
    kmap=input("Line "+str(num)+"? ")
#while kmap:
kmap=" *,"+kmap
kmap=kmap.replace(" ","")
colm=""
kmap=kmap.replace("KC_NO,","       ,")
kmap=kmap.replace("XXXXXXX,"," Null ,")
kmap=kmap.replace("_______,","      ,")
kmap=kmap.replace("KC_TRNS,","      ,")
kmap=kmap.replace("KC_A,","   A  ,")
kmap=kmap.replace("KC_B,","   B  ,")
kmap=kmap.replace("KC_C,","   C  ,")
kmap=kmap.replace("KC_D,","   D  ,")
kmap=kmap.replace("KC_E,","   E  ,")
kmap=kmap.replace("KC_F,","   F  ,")
kmap=kmap.replace("KC_G,","   G  ,")
kmap=kmap.replace("KC_H,","   H  ,")
kmap=kmap.replace("KC_I,","   I  ,")
kmap=kmap.replace("KC_J,","   J  ,")
kmap=kmap.replace("KC_K,","   K  ,")
kmap=kmap.replace("KC_L,","   L  ,")
kmap=kmap.replace("KC_M,","   M  ,")
kmap=kmap.replace("KC_N,","   N  ,")
kmap=kmap.replace("KC_O,","   O  ,")
kmap=kmap.replace("KC_P,","   P  ,")
kmap=kmap.replace("KC_Q,","   Q  ,")
kmap=kmap.replace("KC_R,","   R  ,")
kmap=kmap.replace("KC_S,","   S  ,")
kmap=kmap.replace("KC_T,","   T  ,")
kmap=kmap.replace("KC_U,","   U  ,")
kmap=kmap.replace("KC_V,","   V  ,")
kmap=kmap.replace("KC_W,","   W  ,")
kmap=kmap.replace("KC_X,","   X  ,")
kmap=kmap.replace("KC_Y,","   Y  ,")
kmap=kmap.replace("KC_Z,","   Z  ,")
kmap=kmap.replace("KC_1,","   1  ,")
kmap=kmap.replace("KC_2,","   2  ,")
kmap=kmap.replace("KC_3,","   3  ,")
kmap=kmap.replace("KC_4,","   4  ,")
kmap=kmap.replace("KC_5,","   5  ,")
kmap=kmap.replace("KC_6,","   6  ,")
kmap=kmap.replace("KC_7,","   7  ,")
kmap=kmap.replace("KC_8,","   8  ,")
kmap=kmap.replace("KC_9,","   9  ,")
kmap=kmap.replace("KC_0,","   0  ,")
kmap=kmap.replace("KC_ENTER,","Enter ,")
kmap=kmap.replace("KC_ENT,","Enter ,")
kmap=kmap.replace("KC_ESC,"," Esc  ,")
kmap=kmap.replace("KC_ESCAPE,"," Esc  ,")
kmap=kmap.replace("KC_BSPACE,"," Bksp ,")
kmap=kmap.replace("KC_BSPC,"," Bksp ,")
kmap=kmap.replace("KC_TAB,"," Tab  ,")
kmap=kmap.replace("KC_SPACE,","Space ,")
kmap=kmap.replace("KC_SPC,","Space ,")
kmap=kmap.replace("KC_MINUS,","  -   ,")
kmap=kmap.replace("KC_MINS,","  -   ,")
kmap=kmap.replace("KC_LBRACKET,","  [   ,")
kmap=kmap.replace("KC_LBRC,","  [   ,")
kmap=kmap.replace("KC_RBRACKET,","  ]   ,")
kmap=kmap.replace("KC_RBRC,","  ]   ,")
kmap=kmap.replace("KC_BSLASH,","  \   ,")
kmap=kmap.replace("KC_BSLS,","  \   ,")
kmap=kmap.replace("KC_NONUS_HASH,","   #  ,")
kmap=kmap.replace("KC_NUHS,","      ,")
kmap=kmap.replace("KC_SCOLON,","      ,")
kmap=kmap.replace("KC_SCLN,","      ,")
kmap=kmap.replace("KC_QUOTE,","      ,")
kmap=kmap.replace("KC_QUOT,","      ,")
kmap=kmap.replace("KC_GRAVE,","      ,")
kmap=kmap.replace("KC_GRV,","      ,")
kmap=kmap.replace("KC_COMMA,","      ,")
kmap=kmap.replace("KC_COMM,","      ,")
kmap=kmap.replace("KC_xxxx,","      ,")
kmap=kmap.replace("KC_xxxx,","      ,")
kmap=kmap.replace("KC_xxxx,","      ,")






kmap=kmap.replace(",","|")
print(kmap)
out=open("comment.txt","w+")