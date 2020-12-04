from datetime import datetime, timedelta
d_today = datetime.now()
d_yesterday = d_today - timedelta(days=1)
d_thertydays = d_today - timedelta(days=30)

print(d_today)
print(d_yesterday)
print(d_thertydays)