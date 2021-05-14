import datetime

d =datetime.datetime.strptime("20000801", "%Y%m%d").strftime("%d/%m/%Y")

print(d)


#str(datetime.datetime.strptime(row[3], "%Y%m%d").strftime("%d/%m/%Y"))