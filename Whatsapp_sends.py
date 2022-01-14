import pywhatkit
import time

# print('now is', time.strftime("%Y%m%d%h%M%S"))

print('''
*Для надежной рассылки сообщений рекомендуется:
      - Стабильное и надежное интернет соединение мобильного терминала,
        с номера которого будут рассылаться сообщения.
      - Запущен браузер (по умолчанию) и сюда https://web.whatsapp.com/ подключен(привязан) мобильный терминал.'''
      )

print('''
*Примечание:'
      - Перенос времени отправки связано со свойствами использованых в коде модулей.
      - Каждое новое сообщение будет открывать новую вкладку в браузере.
      - При запуске программы, будет создан файл PyWhatKit_DB.txt с информацией о отправленных сообщениях.
      - Программа ненадежна, написана в учебных целях.'''
      )

phone_numbers = ['number', 'number', ...]

text_message = 'text'

now_hour = int(time.strftime('%H'))
now_min = int(time.strftime('%M'))
start_time_hour = now_hour

n = 0
x = now_min + 3

for i in range(len(phone_numbers)):
    if x > 55 and start_time_hour < 23:
        x = 0
        start_time_hour += 1
        print(f'Перенос отправления на {start_time_hour}:{x}. Ждите пожалуйста. Спасибо!')
    if start_time_hour == 23 and x > 55:
        start_time_hour = 0
        x = 0
        print(f'Перенос отправления на {start_time_hour}:{x}. Ждите пожалуйста. Спасибо!')

    print(f'Следующее отправление сообщения в {start_time_hour}:{x}')

    pywhatkit.sendwhatmsg(phone_numbers[n],
                          text_message,
                          start_time_hour, x)
    print(f'Сообщение на номер {phone_numbers[n]} отправлено.')
    print()
    print()
    n += 1
    x += 1

print()
print('####################')
print("Сообщения разосланы!")
print('Обязательно проверьте в мобильном терминале, последние отправленные сообщения!'
      ' Все ли сообщения были отправлены.'
      )
print('####################')
