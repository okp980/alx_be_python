import json

def process_json(data: dict, filename: str) -> dict:
    with open(filename, 'w') as file:
        json.dump(data, file)
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def main():
    data = {'first_name': 'Emmanuel', 'last_name': 'Okpunor', 'gender': 'male', 'age': 25, 'city': 'Madrid'}
    filename = 'data.json'
    processed_data = process_json(data, filename)
    print(processed_data)

if __name__ == "__main__":
    main()