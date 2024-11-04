
import requests
import time


from config import API_CATS_URL, API_URL, ERROR_TEXT, TOKEN


chat_id: int


class CantGetPhoto(Exception):
    pass


def get_cat_photo() -> str:
    """Функция для получения ссылки на фото котика

    Args:

    Returns:
        str: возращается строка ссылки на фото котика
    """
    cat_response: requests.Response
    cat_photo_link: str
    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code != 200:
        raise CantGetPhoto
    cat_photo_link = cat_response.json()[0]['url']
    return cat_photo_link


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


def sendPhoto() -> None:
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
                try:
                    requests.get(
                        f'{API_URL}{TOKEN}'
                        f'/sendPhoto?chat_id={chat_id}&photo={get_cat_photo()}'
                    )
                except CantGetPhoto:
                    requests.get(
                        f'{API_URL}{TOKEN}'
                        f'/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}'
                    )
        time.sleep(1)
        counter += 1


if __name__ == '__main__':
    # say_hello('Hello!')
    sendPhoto()
