import qmk_kc

with open('meow.txt','w', encoding='utf-8') as f:
  for key, value in qmk_kc.keycodes.items():
    if len(key.split(',')[0]) > 0:
      f.write('"' + key.split(',')[0].strip() + '"  : "' + value.split(',')[0].strip() + '",\n')
    else:
      f.write('"' + key.strip() + '" : "' + value.strip() + '"\n')
