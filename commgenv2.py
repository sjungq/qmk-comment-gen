import collections
import json

index = 0

"""
with open('keymap.c') as keymap:
  stuff = keymap.readlines()
  for item in stuff:
    print('{index} {item}'.format(index = index, item = item))
    index += 1
"""

"""
Convert a keymap.c AND  into a list containing the index, text representation, X, Y, W

A single function accepts that list and writes to text file
"""

KeymapInfo = collections.namedtuple('KeymapInfo', ['layouts', 'custom_keycodes'])
Layout = collections.namedtuple('Layout', ['name', 'layout_dict'])
Key = collections.namedtuple('Key', ['index', 'keycode', 'text', 'x', 'y', 'w'])

def process_keymaps(keymap_file='keymap.c', info_file='info.json'):
  """
  Generates list containing all layouts defined in keymap.c as a list in the following format:
  { 
    layouts : [
      ( 
        name : layout1,
        layout_dict : 
        [
          ( index : 0, keycode : "KC_TAB", x : 0, y: 0, w : 1 ),
          ( index : 1, keycode : "KC_Q", x : 1, y : 0, w : 1 ),
          ...
        ]
      ),

      (
        name : layout2,
        layout_dict : 
        [
          ( index : 0, keycode : "KC_TILD", x : 0, y: 0, w : 1 ),
          ( index : 1, keycode : "KC_EXLM", x : 1, y : 0, w : 1 ),
          ...
        ]
      )
    ],

  }
  """

  #showerthought: you might as well use info.json to print the text.
  #keycodes limited to 6 characters (inside the box); custom codes that bypass this will be cut off.

  with open(info_file, 'r') as info:
    data = json.load(info_file)
    layouts = data['layouts'] 
    # {"LAYOUT_planck_mit":{{"layout":[{w, x, y}]}}, "LAYOUT_planck_grid":{"layout":[{w, x, y}]}}
    #ooglay
    with open(keymap_file, 'r') as keymap:
      keylines = keymap.readlines()
      for line in keylines:
        #look for LAYOUT( or LAYOUT_*(
        #\[(.*?)\] -> captures stuff in brackets
        #\[(.*?)\](\s?=\s?)(LAYOUT) -> captures anything in ["name of layer"] = LAYOUT format
        #
        pass
    pass
  return layouts