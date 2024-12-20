import requests
import logging
from typing import Optional

# ログの設定
logging.basicConfig(level=logging.INFO)

def fetch_data(url: str) -> Optional[str]:
    try:
        response = requests.get(url, timeout=10)  # タイムアウトを10秒に設定
        response.raise_for_status()  # HTTPエラーが発生した場合は例外を発生させる
        logging.info('Data fetched successfully')
        return response.text
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        logging.error(f'Request error occurred: {req_err}')
    except Exception as err:
        logging.error(f'Other error occurred: {err}')
    return None

# データを取得するURL
url = 'https://cxe-sv.iij-bo.jp/api/get_vm_list'
data = fetch_data(url)
if data:
    print(data)