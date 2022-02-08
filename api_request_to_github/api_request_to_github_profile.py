import requests

response = requests.get("https://api.github.com/users/nafio-nabi")
my_profile = response.json()

print(f"username: {my_profile['login']}\nid: {my_profile['id']}\npublic repos: {my_profile['public_repos']}")