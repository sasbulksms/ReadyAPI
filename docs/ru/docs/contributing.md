# Участие в разработке фреймворка

Возможно, для начала Вам стоит ознакомиться с основными способами [помочь ReadyApi или получить помощь](help-readyapi.md){.internal-link target=_blank}.

## Разработка

Если Вы уже склонировали репозиторий и знаете, что Вам нужно более глубокое погружение в код фреймворка, то здесь представлены некоторые инструкции по настройке виртуального окружения.

### Виртуальное окружение с помощью `venv`

Находясь в нужной директории, Вы можете создать виртуальное окружение при помощи Python модуля `venv`.

<div class="termy">

```console
$ python -m venv env
```

</div>

Эта команда создаст директорию `./env/` с бинарными (двоичными) файлами Python, а затем Вы сможете скачивать и устанавливать необходимые библиотеки в изолированное виртуальное окружение.

### Активация виртуального окружения

Активируйте виртуально окружение командой:

=== "Linux, macOS"

    <div class="termy">

    ```console
    $ source ./env/bin/activate
    ```

    </div>

=== "Windows PowerShell"

    <div class="termy">

    ```console
    $ .\env\Scripts\Activate.ps1
    ```

    </div>

=== "Windows Bash"

    Если Вы пользуетесь Bash для Windows (например: <a href="https://gitforwindows.org/" class="external-link" target="_blank">Git Bash</a>):

    <div class="termy">

    ```console
    $ source ./env/Scripts/activate
    ```

    </div>

Проверьте, что всё сработало:

=== "Linux, macOS, Windows Bash"

    <div class="termy">

    ```console
    $ which pip

    some/directory/readyapi/env/bin/pip
    ```

    </div>

=== "Windows PowerShell"

    <div class="termy">

    ```console
    $ Get-Command pip

    some/directory/readyapi/env/bin/pip
    ```

    </div>

Если в терминале появится ответ, что бинарник `pip` расположен по пути `.../env/bin/pip`, значит всё в порядке. 🎉

Во избежание ошибок в дальнейших шагах, удостоверьтесь, что в Вашем виртуальном окружении установлена последняя версия `pip`:

<div class="termy">

```console
$ python -m pip install --upgrade pip

---> 100%
```

</div>

!!! tip "Подсказка"
    Каждый раз, перед установкой новой библиотеки в виртуальное окружение при помощи `pip`, не забудьте активировать это виртуальное окружение.

    Это гарантирует, что если Вы используете библиотеку, установленную этим пакетом, то Вы используете библиотеку из Вашего локального окружения, а не любую другую, которая может быть установлена глобально.

### pip

После активации виртуального окружения, как было указано ранее, введите следующую команду:

<div class="termy">

```console
$ pip install -r requirements.txt

---> 100%
```

</div>

Это установит все необходимые зависимости в локальное окружение для Вашего локального ReadyApi.

#### Использование локального ReadyApi

Если Вы создаёте Python файл, который импортирует и использует ReadyApi,а затем запускаете его интерпретатором Python из Вашего локального окружения, то он будет использовать код из локального ReadyApi.

И, так как при вводе вышеупомянутой команды был указан флаг `-e`, если Вы измените код локального ReadyApi, то при следующем запуске этого файла, он будет использовать свежую версию локального ReadyApi, который Вы только что изменили.

Таким образом, Вам не нужно "переустанавливать" Вашу локальную версию, чтобы протестировать каждое изменение.

### Форматировние

Скачанный репозиторий содержит скрипт, который может отформатировать и подчистить Ваш код:

<div class="termy">

```console
$ bash scripts/format.sh
```

</div>

Заодно он упорядочит Ваши импорты.

Чтобы он сортировал их правильно, необходимо, чтобы ReadyApi был установлен локально в Вашей среде, с помощью команды из раздела выше, использующей флаг `-e`.

## Документация

Прежде всего, убедитесь, что Вы настроили своё окружение, как описано выше, для установки всех зависимостей.

Документация использует <a href="https://www.mkdocs.org/" class="external-link" target="_blank">MkDocs</a>.

Также существуют дополнительные инструменты/скрипты для работы с переводами в `./scripts/docs.py`.

!!! tip "Подсказка"

    Нет необходимости заглядывать в `./scripts/docs.py`, просто используйте это в командной строке.

Вся документация имеет формат Markdown и расположена в директории `./docs/en/`.

Многие руководства содержат блоки кода.

В большинстве случаев эти блоки кода представляют собой вполне законченные приложения, которые можно запускать как есть.

На самом деле, эти блоки кода не написаны внутри Markdown, это Python файлы в директории `./docs_src/`.

И эти Python файлы включаются/вводятся в документацию при создании сайта.

### Тестирование документации


Фактически, большинство тестов запускаются с примерами исходных файлов в документации.

Это помогает убедиться, что:

* Документация находится в актуальном состоянии.
* Примеры из документации могут быть запущены как есть.
* Большинство функций описаны в документации и покрыты тестами.

Существует скрипт, который во время локальной разработки создаёт сайт и проверяет наличие любых изменений, перезагружая его в реальном времени:

<div class="termy">

```console
$ python ./scripts/docs.py live

<span style="color: green;">[INFO]</span> Serving on http://127.0.0.1:8008
<span style="color: green;">[INFO]</span> Start watching changes
<span style="color: green;">[INFO]</span> Start detecting changes
```

</div>

Он запустит сайт документации по адресу: `http://127.0.0.1:8008`.


Таким образом, Вы сможете редактировать файлы с документацией или кодом и наблюдать изменения вживую.

#### Typer CLI (опционально)


Приведенная ранее инструкция показала Вам, как запускать скрипт `./scripts/docs.py` непосредственно через интерпретатор `python` .

Но также можно использовать <a href="https://typer.khulnasoft.com/typer-cli/" class="external-link" target="_blank">Typer CLI</a>, что позволит Вам воспользоваться автозаполнением команд в Вашем терминале.

Если Вы установили Typer CLI, то для включения функции автозаполнения, введите эту команду:

<div class="termy">

```console
$ typer --install-completion

zsh completion installed in /home/user/.bashrc.
Completion will take effect once you restart the terminal.
```

</div>

### Приложения и документация одновременно

Если Вы запускаете приложение, например так:

<div class="termy">

```console
$ uvicorn tutorial001:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

По умолчанию Uvicorn будет использовать порт `8000` и не будет конфликтовать с сайтом документации, использующим порт `8008`.

### Переводы на другие языки

Помощь с переводами ценится КРАЙНЕ ВЫСОКО! И переводы не могут быть сделаны без помощи сообщества. 🌎 🚀

Ниже приведены шаги, как помочь с переводами.

#### Подсказки и инструкции

* Проверьте <a href="https://github.com/khulnasoft/readyapi/pulls" class="external-link" target="_blank">существующие пул-реквесты</a> для Вашего языка. Добавьте отзывы с просьбой внести изменения, если они необходимы, или одобрите их.

!!! tip "Подсказка"
    Вы можете <a href="https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request" class="external-link" target="_blank">добавлять комментарии с предложениями по изменению</a> в существующие пул-реквесты.

    Ознакомьтесь с документацией о <a href="https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews" class="external-link" target="_blank">добавлении отзыва к пул-реквесту</a>, чтобы утвердить его или запросить изменения.

* Проверьте <a href="https://github.com/khulnasoft/readyapi/issues" class="external-link" target="_blank">проблемы и вопросы</a>, чтобы узнать, есть ли кто-то, координирующий переводы для Вашего языка.

* Добавляйте один пул-реквест для каждой отдельной переведённой страницы. Это значительно облегчит другим его просмотр.

Для языков, которые я не знаю, прежде чем добавить перевод в основную ветку, я подожду пока несколько других участников сообщества проверят его.

* Вы также можете проверить, есть ли переводы для Вашего языка и добавить к ним отзыв, который поможет мне убедиться в правильности перевода. Тогда я смогу объединить его с основной веткой.

* Используйте те же самые примеры кода Python. Переводите только текст документации. Вам не нужно ничего менять, чтобы эти примеры работали.

* Используйте те же самые изображения, имена файлов и ссылки. Вы не должны менять ничего для сохранения работоспособности.

* Чтобы узнать 2-буквенный код языка, на который Вы хотите сделать перевод, Вы можете воспользоваться таблицей <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" class="external-link" target="_blank">Список кодов языков ISO 639-1</a>.

#### Существующий язык

Допустим, Вы хотите перевести страницу на язык, на котором уже есть какие-то переводы, например, на испанский.

Кодом испанского языка является `es`. А значит директория для переводов на испанский язык: `docs/es/`.

!!! tip "Подсказка"
    Главный ("официальный") язык - английский, директория для него `docs/en/`.

Вы можете запустить сервер документации на испанском:

<div class="termy">

```console
// Используйте команду "live" и передайте код языка в качестве аргумента командной строки
$ python ./scripts/docs.py live es

<span style="color: green;">[INFO]</span> Serving on http://127.0.0.1:8008
<span style="color: green;">[INFO]</span> Start watching changes
<span style="color: green;">[INFO]</span> Start detecting changes
```

</div>

Теперь Вы можете перейти по адресу: <a href="http://127.0.0.1:8008" class="external-link" target="_blank">http://127.0.0.1:8008</a> и наблюдать вносимые Вами изменения вживую.


Если Вы посмотрите на сайт документации ReadyApi, то увидите, что все страницы есть на каждом языке. Но некоторые страницы не переведены и имеют уведомление об отсутствующем переводе.

Но когда Вы запускаете сайт локально, Вы видите только те страницы, которые уже переведены.


Предположим, что Вы хотите добавить перевод страницы [Основные свойства](features.md){.internal-link target=_blank}.

* Скопируйте файл:

```
docs/en/docs/features.md
```

* Вставьте его точно в то же место, но в директорию языка, на который Вы хотите сделать перевод, например:

```
docs/es/docs/features.md
```

!!! tip "Подсказка"
    Заметьте, что в пути файла мы изменили только код языка с `en` на `es`.

* Теперь откройте файл конфигурации MkDocs для английского языка, расположенный тут:

```
docs/en/mkdocs.yml
```

* Найдите в файле конфигурации место, где расположена строка `docs/features.md`. Похожее на это:

```YAML hl_lines="8"
site_name: ReadyApi
# More stuff
nav:
- ReadyApi: index.md
- Languages:
  - en: /
  - es: /es/
- features.md
```

* Откройте файл конфигурации MkDocs для языка, на который Вы переводите, например:

```
docs/es/mkdocs.yml
```

* Добавьте строку `docs/features.md` точно в то же место, как и в случае для английского, как-то так:

```YAML hl_lines="8"
site_name: ReadyApi
# More stuff
nav:
- ReadyApi: index.md
- Languages:
  - en: /
  - es: /es/
- features.md
```

Убедитесь, что при наличии других записей, новая запись с Вашим переводом находится точно в том же порядке, что и в английской версии.

Если Вы зайдёте в свой браузер, то увидите, что в документации стал отображаться Ваш новый раздел.🎉

Теперь Вы можете переводить эту страницу и смотреть, как она выглядит при сохранении файла.

#### Новый язык

Допустим, Вы хотите добавить перевод для языка, на который пока что не переведена ни одна страница.

Скажем, Вы решили сделать перевод для креольского языка, но его еще нет в документации.

Перейдите в таблицу кодов языков по ссылке указанной выше, где найдёте, что кодом креольского языка является `ht`.

Затем запустите скрипт, генерирующий директорию для переводов на новые языки:

<div class="termy">

```console
// Используйте команду new-lang и передайте код языка в качестве аргумента командной строки
$ python ./scripts/docs.py new-lang ht

Successfully initialized: docs/ht
Updating ht
Updating en
```

</div>

После чего Вы можете проверить в своем редакторе кода, что появился новый каталог `docs/ht/`.

!!! tip "Подсказка"
    Создайте первый пул-реквест, который будет содержать только пустую директорию для нового языка, прежде чем добавлять переводы.

    Таким образом, другие участники могут переводить другие страницы, пока Вы работаете над одной. 🚀

Начните перевод с главной страницы `docs/ht/index.md`.

В дальнейшем можно действовать, как указано в предыдущих инструкциях для "существующего языка".

##### Новый язык не поддерживается

Если при запуске скрипта `./scripts/docs.py live` Вы получаете сообщение об ошибке, что язык не поддерживается, что-то вроде:

```
 raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: partials/language/xx.html
```

Сие означает, что тема не поддерживает этот язык (в данном случае с поддельным 2-буквенным кодом `xx`).

Но не стоит переживать. Вы можете установить языком темы английский, а затем перевести текст документации.

Если возникла такая необходимость, отредактируйте `mkdocs.yml` для Вашего нового языка. Это будет выглядеть как-то так:

```YAML hl_lines="5"
site_name: ReadyApi
# More stuff
theme:
  # More stuff
  language: xx
```

Измените `xx` (код Вашего языка) на `en` и перезапустите сервер.

#### Предпросмотр результата

Когда Вы запускаете скрипт `./scripts/docs.py` с командой `live`, то будут показаны файлы и переводы для указанного языка.

Но когда Вы закончите, то можете посмотреть, как это будет выглядеть по-настоящему.

Для этого сначала создайте всю документацию:

<div class="termy">

```console
// Используйте команду "build-all", это займёт немного времени
$ python ./scripts/docs.py build-all

Updating es
Updating en
Building docs for: en
Building docs for: es
Successfully built docs for: es
Copying en index.md to README.md
```

</div>

Скрипт сгенерирует `./docs_build/` для каждого языка. Он добавит все файлы с отсутствующими переводами с пометкой о том, что "у этого файла еще нет перевода". Но Вам не нужно ничего делать с этим каталогом.

Затем он создаст независимые сайты MkDocs для каждого языка, объединит их и сгенерирует конечный результат на `./site/`.

После чего Вы сможете запустить сервер со всеми языками командой `serve`:

<div class="termy">

```console
// Используйте команду "serve" после того, как отработает команда "build-all"
$ python ./scripts/docs.py serve

Warning: this is a very simple server. For development, use mkdocs serve instead.
This is here only to preview a site with translations already built.
Make sure you run the build-all command first.
Serving at: http://127.0.0.1:8008
```

</div>

## Тесты

Также в репозитории есть скрипт, который Вы можете запустить локально, чтобы протестировать весь код и сгенерировать отчеты о покрытии тестами в HTML:

<div class="termy">

```console
$ bash scripts/test-cov-html.sh
```

</div>

Эта команда создаст директорию `./htmlcov/`, в которой будет файл `./htmlcov/index.html`. Открыв его в Вашем браузере, Вы можете в интерактивном режиме изучить, все ли части кода охвачены тестами.