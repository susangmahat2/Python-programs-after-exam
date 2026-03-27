import random
import time
def getRandomdate(start,end):
    
    print("Start date:",start)
    print("End date:",end)

    randomGenerator=random.random()
    dateformat="%Y-%m-%d"
    starttime=time.mktime(time.strptime(start,dateformat))
    endtime=time.mktime(time.strptime(end,dateformat))
    randomtime=starttime + randomGenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
result=getRandomdate("2020-01-01","2020-12-31")
print("Random date:",result)

