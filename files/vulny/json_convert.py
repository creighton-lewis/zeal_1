import json
import os 
import subprocess

msf_module = os.path.abspath('sicat_2/files/msf_module.json')
print(msf_module)

# Load your original data
with open(msf_module, 'r') as f:
    data = json.load(f)

# Transform the data
result = []
for key, value in data.items():
    result.append({
        "title": value["name"].lower(),
        "module": value["fullname"],
        "link": f"https://www.rapid7.com/db/modules/{value['fullname']}",
        "references": value.get("references", [])
    })

# Output as formatted JSON
print(json.dumps(result, indent=4))

# Write to file
with open('output.json', 'w') as f:
    f.write(json.dumps(result, indent=4))
