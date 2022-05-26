import json

import urllib.request


def get_record(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json


if __name__ == '__main__':
    record = get_record('https://learnywhere.cn/bb/dashboard/profile/search?userId=95439945')
    learnNum = 0
    reviewNum = 0
    duration = 0
    detailList = record['data_body']['learnList']
    for i in detailList:
        if i['date'] == '今日':
            learnNum = i['learnNum']
            reviewNum = i['reviewNum']
    print('今日学习:'+str(learnNum))
    print('今日复习:'+str(reviewNum))
    detailList = record['data_body']['durationList']
    for i in detailList:
        if i['date']=='今日':
            duration=i['duration']
    print('今日时长:'+str(duration))