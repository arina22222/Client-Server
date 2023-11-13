import requests


server_url = 'http://localhost:8080'

operations = ['/add', '/substract', '/multiply', '/divide']

for operation in operations:
    first = input()
    second = input()

    headers= {
        'first' : first,
        'second' : second
    }
   
    response = requests.patch(server_url + operation, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print(f'ok:{response.status_code}  ' + f'Success: {result}')
    else:
        print(f'Bad request :{response.status_code}  '+ 'Fail:', response.text)