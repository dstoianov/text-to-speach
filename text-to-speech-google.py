import os
from gtts import gTTS


def main():
    tts = gTTS(text='Доброе Утро', lang='ru')
    # tts = gTTS(text='Good morning', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")


if __name__ == '__main__':
    main()
