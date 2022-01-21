import requests
import sys
import json

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

token = f'token {sys.argv[2]}'
r = get(sys.argv[1], {'Authorization': token}).json()

issue_user = r['user']['login']

repo_url = r['repository_url']
repos = get(repo_url, {'Authorization': token}).json()

repo_contributor = r['contributors_url']
repo_cons = get(repo_contributor, {'Authorization': token}).json()

contributors = repo_cons['login']

if issue_user == contributors:
    output = f"{issue_user}は初めての貢献者ではありません。"
    print(f"RESULT_OUTPUT={output}")
else:
    output = f"{issue_user}は初めての貢献者です。"
    print(f"RESULT_OUTPUT={output}")
