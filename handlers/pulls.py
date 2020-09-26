import requests

auth = 'your@gmail.com'
passwd = 'yourpass'
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'


def get_request(params):
    return requests.get(url, auth=(auth, passwd), params=params).json()


def get_d(d):
    arr = []
    for x in range(len(d)):
        t = {"num": d[x]["number"], "title": d[x]["title"], "link": d[x]["html_url"]}
        arr.append(t)
    return arr


def get_pulls(state, data):
    if state == 'open' or state == 'closed':
        d = data
        arr1 = []
        for x in range(len(d)):
            if d[x]["state"] == state:
                t = {"num": d[x]["number"], "title": d[x]["title"], "link": d[x]["html_url"]}
                arr1.append(t)
        return arr1
    else:
        d = data
        if state == 'accepted' or state == 'needs work':
            arr2 = []
            for x in range(len(d)):
                t = {"num": d[x]["number"], "title": d[x]["title"], "link": d[x]["html_url"]}
                if d[x]["labels"] and d[x]["labels"][0]["name"] == state:
                    arr2.append(t)
            return arr2
        else:
            return get_d(d)
