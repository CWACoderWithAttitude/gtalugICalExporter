#!/usr/bin/env python

import vobject
import datetime
from pytz import timezone
from dateutil import rrule

TIME_ZONE = timezone('US/Eastern')
TODAY = datetime.date.today() - datetime.timedelta(days=31)
MEETING_START_TIME = datetime.time(19, 30, tzinfo=TIME_ZONE)
MEETING_END_TIME = datetime.time(21, 30, tzinfo=TIME_ZONE)

MEETINGS = list(rrule.rrule(rrule.MONTHLY, count=5, byweekday=(rrule.TU), bysetpos=2))

cal = vobject.iCalendar()

for m in MEETINGS:
        url = "http://gtalug.org/wiki/Meetings:%s-%s" % (m.year, m.strftime("%m"))

        event = cal.add('vevent')
        event.add('summary').value = "GTALUG Meeting"
        event.add('description').value = "Check the website for any updated information: " + url
        event.add('url').value = url

        event.add('dtstart').value = datetime.datetime.combine(m.date(), MEETING_START_TIME)
        event.add('dtend').value = datetime.datetime.combine(m.date(), MEETING_END_TIME)

print (cal.serialize())
