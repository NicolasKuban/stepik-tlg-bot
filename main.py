
import requests
import time


from config import API_CATS_URL, API_URL, ERROR_TEXT, TOKEN


chat_id: int
TIMEOUT = 60


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


def send_request(link: str) -> None:
    offset = -2
    updates: dict
    while True:
        start_time = time.time()
        updates = requests.get(
            f'{API_URL}{TOKEN}'
            f'/getUpdates?offset={offset + 1}&timeout={TIMEOUT}'
        ).json()
        if updates['result']:
            for result in updates['result']:
                print(result['message']['text'])
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                do_something()
                requests.get(f'{link}&chat_id={chat_id}')
        time.sleep(3)
        end_time = time.time()
        print(f'Время выполнения: {end_time - start_time:.4f}')


def get_link_text(text: str) -> str:
    return f'{API_URL}{TOKEN}/sendMessage?text={text}'


def get_link_photo() -> str:
    try:
        return f'{API_URL}{TOKEN}/sendPhoto?photo={get_cat_photo()}'
    except CantGetPhoto:
        return f'{API_URL}{TOKEN}/sendMessage?text={ERROR_TEXT}'


def do_something() -> None:
    print('====> Получен update')


if __name__ == '__main__':
    # say_hello('Hello!')
    # sendPhoto()
    send_request(get_link_text('Привет!'))
    # send_request(get_link_photo())
