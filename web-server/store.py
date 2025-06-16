import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)

    print(type(r.text))
    categories = r.json()
    print(f'esto es un json: {categories}')
    for category in categories:
        print('probando que es category',category)
        print(category['name'])
        