import json
import argparse

# Following piece of code is utilized to receive arguments to run the script with
parser=argparse.ArgumentParser()
parser.add_argument('--school', help='Enter the school name you want to pull data from eg. York University - Keele')
parser.add_argument('--department', help='Enter the department you want to see the professors of eg. Computer Science, Psychology')
argms=parser.parse_args()
# pass parameters as --bar=bar-val and access them using argms.bar

# If school name passed, use it. Otherwise, use YorkUni2 as default
if (argms.school != None): 
    school = argms.school
else:
    school = "YorkUni2"
# If department passed, use it. Otherwise, use Computer Science as default
if (argms.department != None): 
    department = argms.department
else:
    department = "Computer Science"

# Load the list of all profs
with open('./../json/%s.json' %school) as f:
  data = json.load(f)
  
# Create an empty dict to fill with filtered data
Profs = {}

# Iterate through input json file
for key in data:
  if (data[key]['Department'] == department):
      Profs[key] = data[key]

      # Keep these for testing purposes
      #print(data[key])
      #print(json.dumps(data[key], indent=4))

depOutput = ("./../json/%s-%s.json" %(school, department))
# Dump the dictionary to a json file
with open(depOutput, 'w') as Out:
    json.dump(Profs, Out, indent=4)


# outputfile = open("CompSci.json", "w")
# # magic happens here to make it pretty-printed
# outputfile.write(simplejson.dumps(simplejson.loads(csProfs), indent=4, sort_keys=True))
# outputfile.close()