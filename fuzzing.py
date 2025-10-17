import http_requests

def fuzz_url(url: str, method: str, wordlist_filename: str, output_filename: str, optional_arguments: dict[str, str]) -> None:
    wordlist = open(wordlist_filename, 'r')
    output_file = open(output_filename, 'w+')

    output_file.write(f"url,status_code,content_length,fuzz\n")
    
    total = len(wordlist.readlines())
    wordlist.seek(0)
    cleared = 0
    for word in wordlist:
        cleared += 1
        
        word = word.replace("\n", "")
        current_url = url.replace("FUZZ", word)
        current_url = current_url.strip()

        result = http_requests.do_request(current_url, method, _get_cookies(optional_arguments, word), None)
        output_file.write(f"{current_url},{result.status_code},{len(result.content)},{word}\n")

        print(f"\rProgress: {cleared}/{total}", end="", flush=True)
        
    print(f"\rFinished: {cleared}/{total}\n", end="")
    output_file.close()
    wordlist.close()

def _get_cookies(optional_arguments: dict[str, any], word: str) -> dict[str, str]:
    all_cookies = optional_arguments["cookies"]
    if not all_cookies:
        return {}

    return {cookie.split(":")[0].strip() : cookie.strip().split(":")[1].replace("FUZZ", word) for cookie in all_cookies}