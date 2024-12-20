import getpass
import requests

def main():
    print("SV にログインするため Idaten 認証をします")
    user = input("ユーザ名: ")
    password = getpass.getpass("パスワード: ")

    print("jp にログインするため LDAP 認証をします")
    luser = input("ユーザ名: ")
    lpass = getpass.getpass("パスワード: ")

    # Idaten SSO 認証
    user = user.replace('@iij.ad.jp', '')
    luser = luser.replace('@iij.ad.jp', '')

    login_data = {
        'loginId': f'{user}@iij.ad.jp',
        'password': password,
        'dom': '',
        'burl': 'https://login.iij-bo.jp',
        'amtd': 'PASSWD'
    }

    login_url = 'https://login.iij-bo.jp/sso/login.do'
    target_url = 'https://cxe-sv.iij-bo.jp/api/get_vm_list'

    try:
        with requests.Session() as session:
            login_response = session.post(login_url, data=login_data)
            login_response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる

            response = session.get(target_url)
            response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる

            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"リクエスト中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()