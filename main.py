import requests
import time


from config import API_URL, TOKEN


chat_id: int


def say_hello(text: str) -> None:
    offset = -2
    counter = 0
    while counter < 100:
        print('attempt=', counter)
        print(f'offset={offset}')
        updates = requests.get(
            f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}'
        ).json()
        if updates['result']:
            for result in updates['result']:
                print(result['message']['text'])
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                requests.get(
                    f'{API_URL}{TOKEN}'
                    f'/sendMessage?chat_id={chat_id}&text={text}'
                )

        time.sleep(1)
        counter += 1


if __name__ == '__main__':
    say_hello('Hello!')
