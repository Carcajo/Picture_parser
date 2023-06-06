from icrawler.builtin import GoogleImageCrawler
import time


print('Добро пожаловать в парсинг картинок')
x = input('Нажми n чтобы запустить парсинг\n')


if x == 'n':
    time.sleep(1)
    name = input('По какому запросу парсить картинки?\n')

    quantity = int(input('Сколько нужно спарсить картинок?\n'))
    path = input('Введите путь к месту сохранения картинок\n')
    google_crawler = GoogleImageCrawler(storage={'root_dir': path})

    google_crawler.crawl(keyword=name, max_num=quantity)

else:
    print('Такой команды нет')