import json
import datetime

dt = datetime.datetime.strptime('20161001', "%Y%m%d").date()
print "test %s" % dt
print type(str(dt))
dt = dt + datetime.timedelta(days=1)
print type(dt)