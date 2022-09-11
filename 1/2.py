import requests

API_TOKEN = ''

get_parameters = {'chat_id': '', 'text': 'Привет из функции =)'}

response = requests.get(f'https://api.telegram.org/bot{API_TOKEN}/sendMessage',
                        params=get_parameters)



