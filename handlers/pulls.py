import requests

auth = 'your@gmail.com'
passwd = 'your_pass'
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'


def get_request(params):
    return requests.get(url, auth=(auth, passwd), params=params).json()


def get_d(d):
    arr = []
    for x in range(len(d)):
        t = {"num": d[x]["number"], "title": d[x]["title"], "link": d[x]["html_url"]}
        arr.append(t)
        x += 1
    return arr


def get_pulls(state):
    if state == 'open' or state == 'closed':
        return get_d(get_request({'per_page': 100, 'state': state}))
    else:
        d = get_request({'per_page': 100, 'state': "all"})
        if state == 'accepted' or state == 'needs work':
            arr = []
            for x in range(len(d)):
                t = {"num": d[x]["number"], "title": d[x]["title"], "link": d[x]["html_url"]}
                if d[x]["labels"] and d[x]["labels"][0]["name"] == state:
                    arr.append(t)
                    x += 1
            return arr
        else:
            return get_d(d)

