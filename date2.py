from datetime import date, timedelta

y = date.today() - timedelta(1)
tod = date.today() 
tom = date.today() + timedelta(1)


print("Yesterday:", y)
print("Today:", tod)
print("Tomorrow:", tom)
