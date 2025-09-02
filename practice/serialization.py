import json

# Sample Python object
data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}

# Serialize the object to a JSON string
json_string = json.dumps(data)


# Optionally, write the JSON string to a file
with open('data.json', 'w') as file:
    json.dump(data, file)