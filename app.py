import queue
import sounddevice as sd
import vosk
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *
import voice

q = queue.Queue()

model = vosk.Model("D:\sevase_GS\model_small\model_small")

device = sd.default.device          # sd.default.device == 1, 3  ////input, output [1, 4]
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def callback(indata, frames, time, status):

    q.put(bytes(indata))

def recognize(data, vectorizer, clf):
    trg = words.TRIGGERS.intersection(data.split()) #делает проверку, если тригерных слов нету то ретерн возращает проверку в начало
    if not trg:
        return
    data.replace(list(trg)[0], '') # удаляем имя бота из текста
    text_vector = vectorizer.transform([data]).toarray()[0]# получаем вектор полученного текста
    answer = clf.predict([text_vector])[0]# сравниваем с вариантами, получая наиболее подходящий ответ


    func_name = answer.split()[0]#получение имени функции из ответа из data_set
    voice.speaker(answer.replace(func_name, ''))#озвучка ответа из модели data_set + удаление опозновающ. слова
    exec(func_name + '()')#запуск функции из skills

def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys())) #получаем ключи списка, метод хэширует фразы и строит по ним векторы, какой либо масив из матрицы цифр. Похожие фразы, которые и будут содерж похожие слова , то их векторы будут совпадать => машина будет распозновать слова в любых похожих предложениях

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values())) # берем ответы, а не ключи уже. После идет некая проверка, в которой опред, совпадение ключа и ответа и после выводится ответ :)

    del words.data_set


    with sd.RawInputStream(samplerate=samplerate, blocksize = 2000, device=device[0], dtype='int16',    # device[0] == micro
                            channels=1, callback=callback):      # callback записывает данные

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):    # если остановится голос, начнется расшифровка вводимых данных
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
     main()
