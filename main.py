# -*- coding:utf-8 -*-
# author: xiang578
# email: i@xiang578
# blog: www.xiang578.com

import urllib.request
import json
from icalendar import Calendar
from icalendar import Event
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_json(url):
    page = urllib.request.urlopen(url)
    return page


def get_ics(contests):
    cal = Calendar()
    cal['version'] = '2.0'
    cal['prodid'] = '-//xiang578.com//ACM Contests Calendar//CN'
    cal['summary'] = 'ACM Contests Calendar'
    cal['CALSCALE'] = 'GREGORIAN'
    cal['X-WR-TIMEZONE'] = 'Asia/Shanghai'
    for contest in contests:
        dtstart = datetime.strptime(contest['start_time'], '%Y-%m-%d %H:%M:%S')
        dtend = dtstart + relativedelta(hours=2)
        event = Event()
        event.add('uid', contest['id'])
        event.add('dtstamp', datetime.now())
        event.add('summary', contest['name'])
        event.add('location', contest['oj'])
        event.add('DESCRIPTION', contest['link'])
        event.add('dtstart', dtstart)
        event.add('dtend', dtend)
        cal.add_component(event)
    ret = cal.to_ical()
    return ret.decode('utf8')


def save_ics(filename, outputstring):
    print(outputstring)
    filewrite = open(filename, 'w')
    filewrite.write(outputstring)
    filewrite.close()


if __name__ == '__main__':
    jsonurl = 'http://contests.acmicpc.info/contests.json'
    filename = 'contestscalendar.ics'
    calendar = get_json(jsonurl)
    contests = json.load(calendar)
    outputstring = get_ics(contests)
    save_ics(filename, outputstring)
