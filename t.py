import requests

url = "https://t.me/Yso35"
response = requests.get(url).content

# print(response)
# u = response[
#     response.index('src="https://cdn4.telegram-cdn.org/file') : response.index("></a>")
# ]
# print(u)

print(response.index("tgme_page_photo_image"))
