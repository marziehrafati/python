per_hour = int(input('how much do you get per hour ?   '))
hour = int(input('how many hours do you work ?  '))

def salary():
    if hour > 8 :
      return 'error!'
    else:          
        income = hour * per_hour
        return income

print(salary())