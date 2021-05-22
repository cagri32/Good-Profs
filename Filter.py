import json

with open('YorkUni2.json') as f:
  data = json.load(f)

# iterate json to find the list of absent applicant
for key in data:
  if (data[key]['Department'] == 'Computer Science'):
      #print(data[key])
      print(json.dumps(data[key], indent=4))