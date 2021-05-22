import json

# Load the list of all profs
with open('YorkUni2.json') as f:
  data = json.load(f)
  
# Create an empty dict to fill with filtered data
Profs = {}

# Iterate through input json file
for key in data:
  if (data[key]['Department'] == 'Psychology'):
      Profs[key] = data[key]

      # Keep these for testing purposes
      #print(data[key])
      #print(json.dumps(data[key], indent=4))

# Dump the dictionary to a json file
with open('Psychology.json', 'w') as Out:
    json.dump(Profs, Out)



# outputfile = open("CompSci.json", "w")
# # magic happens here to make it pretty-printed
# outputfile.write(simplejson.dumps(simplejson.loads(csProfs), indent=4, sort_keys=True))
# outputfile.close()