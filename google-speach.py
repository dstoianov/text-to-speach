import csv
import os
from gtts import gTTS


def file_to_audio(csv_file_dict, file_to_save, play=False):
    words = []
    translations = []

    print("Reading the file {} ".format(csv_file_dict))
    with open(csv_file_dict, newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        languages = reader.fieldnames
        for row in reader:
            print(row[languages[0]], " --- ", row[languages[1]])
            words.append(" " + row[languages[0]].strip() + " ")
            translations.append(" " + row[languages[1]].strip() + " ")

    print("\nDict has {} langs".format(languages))
    print("Dict has '{}' words to save\n".format(str(len(words))))
    # print(words)
    # print(translations)

    with open(file_to_save, 'wb') as mp3_file:
        for t1, t2 in zip(words, translations):
            print("Adding the word '{}' - '{}'".format(t1, t2))
            synt_word = gTTS(text=str(t1), lang=languages[0])
            synt_trans = gTTS(text=str(t2), lang=languages[1])
            synt_word.write_to_fp(mp3_file)
            synt_trans.write_to_fp(mp3_file)
            synt_word.write_to_fp(mp3_file)

    print("Saved in file {}\nDone.".format(file_to_save))

    if play:
        os.system("mpg321 " + file_to_save)


def main():
    files = [file for file in os.listdir("dict/") if file.endswith(".csv")]
    print("Have '{}' dicts for converting".format(str(len(files))))

    for file in files:
        full_dict_path = os.path.abspath("dict/" + file)
        dir_name = os.path.dirname(full_dict_path)
        file_to_save = "{}/{}_audio.mp3".format(dir_name, file.split('.')[0])

        file_to_audio(full_dict_path, file_to_save)


if __name__ == '__main__':
    main()
