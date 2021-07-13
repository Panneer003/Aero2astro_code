import json 

with open('aeroplane.json','r') as f:  # old json file
    val = json.load(f)

ann = val['annotations']
val.pop('annotations')
val['annotations'] = []

for an in ann:
    an['category_id'] = 1           # update category id
    val['annotations'].append(an)

with open('aeroplane.json','w') as file:   # New json file
    json.dump(val,file)