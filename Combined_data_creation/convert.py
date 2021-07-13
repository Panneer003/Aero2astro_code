import json

# main json file for store all json data
main_json = {}
main_json['categories'] = [{"id": 1, "name": "aeroplane", "supercategory": "vehicle"}, 
                            {"id": 2, "name": "car", "supercategory": "vehicle"}, 
                            {"id": 3, "name": "chair", "supercategory": "furniture"}, 
                            {"id": 4, "name": "cow", "supercategory": "animal"}, 
                            {"id": 5, "name": "person", "supercategory": "person"},
                            {"id": 6, "name": "traffic_light", "supercategory": "outdoor"}]

main_json['images'] = []   
main_json['annotations'] = []

# List of json paths
json_files = ['aeroplane.json','car.json','chair.json','cow.json','person.json','traffic_light.json']

# Load every json file and store coresponding data in main json
for i,file in enumerate(json_files):

    with open(file,'r') as f:
        val = json.load(f)

    for data in val['images']:
        main_json['images'].append(data)
        
    
    for data in val['annotations']:
        main_json['annotations'].append(data)
        
    print('{} successful..'.format(file))
    
with open('main.json','w') as f:
    json.dump(main_json,f)
