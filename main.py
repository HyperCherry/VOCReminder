import json
import nonebot
from hoshino import Service
import urllib.request

sv = Service('VOCReminder')


@nonebot.scheduler.scheduled_job('cron', hour='23', minute='00')
async def voc_reminder():
    bot = nonebot.get_bot()
    record = get_record('https://learnywhere.cn/bb/dashboard/profile/search?userId=95439945')
    learn_num = 0
    review_num = 0
    duration = 0
    detail_list = record['data_body']['learnList']
    for i in detail_list:
        if i['date'] == '今日':
            learn_num = i['learnNum']
            review_num = i['reviewNum']
    msg = f'[CQ:at,qq=594602549]'
    msg += f'\n今日学习:' + str(learn_num) + "\n" '今日复习:' + str(review_num)
    detail_list = record['data_body']['durationList']
    for i in detail_list:
        if i['date'] == '今日':
            duration = i['duration']
    msg += f'\n今日时长:' + str(duration)
    await bot.send_group_msg(group_id=512377098, message=msg)


def get_record(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json
