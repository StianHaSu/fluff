import requests

def do_request(request: str, request_type: str, cookies: dict[str, str], data: dict[str, str]):
    match request_type:
        case "get":
            return requests.get(request, cookies=cookies)
        case "post":
            return requests.post(request, cookies=cookies)


def _do_post(request: str, cookies: dict[str, str], data: dict[str, str], data_type: str):
    match data_type:
        case "form":
            requests.post(request, cookies=cookies, data=data)
        case "json":
            requests.post(request, cookies=cookies, json=data)



