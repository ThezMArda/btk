import requests
url="https://jsonplaceholder.typicode.com/posts"
payload = {
    "title ":"btk",
    "body":"python",
    "userId":1
    
}
response = requests.post(url,json=payload)
print("durum",response.status_code)
print("api yaniti  ",response.json())