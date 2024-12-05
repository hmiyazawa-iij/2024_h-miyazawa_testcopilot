# 変数設定
import requests
import logging
from typing import Optional, Dict, Any
import os

# ログフォルダとファイルの設定
log_folder = 'logs'
log_file = 'app.log'
os.makedirs(log_folder, exist_ok=True)
log_path = os.path.join(log_folder, log_file)

# ログの設定
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(log_path, 'a', 'utf-8')])

def fetch_data(url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Optional[str]:
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)  # タイムアウトを10秒に設定
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
url = 'https://www.iij.ad.jp/'
params = {'key1': 'value1', 'key2': 'value2'}  # 例としてリクエストパラメータを設定
headers = {'User-Agent': 'my-app/0.0.1'}  # 例としてヘッダーを設定

data = fetch_data(url, params=params, headers=headers)
if data:
    print(data)
