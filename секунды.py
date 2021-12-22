sec = int(input('Секунд: '))

days = sec // 86400
print('дней: ', days)

ost1 = sec - days * 86400

hours = ost1 // 3600
print('часов: ', hours)

ost2 = ost1 - hours * 3600

minute = ost2 // 60
print('минут: ', minute)

seconds = ost2 - minute * 60
print('секунд: ', seconds)
