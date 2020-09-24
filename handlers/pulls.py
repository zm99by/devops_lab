import requests

auth = 'your@gmail.com'
passwd = 'your_pass'


def get_request(params):
    return requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls", auth=(auth, passwd),
                        params=params).json()


def get_data(data):
    arr = []
    for x in range(len(data)):
        arr.append({"num": data[x]["number"], "title": data[x]["title"], "link": data[x]["html_url"]})
        x += 1
    return arr


def get_pulls(state):
    if state == 'open' or state == 'closed':
        return get_data(get_request({'per_page': 100, 'state': state}))
    else:
        data = get_request({'per_page': 100, 'state': "all"})
        if state == 'accepted' or state == 'needs work':
            arr = []
            for x in range(len(data)):
                if data[x]["labels"] and data[x]["labels"][0]["name"] == state:
                    arr.append({"num": data[x]["number"], "title": data[x]["html_url"], "link": data[x]["title"]})
                    x += 1
            return arr
        else:
            return get_data(data)
