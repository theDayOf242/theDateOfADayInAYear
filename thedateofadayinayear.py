import datetime

def dateofdayinyear(Year=2021, Day=42):
    ydt = datetime.datetime(year=Year, month=1, day=1)
    ydt2 = datetime.datetime(year=Year, month=1, day=2)
    timeofaday = ydt2 - ydt
    return ydt + (Day - 1)*timeofaday

def dateofdayinyears(Year=2021, Number=4, Day=42):
    l = []
    for y in range(Year, Year+Number):
        l.append(str(dateofdayinyear(y, Day)))
    return l


