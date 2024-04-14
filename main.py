# the new ?__a=1 endpoint
import requests

def check_if_blocked(name: str, cookie: str) -> bool:
    resp = requests.get(
        url="https://i.instagram.com/api/v1/users/web_profile_info/?username=" + name,
        headers={
            "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1',
            "x-ig-app-id": "936619743392459",
            "cookie": cookie
        }
    )

    return resp.json().get("data", {"user": None}).get("user") == None

# username = person to see if they  blocked us
# web_cookie = your cookie when opening instagram on your web browser, just copy it all
username = ''
web_cookie = ''

blocked = check_if_blocked(username, web_cookie)
print(f'{username} has {"not" if not blocked else ""} blocked us! >:(')
