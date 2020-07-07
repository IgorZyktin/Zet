# Zet

Набор инструментов для ведения заметок по методу **Zettelkasten**.

Пример того, что выдаёт линковщик:

![logo]

[logo]: ./graph.gif "Пример графа заметок"

## Что это за метод?

Он был придуман немецким социологом [Никласом Луманом](https://ru.wikipedia.org/wiki/%D0%9B%D1%83%D0%BC%D0%B0%D0%BD,_%D0%9D%D0%B8%D0%BA%D0%BB%D0%B0%D1%81).

Метод строится на применении упорядоченного набора листков бумаги. Каждый листок должен быть пронумерован и содержать одну специфическую идею. Листки могут содержать ссылки друг на друга и обобщающие теги. По своей сути, зеттелькастен напоминает гипертекст. Все листки хранятся в пронумерованных ящиках, за счёт чего листок с любым номером можно быстрой найти. 

Основные идеи:

1. Отсутствии категорий. Информация в системе хранится в структуре похожей на дерево, но введение каких-либо категорий не предусматривается. За счёт этого проще добавлять информацию, не имеющую чётко определённой области.
2. Отсутствует проблема переполнения данными. Система работает тем лучше, чем больше в ней информации.
3. Желательно использование максимально примитивных технологий. Предполагается, что система создаётся один раз и на всю жизнь, поэтому не должно быть зависимости от конкретного приложения, формата или чего то подобного.
4. Желательно максимальное количество ссылок в системе. Информация, не сцепленная с другими заметками не будет работать.
5. Ничего не удаляется. При пересмотре содержимого лучше добавлять заметки, описывающие, почему предыдущие были неправильными.

Набор этих простейших правил создаёт очень удобную и максимально живучую систему сохранения знаний.

## Для чего этот репозиторий

Чтобы было удобнее вести заметки. Главный инструмент здесь это автоматический линковщик, сшивающий заметки между собой по указанным в них тегам. Ещё он умеет создавать дополнительные страницы для тегов, что было понятно, где они упоминаются.

В основе лежат две идеи:
1. Чем проще инструмент планирования, тем выше шанс, что тебе будет не лень им пользоваться.
1. Сделать проще невозможно.

Серьёзно, что может быть проще пачки текстовых документов? Предполагается, что архив заметок будет лежать в сетевом хранилище вроде Yandex Disk / Google drive / Dropbox. Для работы не требуются сторонние приложения и интернет.

Желательно при этом, чтобы каталог контролировался системой контроля версий, например git.

## Как пользоваться

Для начала работы надо сохранить себе *linker.py* и всю папку *lib*. Клонировать репозиторий не обязательно, можно просто сохранить файлы. Необходим установленный python (желательно версии 3.8 и выше). Его можно скачать по ссылке в конце статьи. Никакие сторонние библиотеки и виртуальные окружения для работы не нужны.

### Начало работы

Надо создать несколько файлов с заметками в формате markdown.
 
Желательный формат заметок:
```markdown
# Название заметки

Краткое описание

---
\#тег номер один

\#тег номер два

\#тег номер три

## Заголовок

Текст, в котором может быть что-то про \#тег номер два например.
```

Заголовком статьи будет считаться первое, что идёт после октоторпа (#). Тегами будет считаться всё, нашлось в шапке документа, идёт после \\# без пробела и продолжается до конца строки. Линковщик умеет искать теги и в теле документа, но в первую очередь он опирается на перечисление тегов перед самим текстом заметки. Важно помнить, что у тегов не предусмотрено знака их окончания. Поэтому они в примере приводятся каждый на своей строке.

После этого можно запускать линковщик. Если всё пройдёт хорошо, текст изменится на:
```markdown
# Название заметки

Краткое описание

---
[\#тег номер один](./meta_teg_nomer_odin.md)

[\#тег номер два](./meta_teg_nomer_dva.md)

[\#тег номер три](./meta_teg_nomer_tri.md)

## Заголовок

Текст, в котором может быть что-то про [\#тег номер два](./meta_teg_nomer_dva.md) например.
```
Видно, что сам текст заметки остался тем же, но теперь теги это не просто текст, а реальные ссылки на другие документы.

### Применение линковщика

После того как все заметки написаны:
1. Открыть консоль (Win+R), убедиться, что мы находимся в каталоге с заметками.
1. Вызвать линковщик командой **python linker.py**.

После этого линковщик просканирует все файлы в каталоге и:
1. Выполнит замену текста тегов на соответствующие им гиперссылки. md документы ссылаются на md документы, html на html.
1. Создаст метафайлы meta_*.md для каждого тега, где будет перечислено в каких документах этот тег упоминается.
1. Создаст метафайлы meta_*.html для каждого тега, где будет нарисовано облако из документов с этим тегом.
1. Создаст метафайл index.html, в котором будет граф из всех тегов и всех документов.

Примерно вот так:
```
C:\notes>python linker.py
Сохранены изменения в файле "meta_seryy.md"
Сохранены изменения в файле "meta_seryy.html"
Сохранены изменения в файле "meta_hobot.md"
Сохранены изменения в файле "meta_hobot.html"
Сохранены изменения в файле "meta_4_lapy.md"
Сохранены изменения в файле "meta_4_lapy.html"
Сохранены изменения в файле "meta_hvost.md"
Сохранены изменения в файле "meta_hvost.html"
Сохранены изменения в файле "meta_mashina.md"
Сохранены изменения в файле "meta_mashina.html"
Сохранены изменения в файле "index.html"
```
Важно помнить, что линковщик это не динамический инструмент. Он не нужен для чтения заметок, только для их сшивки. Достаточно время от времени запускать его на одном компьютере, где установлен python. Читать заметки при этом можно с любого устройства, python при этом не требуется. 

После внесения изменений в заметки, линковщик должен быть запущен повторно. Он опять создаст все мета документы и стартовую страницу. Предполагается, что в пределах нескольких тысяч заметок это будет работать достаточно быстро. 

Сразу после этого уже можно работать. Но пользоваться html документами будет не очень удобно т.к. нельзя будет нормально переходить по кликам. Чтобы это можно было делать, необходимо расширение для браузера. В данном проекте применён Local Explorer (ссылка внизу). После его установки, Chrome будет запускать md документы через стандартное приложение операционной системы.

### Справочные данные

1. Подробнее про **Zettelkasten**: 
    * http://vonoiral.com/all/zettelkasten/
    
1. Подробнее про **jQuery** (обеспечивает работу скриптов в данном проекте): 
    * https://jquery.com/
    * Скачать тут: https://jquery.com/download/
    
1. Подробнее про **arbor.js** (рисует графы в данном проекте): 
    * http://arborjs.org/
    * Скачать тут: http://arborjs.org/js/dist/arbor-v0.92.zip
    
1. Подробнее про **python** (на этом языке написан линковщик): 
    * https://pythonworld.ru/osnovy/skachat-python.html
    * Скачать тут: https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe
    
1. Подробнее про **typora** (я применяю этот markdown редактор):
    * https://typora.io/
    * Скачать https://typora.io/#windows
    * Скачать https://typora.io/#linux
       
1. Подробнее про **Local Explorer** (позволяет открывать гиперссылки как файлы):
    * https://chrome.google.com/webstore/detail/local-explorer-file-manag/eokekhgpaakbkfkmjjcbffibkencdfkl
    * Скачать тут: http://goo.gl/trX9bB
