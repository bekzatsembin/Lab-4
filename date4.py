from datetime import datetime, time
def diff(m, n):
  timedelta = m - n
  return timedelta.days * 24 * 3600 + timedelta.seconds

a = datetime.strptime('2011-02-11 01:00:00', '%Y-%m-%d %H:%M:%S')

b = datetime.now()
print("\n%d seconds" %(diff(b, a)))
