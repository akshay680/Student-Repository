import git
import requests

def repo(username):
    request = requests.get('https://api.github.com/users/' + username + '/repos')
    json = request.json()
    commits = []
    li = []
    for i in range(0, len(json)):
        j = requests.get('https://api.github.com/repos/' + username + '/' + json[i].get('name') + '/commits').json()
        commits.append(len(j))
    for i in range(0, len(json)):
        li.append((json[i]['name'], commits[i]))
    return li

print(repo('nidhi'))






