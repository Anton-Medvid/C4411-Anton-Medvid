import requests

response = requests.post('https://httpbin.org/post',
                        data='Test data',
                        headers={'h1': 'test title'})
print(response.text)