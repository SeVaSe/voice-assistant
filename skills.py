import os
import webbrowser
import sys
import subprocess
import voice
import wikipedia


try:
    import requests
except:
    pass
#БРАУЗЕРЫ
def browser1():#Открывает браузер заданнный по уполчанию в системе с url указанным здесь
    webbrowser.open('https://www.youtube.com', new=2)
def browser2():
    webbrowser.open('https://www.google.com/', new=2)
def browser3():
    webbrowser.open('https://zetfix.online/', new=2)
def browser4():
    webbrowser.open('https://kip.eljur.ru/?user=sevase&domain=kip', new=2)
def browser5():
        webbrowser.open('https://vk.com/im', new=2)
def browser6():
        webbrowser.open('https://vk.com/audios564479476?section=all', new=2)
def browser7():
        webbrowser.open('https://vk.com/audios564479476?section=general', new=2)


def game():
    try:
        webbrowser.open('https://www.supremacy1914.com/game.php?L=14&bust=1#/home/overview/', new=2)
    except:
        voice.speaker('Что то пошло не так')

def read():
    try:
        webbrowser.open('https://python.swaroopch.com/control_flow.html', new=2)
    except:
        voice.speaker('Книжка не октрыта')


def offpc():# Эта команда отключает ПК
    #os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():#https://openweathermap.org для показывания погоды
    try:
        params = {'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'appid': '0d27a922b606c2a322cc9c171958cdbb'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot(): #Отключает бота
   sys.exit()


def passive():#Функция заглушка при простом диалоге с ботом
    pass


