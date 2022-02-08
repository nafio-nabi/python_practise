import requests

response = requests.get("https://api.github.com/users/nafio-nabi/repos")
my_projects = response.json()

for project in my_projects:
    repo_name = project["name"]
    repo_url = project["html_url"]
    print(f"Repo: {repo_name}\nRepo URL: {repo_url}\n")