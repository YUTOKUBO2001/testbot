import request

URL = 'https://api.github.com/repos/YUTOKUBO2001/testbot/contributors'
headers = {'Authorization': 'token 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'} # 取得したアクセストークン
r = requests.get(URL.format(repo), headers=headers)
return r.json()