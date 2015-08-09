﻿# -*- coding: utf-8 -*-
'''
    Torrenter v2 plugin for XBMC/Kodi
    Copyright (C) 2012-2015 Vadim Skorba v1 - DiMartino v2
    http://forum.kodi.tv/showthread.php?tid=214366

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

try:
    import xbmcaddon

    __settings__ = xbmcaddon.Addon(id='plugin.video.torrenter')

    language = ('en', 'ru', 'uk')[int(__settings__.getSetting("language"))]
except:
    language = 'ru'



def localize(text):
    dictionary = {
        'ru': {
            'Seeds searching.': 'Идёт поиск сидов.',
            'Please Wait': 'Подождите',
            'Information': 'Информация',
            'Torrent downloading is stopped.': 'Загрузка торрента прекращена.',
            'Search': 'Поиск',
            'Seeds': 'Сиды',
            'Peers': 'Пиры',
            'Materials are loading now.': 'Идёт загрузка материалов.',
            'Search Phrase': 'Фраза для поиска',
            'Magnet-link is converting': 'Идёт преобразование magnet-ссылки',
            'Error': 'Ошибка',
            'Your library out of date and can\'t save magnet-links.': 'Ваша библиотека устарела и не может сохранять магнет-ссылки.',
            'Bookmarks': 'Закладки',
            'Logout': 'Выход',
            'Login': 'Вход',
            'Recent Materials': 'Свежие Материалы ',
            'Register': 'Регистрация',
            'Bookmark': 'Закладка',
            'Item successfully added to Bookmarks': 'Элемент удачно добавлен в закладки',
            'Item successfully removed from Bookmarks': 'Элемент удачно удалён из закладок',
            'Bookmark not added': 'Закладка не добавлена',
            'Bookmark not removed': 'Закладка не удалена',
            'Add To Bookmarks': 'Добавить в закладки',
            'Remove From Bookmarks': 'Удалить из Закладок',
            'Auth': 'Авторизация',
            'Already logged in': 'Пользователь уже в системе',
            'Input Email (for password recovery):': 'Введите E-mail (для восстановления пароля):',
            'Input Email:': 'Введите E-mail:',
            'Input Password (6+ symbols):': 'Введите пароль (6+ символов):',
            'Input Password:': 'Введите пароль:',
            'Login successfull': 'Вход выполнен успешно',
            'Login failed': 'Вход не выполнен',
            'User not logged in': 'Пользователь не в системе',
            'User successfully logged out': 'Пользователь успешно покинул систему',
            'Preloaded: ': 'Предзагружено: ',
            'Do you want to STOP torrent downloading and seeding?': 'Вы хотите остановить загрузку и раздачу торрента?',
            'Torrent Downloading': 'Загрузка торрента',
            'Auth expired, please relogin': 'Авторизация истекла, пожалуйста войдите снова',
            'Storage': 'Хранилище',
            'Storage was cleared': 'Хранилище очищено',
            'Clear Storage': 'Очистить хранилище',
            'Popular': 'Популярное',
            'Views': 'Просмотров',
            'Uploading': 'Раздача',
            'Download': 'Скачать',
            'Input symbols from CAPTCHA image:': 'Введите символы с картинки CAPTCHA:',
            'Please, rate watched video:': 'Пожалуйста, оцените просмотренное видео:',
            'Bad': 'Плохо',
            'So-So': 'Такое...',
            'Good': 'Отлично',
            'Ratings': 'Оценки',
            'Rating': 'Оценка',
            'Retry': 'Повторная попытка',
            '%ds has left': 'Осталось %d попыток',
            'File failed to play! Do you want to RETRY and buffer more?': 'Ошибка проигрывания файла! Хотите предзагрузить больше и повторить?',
            'High Priority Files': 'Высокий Приоритет Файлам',
            'Skip All Files': 'Пропустить Все Файлы',
            'Start': 'Пуск',
            'Stop': 'Стоп',
            'Play':'Воспроизвести',
            'High Priority': 'Высокий Приоритет',
            'Skip File': 'Пропустить Файл',
            'Remove': 'Удалить',
            'Remove with files': 'Удалить с файлами',
            'Play File': 'Проиграть файл',
            'Start All Files': 'Пуск Всем Файлам',
            'Stop All Files': 'Стоп Всем Файлам',
            'Torrent-client Browser': 'Браузер Торрент-клиента',
            'Remote Torrent-client': 'Удаленный торрент-клиент',
            'You didn\'t set up replacement path in setting.': 'Вы не настроили замены путей.',
            'For example /media/dl_torr/ to smb://SERVER/dl_torr/. Setup now?': 'Например /media/dl_torr/ на smb://SERVER/dl_torr/. Настроить?',
            'Manual Torrent-client Path Edit': 'Вручную изменить папку торрент-клиента по-умолчанию',
            'Choose .torrent in video library': 'Выберите .torrent в видеобиблиотеке',
            '.torrent Player': '.torrent Проигрыватель',
            'Choose directory:': 'Выберите папку:',
            'Starting download next episode!': 'Начинаю скачку следующего эпизода!',
            'Choose in torrent-client:': 'Выберите раздачу:',
            'Search Control Window': 'Окно Управления Поиском',
            'Magnet-link (magnet:...)': 'Magnet-ссылка (magnet:...)',
            'Not a magnet-link!': 'Не является magnet-ссылкой',
            'Magnet-link Player': 'Проигрыватель Magnet-Ссылок',
            'UNKNOWN STATUS': 'Неизвестное состояние',
            'Checking preloaded files...': 'Проверка файлов...',
            'Waiting for website response...': 'Ожидание ответа сайта...',
            'Search and cache information for:': 'Поиск и кэширование информации для:',
            'Open Torrent': 'Открыть Список файлов',
            'Torrent list is empty.': 'Список раздач пуст.',
            'Content Lists': 'Списки Медиа',
            'Canceled by User': 'Отменено пользователем',
            'Do you want to search and cache full metadata + arts?': 'Хотите автоматически получать мета-данные и арты?',
            'This vastly decreases load speed, but you will be asked to download premade bases!': 'Это существенно снижает скорость загрузки, но Вам предложат скачать готовые базы!',
            'Do you want to preload full metadata?': 'Хотите готовую загрузить базу данных?',
            'It is highly recommended!': 'Настоятельно рекомендовано согласиться!',
            'TV Shows': 'Сериалы',
            'Cartoons': 'Мультфильмы',
            'Anime': 'Аниме',
            'Most Recent': 'Горячие Новинки',
            'Top 250 Movies': 'Лучшие 250 фильмов',
            'Top All Time': 'Лучшее за ВСЕ ВРЕМЯ',
            'by Genre': 'по Жанру',
            'by Year': 'по Году',
            'Action': 'Боевики',
            'Adventure': 'Приключения',
            'Animation': 'Анимация',
            'Biography': 'Биография',
            'Comedy': 'Комедии',
            'Crime': 'Детектив',
            'Documentary': 'Документальное',
            'Drama': 'Драмы',
            'Family': 'Семейное',
            'Fantasy': 'Фэнтази',
            'Film-Noir': 'Нуар',
            'History': 'Историчекие',
            'Horror': 'Ужасы',
            'Music': 'Музыкальные',
            'Musical': 'Мьюзиклы',
            'Mystery': 'Мистика',
            'Romance': 'Мелодрамы',
            'Sci-Fi': 'Фантастика',
            'Short': 'Короткометражки',
            'Sport': 'Спортивные',
            'Thriller': 'Триллеры',
            'War': 'Военные',
            'Western': 'Вестерны',
            '[B]by Site[/B]': '[B]по Сайту[/B]',
            'Cartoons Series': 'Мультсериалы',
            'Cartoons Short': 'Мультфильмы (короткометражки)',
            'Male': 'Мужские',
            'Female': 'Женские',
            'Russia & USSR': 'Россия + СССР',
            'Next Page': 'Следующая Страница',
            'Previous Page': 'Предыдущая Страница',
            'Russian Movies': 'Отечественные Фильмы',
            'Movies': 'Зарубежные Фильмы',
            'Anime Film': 'Полнометражное Аниме',
            'Anime Series': 'Аниме Сериалы',
            'Can\'t download torrent, probably no seeds available.': 'Не могу скачать торрент, скорее всего нет доступных сидов.',
            'Personal List': 'Личный Список',
            'Add to %s': 'Добавить в %s',
            'Delete from %s': 'Удалить из %s',
            'Added!': 'Добавлено',
            'Deleted!': 'Удалено!',
            'Search History': 'История Поиска',
            'Favourites': 'Избранное',
            'Favourites SH': 'Избранное ИП',
            'Clear %s': 'Очистить %s',
            'Clear!': 'Очищено!',
            'kb/s': 'Кб/с',
            'Queued': 'В очереди',
            'Checking': 'Проверка',
            'Downloading metadata': 'Скачивание мета-данных',
            'Downloading': 'Скачивание',
            'Finished': 'Окончено',
            'Seeding': 'Раздача (сидирование)',
            'Allocating': 'Allocating',
            'Allocating file & Checking resume': 'Allocating file & Checking resume',
            'For Kids': 'Детское',
            'Adult': 'Эротика',
            'Does not support magnet links!': 'Не поддерживает магнит-ссылки!',
            'Reset All Cache DBs': 'Сбросить Базы Данных',
            '[B]Search[/B]': '[B]Поиск[/B]',
            'You can always restart this by deleting DBs via Context Menu': 'Вы всегда можете перезапустить этот процесс через Контекстное Меню',
            'Your preloaded databases are outdated!': 'Ваши предзакаченные базы метаданных устарели!',
            'Do you want to download new ones right now?': 'Хотите прямо сейчас скачать новые?',
            'Individual Tracker Options':'Выбор Трекеров',
            'Downloading and copy subtitles. Please wait.':'Скачиваю и копирую субтитры. Пожалуйста подождите.',
            'International Check - First Run':'International Check - Первый запуск',
            'Delete Russian stuff?':'Удалить русские трекеры?',
            'Save to path':'Сохранить в папку',
            'Return Russian stuff':'Вернуть русские трекеры',
            '%d files have been returned':'%d файлов возвращено',
            'Download via T-client':'Скачать Торр-клиентом',
            'Download via Libtorrent':'Скачать Libtorrent\'ом',
            'Download Status':'Статус Загрузки',
            'Download has not finished yet':'Загрука не завершена',
            'Stopped and Deleted!':'Загрузка остановлена и удалена!',
            'Unpaused!':'Возобновлено!',
            'Paused!':'Приостановлено!',
            'Stopped!':'Остановлено!',
            'Started!':'Начинается загрузка!',
            'Delete and Stop':'Удалить и Остановить',
            'Unpause':'Возобновить',
            'Pause':'Пауза',
            'Delete':'Удалить',
            'Open (no return)':'Открыть (без возврата)',
            'Torrent is seeding. To stop it use Download Status.':'Сидирование. Для остановки используйте Статус Загрузки.',
            'Start All':'Запустить Все',
            'Started All!':'Все Запущены!',
            'Stopped All!':'Все Остановлено!',
            'Stop All':'Остановить Все',
            'Keyboard':'Клавиатура',
            'Copy Files in Root':'Скопировать файлы в Корень',
            'Copied %d files!':'Скопировано %d файлов!',
            'Add to MyShows.ru':'Добавить в MyShows.ru',
            'Return to MyShows.ru':'Вернуться в MyShows.ru',
            'Search results:':'Результаты поиска:',
            'by Seeders':'по Сидам',
            'by Date':'по Дате',
            'Sort':'Сортировка',
            'Close':'Закрыть окно',
            'Views:':'Просм.:',
            'Rating:':'Рейтинг:',
            'Information not found!':'Информация не найдена!',
            'Choose searcher':'Выберите трекер',
            'Python-Libtorrent Not Found':'Python-Libtorrent не найден',
            'Windows has static compiled python-libtorrent included.':'На Windows при установке из репозитория к плагину идет python-libtorrent.',
            'You should install "script.module.libtorrent" from "MyShows.me Kodi Repo"':'Установите "script.module.libtorrent" из "MyShows.me Kodi Repo"',
            'Linux x64 has not static compiled python-libtorrent included.':'На Linux x64 не смогли собрать статическую python-libtorrent',
            'You should install it by "sudo apt-get install python-libtorrent"':'Установи коммандой "sudo apt-get install python-libtorrent"',
            'Linux has static compiled python-libtorrent included but it didn\'t work.':'На Linux x86 есть статическая python-libtorrent, но она очевидно не сработала.',
            'As far as I know you can compile python-libtorrent for ARMv6-7.':'На ARMv6-7 можно скомпилировать python-libtorrent',
            'You should search for "OneEvil\'s OpenELEC libtorrent" or use Ace Stream.':'Поищи "OneEvil\'s OpenELEC libtorrent" или используй Ace Stream',
            'Please use install Ace Stream APK and choose it in Settings.':'Установите Ace Stream APK и выберите плеер в Найстройка плагина',
            'It is possible to compile python-libtorrent for Android, but I don\'t know how.':'Вообще скомпилировать python-libtorrent на Android можно, но мы не знаем как.',
            'It is possible to compile python-libtorrent for OS X.':'Вообще скомпилировать python-libtorrent на OS X можно.',
            'But you would have to do it by yourself, there is some info on github.com.':'Но придется это тебе делать самому, на гитхабе была инфа',
            'It is NOT possible to compile python-libtorrent for iOS.':'Под iOS невозможно скомпилировать python-libtorrent',
            'But you can use torrent-client control functions.':'Но все остальные функции кроме прямого стриминга с торрента работают.',
            'I added custom searchers to Torrenter v2!':'Я добавил внешние серчеры для трекеров в стиле Pulsar!',
            'Now you can use your login on trackers or write and install your own searcher!':'Теперь можно использовать свой логин или даже написать и установить свой серчер.',
            'Would you like to install %s from "MyShows.me Kodi Repo" in Programs section?':'Хотите установить %s из "MyShows.me Kodi Repo" в Программах?',
            'Open installation window?':'Открыть окно установки?',
            'Android Support':'Поддержка Android',
            'Android has no temprorary folder':'У Android отсутствует стандартная временная папка',
            'Please specify storage folder in Settings!':'Пожалуйста, укажите папку хранилища файлов!',
            'You have no installed or active searchers! More info in Search Control Window!':'У вас нет установленных или активных серчеров. Подробнее в Окне Управления Поиском.',
            'Please contact DiMartino on kodi.tv forum. We compiled python-libtorrent for Android,':'Свяжитесь с DiMartino на xbmc.ru. Мы собрали python-libtorrent на Android',
            'but we need your help with some tests on different processors.':'но нам нужна помощь в тестировании на разные процессоры.',
            'We added Android ARM full support to Torrenter v2!':'Мы добавили полную поддержку Android ARM в Torrenter v2!',
            'I deleted pre-installed ones, install them in Search Control Window!':'Теперь серчеры нужно устанавливать отдельно в Окне Управления Поиском!',
            'Torrenter didn\'t find %s searcher':'Торрентер не нашел серчер трекера %s',
            'Torrenter Tracker Install':'Установка трекеров в Torrenter',
            'Ask to save':'Спросить о сохранении',
            'Would you like to save this file?':'Хотите сохранить данный файл?',
            'Your storage path is not writable or not local! Please change it in settings!':'Ваше хранилище не доступно для записи или не локально! Измените в настройках!',
            'Upgrade advancedsettings.xml':'Обновление advancedsettings.xml',
            'We would like to set some advanced settings for you!':'Нам нужно обновить продвинутые настройки для работы!',
            'Do it!':'Скажите "ДА"!',
            'Please, restart Kodi now!':'Теперь перезагрузите Коди, пожалуйста!',
            './ (Root folder)':'./ (Корневой каталог)',
        },
        'uk': {
            'Seeds searching.': 'Йде пошук сідів.',
            'Please Wait': 'Зачекайте',
            'Information': 'Інформація',
            'Torrent downloading is stopped.': 'Завантаження торренту зупинено.',
            'Search': 'Пошук',
            'Seeds': 'Сіди',
            'Peers': 'Піри',
            'Materials are loading now.': 'Йде завантаження матеріалів.',
            'Search Phrase': 'Фраза для пошуку',
            'Magnet-link is converting.': 'Йде перетворення магнет-посилання.',
            'Error': 'Помилка',
            'Your library out of date and can\'t save magnet-links.': 'Ваша бібліотека застаріла і не може зберігати магнет-посилання.',
            'Bookmarks': 'Закладки',
            'Logout': 'Вихід',
            'Login': 'Вхід',
            'Recent Materials': 'Свіжі матеріали',
            'Register': 'Регістрація',
            'Bookmark': 'Закладка',
            'Item successfully added to Bookmarks': 'Элемент успішно доданий в закладки',
            'Item successfully removed from Bookmarks': 'Элемент успішно вилучений из закладок',
            'Bookmark not added': 'Закладка не додана',
            'Bookmark not removed': 'Закладка не вилучена',
            'Add To Bookmarks': 'Додати в закладки',
            'Remove From Bookmarks': 'Вилучити з закладок',
            'Auth': 'Авторизація',
            'Already logged in': 'Користувач вже в системі',
            'Input Email (for password recovery):': 'Введіть E-mail (для відновлення паролю):',
            'Input Email:': 'Введіть E-mail:',
            'Input Password (6+ symbols):': 'Введіть пароль (6+ символів):',
            'Input Password:': 'Введіть пароль:',
            'Login successfull': 'Вхід виконаний успішно',
            'Login failed': 'Вхід не виконаний',
            'User not logged in': 'Користувач не в системі',
            'User successfully logged out': 'Користувач успішно залишив систему',
            'Preloaded: ': 'Попередньо завантажено: ',
            'Do you want to STOP torrent downloading and seeding?': 'Ви бажаєте зупинити завантаження і раздачу торренту?',
            'Torrent Downloading': 'Завантаження торренту',
            'Auth expired, please relogin': 'Авторизація сплила, будь ласка, увійдіть знову',
            'Storage': 'Сховище',
            'Storage was cleared': 'Сховище очищене',
            'Clear Storage': 'Очистити сховище',
            'Popular': 'Популярне',
            'Views': 'Перегляди',
            'Uploading': 'Роздача',
            'Download': 'Завантажити',
            'Input symbols from CAPTCHA image:': 'Введіть символи з картинки CAPTCHA:',
            'Please, rate watched video:': 'Будь ласка, оцініть переглянуте відео:',
            'Bad': 'Погане',
            'So-So': 'Таке собі...',
            'Good': 'Добре',
            'Ratings': 'Оцінки',
            'Rating': 'Оцінка',
            'Retry': 'Повторна спроба',
            '%ds has left': 'Залишилось %d сброб',
            'File failed to play! Do you want to RETRY and buffer more?': 'Помилка відтворення файлу! Бажаєте спробувати знову і завантажити більше?',
            'High Priority Files': 'Файли високого пріоритету',
            'Skip All Files': 'Пропустити всі файли',
            'Start': 'Запустити',
            'Stop': 'Стоп',
            'Play':'Відтворити',
            'High Priority': 'Високий пріоритет',
            'Skip File': 'Пропустити файл',
            'Remove': 'Вилучити',
            'Remove with files': 'Вилучити з файлами',
            'Play File': 'Відтворити файл',
            'Start All Files': 'Запустити всі файли',
            'Stop All Files': 'Зупинити всі файли',
            'Torrent-client Browser': 'Браузер торрент-клієнта',
            'Remote Torrent-client': 'Віддалений торрент-клієнт',
            'You didn\'t set up replacement path in setting.': 'Вы не налаштували заміну шляху.',
            'For example /media/dl_torr/ to smb://SERVER/dl_torr/. Setup now?': 'Наприклад, /media/dl_torr/ на smb://SERVER/dl_torr/. Налаштувати?',
            'Manual Torrent-client Path Edit': 'Змінити вручну каталог торрент-клієнта',
            'Choose .torrent in video library': 'Виберіть .torrent у відеобібліотеці',
            '.torrent Player': '.torrent-програвач',
            'Choose directory:': 'Виберіть каталог:',
            'Starting download next episode!': 'Починається завантаження наступного епізоду!',
            'Choose in torrent-client:': 'Оберіть роздачу:',
            'Search Control Window': 'Вікно керування пошуком',
            'Magnet-link (magnet:...)': 'Магнет-посилання (magnet:...)',
            'Not a magnet-link!': 'Не є магнет-посиланням',
            'Magnet-link Player': 'Програвач магнет-посилань',
            'UNKNOWN STATUS': 'Невідомий стан',
            'Checking preloaded files...': 'Перевірка файлів...',
            'Waiting for website response...': 'Очікування відповіді сайту...',
            'Search and cache information for:': 'Пошук і кешування інформації для:',
            'Open Torrent': 'Відкрити список файлів',
            'Torrent list is empty.': 'Список роздач порожній.',
            'Content Lists': 'Списки медіа',
            'Canceled by User': 'Скасовано користувачем',
            'Do you want to search and cache full metadata + arts?': 'Бажаєте автоматично отримувати мета-дані та арти?',
            'This vastly decreases load speed, but you will be asked to download premade bases!': 'Це суттєво знижує швидкість завантаження, але вам буде запропоновано завантажити готові бази!',
            'Do you want to preload full metadata?': 'Бажаєте завантажити повні мета-дані?',
            'It is highly recommended!': 'Наполегливо рекомендується погодитись!',
            'TV Shows': 'Серіали',
            'Cartoons': 'Мультфільми',
            'Anime': 'Аніме',
            'Most Recent': 'Гарячі новинки',
            'Top 250 Movies': 'Найкращі 250 фільмів',
            'Top All Time': 'Краще за весь час',
            'by Genre': 'по Жанру',
            'by Year': 'по Року',
            'Action': 'Боєвики',
            'Adventure': 'Пригоди',
            'Animation': 'Анімація',
            'Biography': 'Біографія',
            'Comedy': 'Комедії',
            'Crime': 'Детектив',
            'Documentary': 'Документальне',
            'Drama': 'Драми',
            'Family': 'Сімейне',
            'Fantasy': 'Фентезі',
            'Film-Noir': 'Нуар',
            'History': 'Історичні',
            'Horror': 'Жахи',
            'Music': 'Музичні',
            'Musical': 'М\'юзикли',
            'Mystery': 'Містика',
            'Romance': 'Мелодрами',
            'Sci-Fi': 'Фантастика',
            'Short': 'Короткометражки',
            'Sport': 'Спортивні',
            'Thriller': 'Трилери',
            'War': 'Військові',
            'Western': 'Вестерни',
            '[B]by Site[/B]': '[B]по Сайту[/B]',
            'Cartoons Series': 'Мультсеріали',
            'Cartoons Short': 'Мультфільми (короткометражки)',
            'Male': 'Чоловічі',
            'Female': 'Жіночі',
            'Russia & USSR': 'Росія + СРСР',
            'Next Page': 'Наступна сторінка',
            'Previous Page': 'Попередня сторінка',
            'Russian Movies': 'Вітчизняні фільми',
            'Movies': 'Іноземні фільми',
            'Anime Film': 'Повнометражні аніме',
            'Anime Series': 'Аніме-серіали',
            'Can\'t download torrent, probably no seeds available.': 'Не вдаєть завантажити торрент, мабуть, немає доступних сідів.',
            'Personal List': 'Особистий список',
            'Add to %s': 'Додати в %s',
            'Delete from %s': 'Вилучити из %s',
            'Added!': 'Додано',
            'Deleted!': 'Вилучено!',
            'Search History': 'Історія пошуку',
            'Favourites': 'Вибране',
            'Favourites SH': 'Вибране SH',
            'Clear %s': 'Очистити %s',
            'Clear!': 'Очищено!',
            'kb/s': 'Кб/с',
            'Queued': 'В черзі',
            'Checking': 'Перевірка',
            'Downloading metadata': 'Завантаження мета-даних',
            'Downloading': 'Завантаження',
            'Finished': 'Завершено',
            'Seeding': 'Роздача (сідування)',
            'Allocating': 'Виділення',
            'Allocating file & Checking resume': 'Виділення файлу і перевірка резюме',
            'For Kids': 'Дитяче',
            'Adult': 'Еротика',
            'Does not support magnet links!': 'Не підтримує магнет-посилання!',
            'Reset All Cache DBs': 'Зкинути усі закешовані бази',
            '[B]Search[/B]': '[B]Пошук[/B]',
            'You can always restart this by deleting DBs via Context Menu': 'Ви завжди можете перезапустити, вилучивши бази через контекстне меню',
            'Your preloaded databases are outdated!': 'Ваші завантажені бази мета-даних застаріли!',
            'Do you want to download new ones right now?': 'Бажаєте завантажити нові прямо зараз?',
            'Individual Tracker Options':'Вибір трекерів',
            'Downloading and copy subtitles. Please wait.':'Завантаження та копіювання субтитрів. Будь ласка, зачекайте.',
            'International Check - First Run':'Міжнародна перевірка - перший запуск',
            'Delete Russian stuff?':'Вилучити російські трекери?',
            'Save to path':'Зберегти в каталог',
            'Return Russian stuff':'Повернути російські трекери',
            '%d files have been returned':'%d файлів повернуто',
            'Download via T-client':'Завантажити торрент-клієнтом',
            'Download via Libtorrent':'Завантажити Libtorrent\'ом',
            'Download Status':'Статус завантаження',
            'Download has not finished yet':'Завантаження не завершене',
            'Stopped and Deleted!':'Зупинено та Вилучено!',
            'Unpaused!':'Відновлено!',
            'Paused!':'Призупинено!',
            'Stopped!':'Зупинено!',
            'Started!':'Запущено!',
            'Delete and Stop':'Вилучити та зупинити',
            'Unpause':'Відновити',
            'Pause':'Пауза',
            'Delete':'Видалити',
            'Open (no return)':'Відкрити (без повернення)',
            'Torrent is seeding. To stop it use Download Status.':'Сідування. Для зупинки використовуйте Статус завантаження.',
            'Start All':'Запустити все',
            'Started All!':'Все запущене!',
            'Stopped All!':'Все зупинене!',
            'Stop All':'Зупинити все',
            'Keyboard':'Клавіатура',
            'Copy Files in Root':'Зкопіювати файли в корінь',
            'Copied %d files!':'Зкопійовано %d файлів!',
            'Add to MyShows.ru':'Додати в MyShows.ru',
            'Return to MyShows.ru':'Повернутись в MyShows.ru',
            'Search results:':'Результати пошуку:',
            'by Seeders':'по сідам',
            'by Date':'по даті',
            'Sort':'сортування',
            'Close':'Закрити вікно',
            'Views:':'Перегляди.:',
            'Rating:':'Рейтинг:',
            'Information not found!':'Інформація не знайдена!',
            'Choose searcher':'Оберіть трекер',
            'Python-Libtorrent Not Found':'Python-Libtorrent не знайдено',
            'Windows has static compiled python-libtorrent included.':'На Windows при встановленні з репозиторію разом з плагіном йде python-libtorrent.',
            'You should install "script.module.libtorrent" from "MyShows.me Kodi Repo"':'Встановіть "script.module.libtorrent" з "MyShows.me Kodi Repo"',
            'Linux x64 has not static compiled python-libtorrent included.':'На Linux x64 не змогли зібрати статичну версію python-libtorrent',
            'You should install it by "sudo apt-get install python-libtorrent"':'Встановіть командою "sudo apt-get install python-libtorrent"',
            'Linux has static compiled python-libtorrent included but it didn\'t work.':'На Linux x86 є статична версія python-libtorrent, але вона не спрацювала.',
            'As far as I know you can compile python-libtorrent for ARMv6-7.':'На ARMv6-7 можно скомпілювати python-libtorrent',
            'You should search for "OneEvil\'s OpenELEC libtorrent" or use Ace Stream.':'Пошукайте "OneEvil\'s OpenELEC libtorrent" або використовуйте Ace Stream',
            'Please use install Ace Stream APK and choose it in Settings.':'Встановіть Ace Stream APK і оберіть плеєр в Налаштуваннях',
            'It is possible to compile python-libtorrent for Android, but I don\'t know how.':'Скомпілювати python-libtorrent на Android можливо, але ми не знаємо як.',
            'It is possible to compile python-libtorrent for OS X.':'Скомпілювати python-libtorrent на OS X можливо.',
            'But you would have to do it by yourself, there is some info on github.com.':'Але це доведеться робити самому, на гітхабі була інформація',
            'It is NOT possible to compile python-libtorrent for iOS.':'Під iOS неможливо скомпілювати python-libtorrent',
            'But you can use torrent-client control functions.':'Але всі решта функцій, крім прямого стрімінгу, працюють.',
        }
    }
    try:
        return dictionary[language][text]
    except:
        if language=='uk':
            try:
                return dictionary['ru'][text]
            except:
                return text
        else:
            return text
