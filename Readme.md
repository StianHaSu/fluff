# fluff

I made this tool to solve a challenge in the course IN5290 (Ethical Hacking).  
I had already solved the challenge, but somebody thought my solution wasn't cool enough.

fluff is basically like ffuf, with a few exceptions:  
- It is written Python  
- It is considerably slower  
- It is way less feature rich  

But what fluff lacks in speed and features, it makes ups for in doing the job (some times).
And it is also faster than the free tier of BurpSuite intruder, so theres that.

## Usage  
To run the tool, you have to provide arguments for:  
- --url (the url to fuzz)
- --list (the wordlist to use)

Optional arguments:  
- -m/--method (the http method to use (get/post)) *currently only get works
- -c/--cookie (optional cookies) on the format (-c [cookiename],[cookievalue])  
you can add multiple cookies like this: -c [cookiename],[cookievalue] -c [cookiename2],[cookievalue2]

### Examples
**Simple get fuzz:**  
python3 fluff.py --url example.com/FUZZ --list wordlist.txt -m get

**Get with cookie fuzz:**  
python3 fluff.py --url example.com --list wordlist.txt -m get -c myid,1FUZZ3