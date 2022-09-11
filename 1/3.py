import requests

API_TOKEN = ''


def send_message(chat_id: str, text: str) -> int:
    get_parameters = {'chat_id': chat_id, 'text': text}

    response = requests.get(f'https://api.telegram.org/bot{API_TOKEN}/sendMessage',
                            params=get_parameters)

    return response.status_code


if __name__ == '__main__':
    send_message('70365850', 'Привет из функции =)')
