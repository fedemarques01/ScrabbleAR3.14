import datetime

timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
while True:
    print(datetime.datetime.utcnow())
    if datetime.datetime.utcnow() > timer_stop:
        print("timer complete")
        break

